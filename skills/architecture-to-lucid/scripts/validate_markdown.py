#!/usr/bin/env python3
"""Validate/extract Architecture Markdown v1 without third-party dependencies.

This helper performs no network calls and never creates or edits Lucid documents.
"""

import argparse
import json
import re
import sys
from pathlib import Path


ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
STATUSES = {"Confirmed", "Proposed", "Open"}
HEADERS = {
    "Metadata": ["Field", "Value"],
    "Sources": ["ID", "Reference", "Locator"],
    "Elements": ["ID", "Name", "Type", "Parent", "Scope", "Responsibility", "Technology", "Deployment", "Shape", "Status", "Sources"],
    "Relationships": ["ID", "Source", "Target", "Action", "Details", "Status", "Sources"],
    "Views": ["ID", "Level", "Title", "Focus", "Elements", "Relationships", "Status"],
    "Constraints": ["ID", "Rule", "Status", "Sources"],
    "Open questions": ["ID", "Question", "Affects"],
}
OPTIONAL = {
    "Elements": {"Technology", "Deployment", "Status", "Sources"},
    "Relationships": {"Details", "Status", "Sources"},
    "Views": {"Status"},
    "Constraints": {"Status", "Sources"},
}


def cells(line):
    """Split a pipe table row, preserving literal escaped pipes."""
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    result, current = [], []
    pos = 0
    while pos < len(text):
        char = text[pos]
        if char == "\\" and pos + 1 < len(text) and text[pos + 1] == "|":
            current.append("|")
            pos += 2
            continue
        if char == "|":
            result.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        pos += 1
    result.append("".join(current).strip())
    return result


def listed(value):
    if value.strip() in {"", "-"}:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def empty(value):
    return value.strip() in {"", "-"}


def parse_markdown(text):
    sections, sequence_ids, errors = {}, [], []
    current = None
    fence = None
    code = []
    blocks = []
    for line_number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})([^\s]*)\s*$", line)
        if fence:
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence) and not marker.group(2):
                blocks.append((current, code_language, "\n".join(code)))
                fence, code = None, []
            else:
                code.append(line)
            continue
        if marker:
            fence, code_language = marker.group(1), marker.group(2).lower()
            code = []
            continue
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1)
            if current in sections:
                errors.append(f"line {line_number}: duplicate section {current!r}")
            sections.setdefault(current, [])
            if current.startswith("Sequence: "):
                sequence_ids.append(current)
            continue
        if current and line.lstrip().startswith("|"):
            sections[current].append((line_number, cells(line)))
    if fence:
        errors.append("unterminated code fence")

    def table(section, expected):
        rows = sections.get(section, [])
        if not rows:
            errors.append(f"{section}: missing table")
            return []
        actual = rows[0][1]
        optional = OPTIONAL.get(section, set())
        required = set(expected) - optional
        if len(actual) != len(set(actual)) or not required.issubset(actual) or not set(actual).issubset(expected):
            errors.append(f"{section}: required columns {sorted(required)}; optional columns {sorted(optional)}")
            return []
        if len(rows) < 2 or len(rows[1][1]) != len(actual) or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1][1]):
            errors.append(f"{section}: missing or invalid table separator")
            return []
        records = []
        for number, row in rows[2:]:
            if len(row) != len(actual):
                errors.append(f"line {number}: {section} has {len(row)} cells; expected {len(actual)}")
                continue
            record = dict(zip(actual, row))
            for key in optional:
                record.setdefault(key, None)
            records.append(record)
        return records

    raw = {name: table(name, header) for name, header in HEADERS.items()}
    metadata = {}
    for row in raw["Metadata"]:
        if row["Field"] in metadata:
            errors.append(f"Metadata: duplicate field {row['Field']}")
        metadata[row["Field"]] = row["Value"]
    for field, value in {"Format version": "1", "Document status": "draft", "Language": "en", "Mode": "logical", "Default status": "Proposed", "Default sources": "-"}.items():
        metadata.setdefault(field, value)
    model = {"metadata": metadata}
    list_columns = {"Sources", "Elements", "Relationships", "Participants", "Affects"}
    for name, key in [("Sources", "sources"), ("Elements", "elements"), ("Relationships", "relationships"), ("Views", "views"), ("Constraints", "constraints"), ("Open questions", "open_questions")]:
        model[key] = []
        for row in raw[name]:
            normalized = {}
            for column, value in row.items():
                if value is None:
                    value = metadata["Default status"] if column == "Status" else metadata["Default sources"] if column == "Sources" else "-"
                normalized[column.lower().replace(" ", "_")] = listed(value) if column in list_columns else value
            model[key].append(normalized)
    model["sequences"] = []
    for heading in sequence_ids:
        seq_id = heading.removeprefix("Sequence: ").strip()
        fields = {}
        for row in table(heading, ["Field", "Value"]):
            if row["Field"] in fields:
                errors.append(f"{heading}: duplicate field {row['Field']}")
            fields[row["Field"]] = row["Value"]
        for required in ["Title", "Participants", "Status", "Sources"]:
            if empty(fields.get(required, "")):
                errors.append(f"{heading}: missing {required}")
        sources = [block for section, language, block in blocks if section == heading and language == "plantuml"]
        if len(sources) != 1:
            errors.append(f"{heading}: expected exactly one plantuml block")
        model["sequences"].append({"id": seq_id, "title": fields.get("Title", ""), "participants": listed(fields.get("Participants", "")), "status": fields.get("Status", ""), "sources": listed(fields.get("Sources", "")), "markup": sources[0] if sources else ""})
    return model, errors


def validate_sequence(sequence, elements, errors):
    prefix = sequence["id"]
    markup = sequence["markup"]
    declared = {}
    stack, in_note, messages = [], False, 0
    for line in markup.splitlines():
        line = line.strip()
        if not line or line.startswith("'"):
            continue
        if in_note:
            if line == "end note":
                in_note = False
            continue
        declaration = re.fullmatch(r'(actor|participant|boundary|control|entity|database)\s+(?:"([^"]+)"\s+as\s+([A-Za-z][A-Za-z0-9_]*)|([A-Za-z][A-Za-z0-9_]*))(?:\s+#[0-9A-Fa-f]{3,8})?', line)
        if declaration:
            alias = declaration.group(3) or declaration.group(4)
            name = declaration.group(2) or declaration.group(4)
            if alias in declared:
                errors.append(f"{prefix}: duplicate participant alias {alias}")
            declared[alias] = name
            if alias in elements and name != elements[alias]["name"]:
                errors.append(f"{prefix}: participant {alias} display name differs from Elements")
            continue
        message = re.fullmatch(r"([A-Za-z][A-Za-z0-9_]*)\s*(-->>|->>|-->|->)\s*([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.+)", line)
        if message:
            messages += 1
            for alias in [message.group(1), message.group(3)]:
                if alias not in sequence["participants"]:
                    errors.append(f"{prefix}: message endpoint {alias} is not a listed participant")
            continue
        if re.match(r"^(alt|loop|opt|par|critical|group)(?:\s|$)", line):
            stack.append(line.split()[0])
            continue
        if line == "else" or line.startswith("else "):
            if not stack or stack[-1] != "alt":
                errors.append(f"{prefix}: else is only supported inside alt")
            continue
        if line == "end":
            if stack:
                stack.pop()
            else:
                errors.append(f"{prefix}: unmatched end")
            continue
        if re.match(r"^note(?:\s|$)", line):
            in_note = ":" not in line
            continue
        activation = re.fullmatch(r"(?:activate|deactivate)\s+([A-Za-z][A-Za-z0-9_]*)", line)
        if activation:
            if activation.group(1) not in sequence["participants"]:
                errors.append(f"{prefix}: activation refers to unknown participant")
            continue
        if line in {"@startuml", "@enduml", "autonumber", "autonumber stop", "autonumber resume"} or line.startswith(("title ", "caption ")):
            continue
        errors.append(f"{prefix}: unsupported or unrecognized sequence syntax: {line[:90]}")
    if stack or in_note:
        errors.append(f"{prefix}: unclosed sequence group or note")
    if markup.splitlines().count("@startuml") != 1 or markup.splitlines().count("@enduml") != 1:
        errors.append(f"{prefix}: expected one @startuml and one @enduml")
    if len(sequence["participants"]) != len(set(sequence["participants"])):
        errors.append(f"{prefix}: duplicate participant IDs")
    if set(declared) != set(sequence["participants"]):
        errors.append(f"{prefix}: declared aliases differ from Participants")
    if not messages:
        errors.append(f"{prefix}: no recognized messages")
    sequence["message_count"] = messages


def validate_model(model, errors):
    warnings = []
    metadata = model["metadata"]
    for field in ["Format version", "System ID", "Title", "Document status", "Language", "Mode"]:
        if empty(metadata.get(field, "")):
            errors.append(f"Metadata: missing {field}")
    for field, allowed in [("Format version", {"1"}), ("Language", {"en"}), ("Document status", {"draft", "reviewed"}), ("Mode", {"logical", "technical"})]:
        if metadata.get(field) not in allowed:
            errors.append(f"Metadata: unsupported {field}: {metadata.get(field)!r}")
    if metadata.get("Default status") not in STATUSES:
        errors.append("Metadata: Default status must be Confirmed, Proposed or Open")
    seen = set()
    for collection in ["sources", "elements", "relationships", "views", "constraints", "open_questions", "sequences"]:
        for row in model[collection]:
            identity = row["id"]
            if not ID.fullmatch(identity):
                errors.append(f"{collection}: invalid ID {identity!r}")
            if identity in seen:
                errors.append(f"duplicate global ID {identity}")
            seen.add(identity)
            for key, value in row.items():
                if isinstance(value, str) and not value.strip():
                    errors.append(f"{identity}: empty {key}; use '-' for optional cells")
            if "status" in row and row["status"] not in STATUSES:
                errors.append(f"{identity}: invalid status {row['status']!r}")
    source_ids = {s["id"] for s in model["sources"]}
    for source in model["sources"]:
        if empty(source["reference"]) or empty(source["locator"]):
            errors.append(f"{source['id']}: missing reference or locator")
    for collection in ["elements", "relationships", "constraints", "sequences"]:
        for row in model[collection]:
            if not row["sources"]:
                errors.append(f"{row['id']}: missing source evidence")
            for source in row["sources"]:
                if source not in source_ids:
                    errors.append(f"{row['id']}: unknown source {source}")
    elements = {row["id"]: row for row in model["elements"]}
    relationships = {row["id"]: row for row in model["relationships"]}
    if not elements or not model["sources"]:
        errors.append("populate at least one source and one element")
    if not model["views"] and not model["sequences"]:
        errors.append("populate at least one view or sequence")
    system = elements.get(metadata.get("System ID"))
    if not system or system["type"] != "SoftwareSystem" or system["scope"] != "Internal":
        errors.append("System ID must reference an Internal SoftwareSystem")
    for element in model["elements"]:
        eid, kind, parent = element["id"], element["type"], element["parent"]
        if kind not in {"Person", "SoftwareSystem", "Container", "Component"}:
            errors.append(f"{eid}: invalid element Type {kind!r}")
        if element["scope"] not in {"Internal", "External", "Actor"}:
            errors.append(f"{eid}: invalid Scope")
        if kind == "Person" and (element["scope"] != "Actor" or element["shape"] != "Person"):
            errors.append(f"{eid}: a Person requires Actor scope and Person shape")
        if kind != "Person" and element["scope"] == "Actor":
            errors.append(f"{eid}: Actor scope requires Person type")
        if kind != "Person" and element["shape"] not in {"Rectangle", "Database"}:
            errors.append(f"{eid}: invalid shape for non-person")
        if element["shape"] == "Database" and kind != "Container":
            errors.append(f"{eid}: Database shape requires Container type")
        if empty(element["name"]) or empty(element["responsibility"]):
            errors.append(f"{eid}: missing name or responsibility")
        if kind in {"Person", "SoftwareSystem"} and not empty(parent):
            errors.append(f"{eid}: people/software systems must not have a Parent")
        if kind in {"Container", "Component"}:
            expected = "SoftwareSystem" if kind == "Container" else "Container"
            if parent not in elements or elements[parent]["type"] != expected:
                errors.append(f"{eid}: {kind} needs a {expected} parent")
            elif element["scope"] != elements[parent]["scope"]:
                errors.append(f"{eid}: ownership scope differs from parent")
        if metadata.get("Mode") == "technical" and kind in {"Container", "Component"} and empty(element["technology"]):
            warnings.append(f"{eid}: technology is undecided in technical mode")
    for relationship in model["relationships"]:
        for endpoint in ["source", "target"]:
            if relationship[endpoint] not in elements:
                errors.append(f"{relationship['id']}: unknown {endpoint} {relationship[endpoint]}")
        if empty(relationship["action"]):
            errors.append(f"{relationship['id']}: missing displayed action")
    for view in model["views"]:
        vid, level, focus = view["id"], view["level"], elements.get(view["focus"])
        if level not in {"C1", "C2", "C3"}:
            errors.append(f"{vid}: invalid Level")
        expected = "Container" if level == "C3" else "SoftwareSystem"
        if not focus or focus["type"] != expected or focus["scope"] != "Internal":
            errors.append(f"{vid}: focus must be an Internal {expected}")
        if empty(view["title"]):
            errors.append(f"{vid}: missing title")
        if not view["elements"]:
            errors.append(f"{vid}: no elements selected")
        for field in ["elements", "relationships"]:
            if len(view[field]) != len(set(view[field])):
                errors.append(f"{vid}: duplicate IDs in {field}")
        if level == "C1" and view["focus"] not in view["elements"]:
            errors.append(f"{vid}: C1 focus must be a visible element")
        if level in {"C2", "C3"} and view["focus"] in view["elements"]:
            errors.append(f"{vid}: focus is the boundary, not an inner element")
        for eid in view["elements"]:
            element = elements.get(eid)
            if not element:
                errors.append(f"{vid}: unknown element {eid}")
                continue
            kind = element["type"]
            if level == "C1" and kind not in {"Person", "SoftwareSystem"}:
                errors.append(f"{vid}: C1 cannot show {kind} {eid}")
            if level == "C2" and (kind == "Component" or (kind == "Container" and element["parent"] != view["focus"])):
                errors.append(f"{vid}: element {eid} is outside the C2 decomposition")
            if level == "C3" and kind == "Component" and element["parent"] != view["focus"]:
                errors.append(f"{vid}: component {eid} belongs to another container")
        for rid in view["relationships"]:
            relation = relationships.get(rid)
            if not relation:
                errors.append(f"{vid}: unknown relationship {rid}")
            elif relation["source"] not in view["elements"] or relation["target"] not in view["elements"]:
                errors.append(f"{vid}: endpoints of {rid} must both be visible")
    for question in model["open_questions"]:
        if empty(question["question"]):
            errors.append(f"{question['id']}: missing question")
        for affected in question["affects"]:
            if affected not in seen or affected in source_ids:
                errors.append(f"{question['id']}: unknown affected architecture ID {affected}")
    for sequence in model["sequences"]:
        for participant in sequence["participants"]:
            if participant not in elements:
                errors.append(f"{sequence['id']}: unknown participant {participant}")
        validate_sequence(sequence, elements, errors)
    open_count = sum(row.get("status") == "Open" for rows in model.values() if isinstance(rows, list) for row in rows)
    if open_count:
        warnings.append(f"{open_count} records have Open status; review before rendering affected views")
    return warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--json", action="store_true", help="Print the normalized model only if validation succeeds")
    args = parser.parse_args()
    try:
        text = args.markdown.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Cannot read Markdown: {error}", file=sys.stderr)
        return 2
    model, errors = parse_markdown(text)
    warnings = validate_model(model, errors)
    if errors:
        print("INVALID", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if args.json:
        print(json.dumps(model, ensure_ascii=False, indent=2))
    else:
        print(f"VALID: {len(model['elements'])} elements, {len(model['relationships'])} relationships, {len(model['views'])} C4 views, {len(model['sequences'])} sequences")
        print("Structural validation only; semantic and live Lucid checks remain required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

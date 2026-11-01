---
name: lucidchart-to-brief
description: Extract a concise factual architecture input brief from a supplied Lucidchart business diagram, export, screenshot or equivalent process diagram, using a short interview to resolve ambiguity.
---
# Lucidchart to Brief

Produce an English Markdown brief for architecture-design or independent use. Preserve business meaning; do not redesign the system.

1. Obtain the diagram through an available authorized connector, or use a supplied PDF/image/export/text. Do not claim access to an unread Lucidchart URL. Ask for an accessible export if blocked.
2. Inspect readable labels, boundaries, actors, blocks and arrows. Preserve source names and direction. Separate observations from interpretations; mark unreadable labels, ambiguous connectors and missing legends. Do not treat proximity as a relationship.
3. Draft the first brief early. Ask at most 3–4 related questions that materially affect interpretation. Reuse answers and do not invent business scenarios, components, APIs or technologies.
4. Update only affected sections after answers. Keep unresolved ambiguities visible.
5. Save the brief at an agreed project path, plus `interview/brief-state.md` after meaningful steps: source/version, resolved questions, open questions, brief path and next action. Read this checkpoint first on resume.
6. Hand off the brief path to architecture-design when requested; do not automatically run the full design workflow.

Use these brief sections only when useful:
- Source and scope.
- Actors and external systems.
- Observed activities, boundaries and directed interactions (stable IDs when useful).
- Logical information exchanged, where observable.
- Validated interpretations and constraints.
- Uncertainties and questions for architecture design.

Cite diagram page/region or element labels for important observations. Keep inferred details explicitly provisional.
Stay in the current agent for small tasks. For a large extraction, use architecture-extract if installed, giving exact inputs and a bounded output. Retain architect review for uncertain meaning.
If the architecture-design delegation reference is available, read it only when needed; otherwise use a compact handoff containing findings, evidence, assumptions, unresolved questions and next action. Checkpoint before a fresh worker or coordinator. Never assume exact context monitoring or automatic agent restart.

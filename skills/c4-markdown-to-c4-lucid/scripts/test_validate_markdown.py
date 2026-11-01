#!/usr/bin/env python3
"""Local behavioral checks; no network or Lucid side effects."""
import copy
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_markdown import parse_markdown, validate_model


ASSETS = Path(__file__).resolve().parent.parent / 'assets'
COMPACT = '''# Example
## Metadata
| Field | Value |
|---|---|
| System ID | system |
| Title | Example |
| Default sources | source |
## Sources
| ID | Reference | Locator |
|---|---|---|
| source | Interview | Scope |
## Elements
| ID | Name | Type | Parent | Scope | Responsibility | Shape |
|---|---|---|---|---|---|---|
| user | User | Person | - | Actor | Submit tasks | Person |
| system | Example | SoftwareSystem | - | Internal | Process tasks | Rectangle |
## Relationships
| ID | Source | Target | Action |
|---|---|---|---|
| rel_submit | user | system | Submit tasks |
## Views
| ID | Level | Title | Focus | Elements | Relationships |
|---|---|---|---|---|---|
| c1 | C1 | Context | system | user, system | rel_submit |
## Constraints
| ID | Rule |
|---|---|
## Open questions
| ID | Question | Affects |
|---|---|---|
'''


def checked(text):
    model, errors = parse_markdown(text)
    warnings = validate_model(model, errors)
    return model, errors, warnings


class MarkdownTests(unittest.TestCase):
    def test_completed_example(self):
        model, errors, _ = checked((ASSETS / 'domain-tasks-example.md').read_text())
        self.assertEqual(errors, [])
        self.assertEqual(len(model['views']), 3)
        self.assertEqual(model['sequences'][0]['message_count'], 61)

    def test_blank_template_is_incomplete(self):
        _, errors, _ = checked((ASSETS / 'architecture-template.md').read_text())
        self.assertTrue(errors)

    def test_compact_defaults(self):
        model, errors, _ = checked(COMPACT)
        self.assertEqual(errors, [])
        self.assertEqual(model['metadata']['Mode'], 'logical')
        self.assertEqual(model['elements'][0]['status'], 'Proposed')
        self.assertEqual(model['elements'][0]['sources'], ['source'])
        self.assertEqual(model['elements'][0]['technology'], '-')

    def test_dangling_endpoint(self):
        _, errors, _ = checked(COMPACT.replace('| rel_submit | user | system |', '| rel_submit | user | missing |'))
        self.assertTrue(any('unknown target' in error for error in errors))

    def test_hidden_endpoint(self):
        _, errors, _ = checked(COMPACT.replace('| user, system | rel_submit |', '| system | rel_submit |'))
        self.assertTrue(any('both be visible' in error for error in errors))

    def test_duplicate_id(self):
        _, errors, _ = checked(COMPACT.replace('| rel_submit | user | system |', '| system | user | system |'))
        self.assertTrue(any('duplicate global ID' in error for error in errors))

    def test_unknown_evidence(self):
        _, errors, _ = checked(COMPACT.replace('| Default sources | source |', '| Default sources | missing_source |'))
        self.assertTrue(any('unknown source' in error for error in errors))

    def test_level_and_parent_validation(self):
        _, errors, _ = checked(COMPACT.replace('| user | User | Person | - | Actor | Submit tasks | Person |', '| user | Worker | Component | missing_parent | Internal | Process tasks | Rectangle |'))
        self.assertTrue(any('needs a Container parent' in error for error in errors))
        self.assertTrue(any('C1 cannot show Component' in error for error in errors))

    def test_literal_pipe_and_line_break(self):
        model, errors, _ = checked(COMPACT.replace('Submit tasks | Person', 'Submit \\| inspect<br>tasks | Person'))
        self.assertEqual(errors, [])
        self.assertEqual(model['elements'][0]['responsibility'], 'Submit | inspect<br>tasks')

    def test_extra_cell_rejected(self):
        _, errors, _ = checked(COMPACT.replace('| rel_submit | user | system | Submit tasks |', '| rel_submit | user | system | Submit tasks | extra |'))
        self.assertTrue(any('cells; expected' in error for error in errors))

    def test_explicit_status_overrides_default(self):
        text = COMPACT.replace('| ID | Name | Type | Parent | Scope | Responsibility | Shape |', '| ID | Name | Type | Parent | Scope | Responsibility | Shape | Status |')
        text = text.replace('|---|---|---|---|---|---|---|', '|---|---|---|---|---|---|---|---|')
        text = text.replace('| Submit tasks | Person |', '| Submit tasks | Person | Confirmed |')
        text = text.replace('| Process tasks | Rectangle |', '| Process tasks | Rectangle | Proposed |')
        model, errors, _ = checked(text)
        self.assertEqual(errors, [])
        self.assertEqual(model['elements'][0]['status'], 'Confirmed')

    def test_unknown_sequence_participant_rejected(self):
        model, errors = parse_markdown((ASSETS / 'domain-tasks-example.md').read_text())
        model['sequences'][0]['markup'] += '\nunknown -> ui : Extra message'
        validate_model(model, errors)
        self.assertTrue(any('not a listed participant' in error for error in errors))

    def test_unbalanced_sequence_rejected(self):
        model, errors = parse_markdown((ASSETS / 'domain-tasks-example.md').read_text())
        model['sequences'][0]['markup'] = model['sequences'][0]['markup'].replace('alt Permission denied', 'Permission denied', 1)
        validate_model(model, errors)
        self.assertTrue(errors)

    def test_preprocessor_rejected(self):
        model, errors = parse_markdown((ASSETS / 'domain-tasks-example.md').read_text())
        model['sequences'][0]['markup'] += '\n!include unsafe.puml'
        validate_model(model, errors)
        self.assertTrue(any('unsupported or unrecognized' in error for error in errors))

    def test_cli_json_and_missing_file(self):
        script = Path(__file__).with_name('validate_markdown.py')
        result = subprocess.run([sys.executable, str(script), str(ASSETS / 'domain-tasks-example.md'), '--json'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        import json
        self.assertEqual(json.loads(result.stdout)['metadata']['System ID'], 'system')
        result = subprocess.run([sys.executable, str(script), str(ASSETS / 'nonexistent.md')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

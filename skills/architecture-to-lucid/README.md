# Architecture to Lucid

A compact Claude Code skill for **shared canonical Architecture Markdown v1 → editable Lucid C4 and sequence diagrams**, with one-time normalization for external documentation. Conversations can be in French; all professional artifacts are in English.

## Install in Claude Code

Clone the repository if needed:

```bash
git clone https://github.com/laurentcharbonnel/architecture-skills.git
cd architecture-skills
mkdir -p ~/.claude/skills
cp -R skills/architecture-to-lucid ~/.claude/skills/
```

Run the copy from the repository root. Compare or back up an existing destination first. For project-only installation, copy the folder into the project's `.claude/skills/` instead. To update, run `git pull --ff-only` in the clone and repeat the copy after reviewing local changes. [Claude Code skills](https://code.claude.com/docs/en/skills).

## Prerequisites

Configure the Lucid MCP once in Claude Code:

```bash
claude mcp add --transport http lucid https://mcp.lucid.app/mcp
```

Then run `/mcp` in Claude Code and authorize Lucid. Team/Enterprise accounts require administrator enablement of MCP access; your AI tool administrator may also need to authorize the integration. Reuse an existing authorized connection rather than adding a duplicate. [Official Lucid setup](https://help.lucid.co/hc/en-us/articles/42578801807508-Integrate-Lucid-with-AI-tools-using-the-Lucid-MCP-server).

No credentials are bundled, and the skill does not configure or authenticate an account automatically.

## Use it

### 1. Normalize an external document

```text
/architecture-to-lucid Normalize docs/external-spec.md into docs/architecture-model.md using the bundled template. Preserve source references, mark inferred structure Proposed and list missing information. Do not create Lucid documents yet.
```

You can also copy [architecture-model-template.md](assets/architecture-model-template.md) and fill it yourself. The completed [domain-tasks-example.md](assets/domain-tasks-example.md) demonstrates C1, C2, a proposed logical C3 and a sequence with failure/retry branches.

### 2. Create Lucid from the Markdown

```text
/architecture-to-lucid Create the C1 and C2 views from docs/architecture-model.md in Lucid. Apply the convention, verify actual readback and visual output, and save the links and fidelity report.
```

Request C3 and sequence sections when needed. Missing details stay explicit; logical views need not select a stack. Lucid creation/update is strictly on-demand: only an explicit architect request authorizes the selected C1/C2/C3 views or sequences. Never call the connector automatically during interviews, checkpoints or artifact synchronization. Reuse canonical Markdown without restarting the interview; prefer targeted updates to existing diagrams when the MCP supports them. Mermaid remains the default lightweight rendering in `design-doc.md`. Normalization, validation and generic preview requests do not authorize Lucid generation.

### 3. Review a manual change

```text
/architecture-to-lucid Compare the saved architecture-model.md and Lucid mapping with the current diagrams. Report changes, then update the Markdown to reflect my edits.
```

## Resources and output

The [Markdown schema](references/markdown-format.md) defines the canonical tables, sequence PlantUML and defaults shared with architecture-design. Reuse HLD/LLD models from architecture-design’s New Design or Existing Design modes directly, with their stable IDs and owning paths/revisions; validate each independently and reconcile HLD context references as the schema describes; no separate normalization, inventory or sequence model. Mermaid previews and extracted JSON are derived outputs. The [Lucid workflow](references/lucid-workflow.md) defines creation, mappings and fidelity checks. Save the canonical Markdown, mapping and fidelity report in the project. Read the completed example only when useful.

## Token efficiency

- Detailed references load by operation; the entry point only routes the work.
- Element definitions are shared across views, with stable ID lists for each view.
- Optional columns and document defaults avoid repeated status/source/technology cells.
- Validation runs as a Python script; its code and the long example need not enter model context.
- Readback is reduced to differences/counts; unchanged views are reused.

Token savings depend on the source and tool responses; this is not a fixed token-count guarantee.

## Validation and limits

Python 3.9+; standard library only. From the repository root:

```bash
python3 skills/architecture-to-lucid/scripts/validate_markdown.py skills/architecture-to-lucid/assets/domain-tasks-example.md
python3 skills/architecture-to-lucid/scripts/validate_markdown.py docs/architecture-model.md --json > docs/architecture-model.json
python3 skills/architecture-to-lucid/scripts/test_validate_markdown.py
```

See [recorded validation results](VALIDATION.md). The blank template intentionally fails until populated. The helper checks structural consistency, not business correctness or Lucid renderability. Native sequence source must be read back because generic fetch was observed to omit actor/database interactions. Fidelity is assessed separately from visual quality.

## Integration

Keep the existing architecture-design skill responsible for the interview, High-Level Design and Low-Level Design. Use this complementary skill to consume its canonical Markdown directly, publish selected views, and verify diagrams. The interview needs this folder installed alongside architecture-design for its shared schema/template/validator, but no Lucid connection until publication. Normalization is only needed for other input formats. Semantic edits update Markdown first; Lucid refreshes require an explicit architect request; there is no automatic synchronization or change to shared standards.

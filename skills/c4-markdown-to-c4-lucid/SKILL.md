---
name: c4-markdown-to-c4-lucid
description: Normalize architecture documentation into compact Markdown and create matching editable Lucid C1, C2, C3 and sequence diagrams. Use for Markdown-to-Lucid conversion and fidelity checks.
---

# C4 Markdown to C4 Lucid

Converse in the user's language; write artifacts and diagram labels in English. Complement the architecture-design interview rather than repeating it.

## Load only the selected workflow

- **Existing canonical Markdown (including architecture-design output):** reuse each owning path and its IDs directly (HLD C1/C2; LLD C3/sequences); validate each supplied model without re-normalizing or creating a parallel canonical file. Apply the shared schema’s context-reference rule when both levels exist.
- **Normalize other documentation:** use [assets/architecture-template.md](assets/architecture-template.md) and [references/markdown-format.md](references/markdown-format.md). Save traceable Markdown; publishing requires a creation request.
- **Create Lucid:** validate the Markdown, then read [references/lucid-workflow.md](references/lucid-workflow.md). A clear creation request is sufficient authorization; respect actual tool access controls.
- **Review edits/fidelity:** use the saved mapping and workflow reference. Integrate edits into Markdown when requested; otherwise propose a diff.

Load [assets/domain-tasks-example.md](assets/domain-tasks-example.md) only when an example is useful. Do not load all references, examples or script code by default.

## Canonical source

Use exactly [Architecture Markdown v1](references/markdown-format.md), shared with architecture-design. Each record has one owning model; necessary context rows follow the schema’s reference rule. Sequences use PlantUML sections once in their owning file. Track each selected view/sequence’s source path and revision. Do not derive Lucid from interview Mermaid or introduce a competing canonical model. Normalization is only for input not already in this schema. Stable IDs survive renames. Distinguish Confirmed facts, Proposed design and Open decisions. Do not invent technologies, boundaries or behavior. Apply existing project standards without changing them during conversion.

Run the helper, resolving its path from this skill:
```bash
python3 scripts/validate_markdown.py architecture.md
python3 scripts/validate_markdown.py architecture.md --json > architecture-model.json
```
Python 3.9+, no dependencies/network. The JSON is a disposable extraction for rendering, never a second source or an input edited independently. Keep the original Markdown path/revision in the rendering mapping. If Python is unavailable, validate manually and disclose the limitation.

## Rendering and verification

Internal elements: blue; external systems: gray; people: blue silhouettes; stores: cylinders. Show name, [type], responsibility, and technology/deployment when known. C1 focuses a system; C2 its containers; C3 one container's components. Use the proper boundary. Blue denotes ownership even outside the current C3 frame. C2 labels are short English actions, normally 2–3 words; keep details in Markdown.

Read actual Lucid content back; compare names, descriptions, boundaries, directions and sequence semantics. Inspect exports separately. Generic sequence fetch omitted actor/database messages in the workshop: use native generator markup. Import success alone is not fidelity proof.

## Token budget and persistence

Render requested views only. Reuse context and mappings; update changed sections. Process bulky readbacks locally and return counts/differences, not whole documents. Never skip source content needed for correctness or resources mandated by live tools to save tokens.

Save Markdown, mapping and a concise fidelity report. Check a timed-out creation before retrying to avoid duplicates. Repair the same document for at most three passes, then disclose remaining defects. Preserve collaborator edits and unresolved checks.

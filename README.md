# Architecture Skills

Reusable Claude Code skills for architecture work. Keep reusable methods, generic design patterns and artifact templates here; project specifications stay in their own repositories. Enterprise standards and platform catalogs belong in a separate, authorized enterprise repository.

## Skills

| Skill | Purpose |
| --- | --- |
| [architecture-design](skills/architecture-design/README.md) | Guide architecture interviews through structure, sequences, contracts and implementation handoff. |
| [lucid-to-brief](skills/lucid-to-brief/README.md) | Extract a factual architecture input brief from a Lucidchart diagram or supplied export. |
| [c4-markdown-to-c4-lucid](skills/c4-markdown-to-c4-lucid/README.md) | Consume shared canonical C4 Markdown (normalize other inputs once) and create matching editable Lucid diagrams. |

Each skill's README contains its installation, prerequisites, examples, resources and validation limits. Copy whole skill folders to preserve resources. Install architecture-design alongside c4-markdown-to-c4-lucid: it reuses that sibling's schema, template and validator; the interview itself needs no Lucid connection.

## Shared canonical architecture

`architecture-design` maintains one project Markdown file using the existing [Architecture Markdown v1 schema](skills/c4-markdown-to-c4-lucid/references/markdown-format.md) and [template](skills/c4-markdown-to-c4-lucid/assets/architecture-template.md). It derives Mermaid during the interview; `c4-markdown-to-c4-lucid` consumes the same file to render selected Lucid views/sequences. Elements, relationships and sequence PlantUML are defined once. Rendering JSON, mapping files and diagrams are derived outputs. Semantic edits return to Markdown before regeneration; there is no background synchronization.

C1/C2 commentary and team review remain in `high-level-design/`; C3, detailed scenario commentary, contracts and implementation guidance remain in `low-level-design/`. They reference canonical IDs. Checkpoints retain the canonical path/revision, current IDs and pending work so resuming does not require loading every artifact.

## Shared principles

- Keep the architect responsible for decisions; distinguish confirmed facts, proposals and open questions.
- Preserve source evidence and approved enterprise standards. Change enterprise standards only with explicit approval.
- Write professional artifacts in English; converse in the user's preferred language.
- Keep entry points concise. Load references, templates and examples only for the current operation.
- Reuse resolved answers and checkpoints. Update affected artifacts rather than regenerating entire specifications.
- Keep project artifacts, company information, credentials and internal diagrams out of this public repository.
- Use bounded delegation only when useful; retain human review of uncertain meaning and design choices.

## Repository conventions

`SKILL.md` contains runtime instructions. `README.md` explains installation and use to people. `references/` holds detailed operational guidance; `assets/` holds reusable templates and examples; `scripts/` holds deterministic helpers when needed.

Before publishing, check frontmatter, names, local links and resource paths, then run relevant helpers. Structural checks do not establish Claude Code behavior, live MCP access or measured token savings. Keep these limits explicit.

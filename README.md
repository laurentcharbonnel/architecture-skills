# Architecture Skills

Reusable Claude Code skills for architecture work. Keep reusable methods, generic design patterns and artifact templates here; project specifications stay in their own repositories. Enterprise standards and platform catalogs belong in a separate, authorized enterprise repository.

## Skills

| Skill | Purpose |
| --- | --- |
| [architecture-design](skills/architecture-design/README.md) | Guide architecture interviews through structure, sequences, contracts and implementation handoff. |
| [lucid-to-brief](skills/lucid-to-brief/README.md) | Extract a factual architecture input brief from a Lucidchart diagram or supplied export. |
| [c4-markdown-to-c4-lucid](skills/c4-markdown-to-c4-lucid/README.md) | Normalize documentation into canonical C4 Markdown and create matching editable Lucid diagrams. |

Each skill's README contains its installation, prerequisites, examples, resources and validation limits. Copy the whole skill folder to preserve its bundled resources.

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

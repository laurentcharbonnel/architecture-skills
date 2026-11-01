# Architecture Skills

Reusable skills for architecture work and rapid prototyping with Claude Code and Codex. Keep reusable methods, generic design patterns and artifact templates here; project specifications stay in their own repositories. Enterprise standards and platform catalogs belong in a separate, authorized enterprise repository.

## Skills

| Skill | Purpose |
| --- | --- |
| [architecture-design](skills/architecture-design/README.md) | Start a New Design interview or reuse existing documentation with Existing Design, through structure, sequences, contracts and implementation handoff. |
| [lucid-to-brief](skills/lucid-to-brief/README.md) | Extract a factual architecture input brief from a Lucidchart diagram or supplied export. |
| [architecture-to-lucid](skills/architecture-to-lucid/README.md) | Consume shared canonical Architecture Markdown (normalize other inputs once) and create matching editable Lucid C1/C2/C3 and sequence diagrams. |
| [rapid-prototype](skills/rapid-prototype/SKILL.md) | Quickly test a technical hypothesis or explore an interface, user flow, or simulation with a minimal interactive prototype. |

The architecture skills' READMEs cover installation, prerequisites, examples, resources and validation limits. Copy whole skill folders to preserve resources. Install architecture-design alongside architecture-to-lucid: it reuses that sibling's schema, template and validator; the interview itself needs no Lucid connection.

Use **Existing Design** when a topic is already documented: bounded source intake, a short gap analysis, then C1/C2 validation before deeper artifacts. Original sources stay in place; facts, inferences and gaps remain explicit. See the [usage example](skills/architecture-design/README.md#2-existing-design--reuse-architecture-already-documented).

## Rapid prototyping

`rapid-prototype` is independent of `architecture-design` and needs no sibling skill. Both modes follow **Idea → Minimal Scope → Build → Test → Decide**, with minimal reading, dependencies, files and token use. It stops when the hypothesis is sufficiently tested and reports limitations and optional next steps.

Copy `skills/rapid-prototype/` into your tool's skill directory (for example, `.claude/skills/` for Claude Code or `.agents/skills/` for Codex). Its single `SKILL.md` contains the complete instructions.

Examples in Claude Code:

```text
/rapid-prototype Technical POC: In this repository, check whether the existing CSV parser handles quoted multiline fields. Add the smallest runnable example and one focused test.

/rapid-prototype Visual Prototype: From scratch, explore a two-step appointment booking flow with local sample data in a minimal interactive prototype.
```

In Codex, use `$rapid-prototype` with the same mode and request. Either mode can start from scratch or use an existing repository. Only a prototype/code and a brief README or test result, when useful, are expected; production architecture is outside this workflow.

## Shared canonical architecture

`architecture-design` maintains `high-level-design/architecture-model.md` (C1/C2) and `low-level-design/architecture-model.md` (C3 and detailed sequences) using the same existing [Architecture Markdown v1 schema](skills/architecture-to-lucid/references/markdown-format.md) and [template](skills/architecture-to-lucid/assets/architecture-model-template.md). Mermaid is the default lightweight rendering in `design-doc.md`; `architecture-to-lucid` consumes each owning file directly only on an explicit architect request to create or update selected Lucid views/sequences. Never call the Lucid connector automatically during interviews, checkpoints or artifact synchronization; prefer targeted updates to existing diagrams when the MCP supports them. Each record has one owning model; minimal HLD context needed in LLD is referenced as described in the shared schema. Sequence PlantUML is defined once, with no separate `sequences/` artifact. Rendering JSON, mapping files and diagrams are derived outputs. Semantic edits return to Markdown before regeneration; there is no background synchronization.

Short human `design-doc.md` documents explain C1/C2 and C3/interactions at their respective design levels; lightweight HLD `review.md` captures feedback and open decisions. Structured `architecture-model.md` models support agents and diagram generation. Optional `components/`, machine-readable `contracts/` and `orchestrators/` add only useful implementation detail under LLD. Minimal ADRs live in `decisions/`; `interview/state.md` retains both model paths/revisions, IDs and pending work.

## Shared principles

- Keep the architect responsible for decisions; distinguish confirmed facts, proposals and open questions.
- Preserve source evidence and approved enterprise standards. Change enterprise standards only with explicit approval.
- Write professional artifacts in English; converse in the user's preferred language.
- Keep entry points concise. Load references, templates and examples only for the current operation.
- Reuse resolved answers and checkpoints. Update affected artifacts rather than regenerating entire specifications.
- Keep project artifacts, company information, credentials and internal diagrams out of this public repository.
- Use bounded delegation only when useful; retain human review of uncertain meaning and design choices.

## Repository conventions

`SKILL.md` contains runtime instructions. `README.md`, when needed, explains installation and use to people. `references/` holds detailed operational guidance; `assets/` holds reusable templates and examples; `scripts/` holds deterministic helpers when needed.

Before publishing, check frontmatter, names, local links and resource paths, then run relevant helpers. Structural checks do not establish Claude Code behavior, live MCP access or measured token savings. Keep these limits explicit.

# Phase guidance

Read only the section needed for the current phase. Keep outputs in the project specifications repository, following the project output structure below.

## Existing Design intake

Use when the chosen topic already has architecture documentation but needs artifacts in the validated output structure below. New Design uses the same phases with an interview to discover the design.

- Read `interview/state.md` first when present. Bound intake to the selected topic: inspect its relevant files and follow only necessary links; do not scan the whole repository. Extract and reuse existing components, relationships, decisions, sequences and contracts with file/section locators. Do not redesign or invent missing details.
- Keep three evidence categories in the existing format: documented facts with Sources (Confirmed only when supported), inferences to validate (Proposed with rationale/source), and gaps or conflicting sources (Open records/questions with affected IDs). Documented proposals remain Proposed; documentation alone does not make a choice approved. Do not silently reconcile contradictions.
- Present a short gap analysis: what can be reused, what needs normalization, and what blocks the requested artifacts. Keep it in the response and persist actionable gaps in canonical Open questions and the checkpoint; no new report file. Reuse resolved answers, skip the full interview, and ask at most 3–4 targeted intake questions, only for blocking gaps. Leave nonblocking gaps explicit; if a blocker remains, checkpoint it instead of inventing an answer.
- Record the mapping from source locators to useful outputs/IDs in the checkpoint, using the agreed output structure. Preserve all source files in place without moving or rewriting them. Reuse conforming canonical models directly; normalize nonconforming sources once into the owning model. If an output path collides with a source, agree a non-destructive mapping before writing. Original documents remain evidence, not a second actively maintained canonical model.
- Start with supported C1/C2 in `high-level-design/architecture.md` and its short derived `overview.md`. Check schema and source fidelity, then obtain architect validation at the checkpoint before proceeding to C3, sequences, contracts and implementation detail. Offer team review and create `review.md` only when review is performed. If the architect explicitly chooses provisional continuation, retain unresolved decisions and their downstream risks; do not imply validation.
- Continue Structure → Sequence → Contracts → Implementation using the sections below. Reuse documented scenarios and interface schemas when their phase is reached; link untouched contracts or copy only needed schemas into generated outputs with provenance. Create LLD overview/model and optional components/contracts/orchestrators only when useful. Generate code only by separate request. Update affected canonical records incrementally and synchronize dependent context rows, human overviews and derived Mermaid at validated checkpoints as described in [canonical-rendering.md](canonical-rendering.md). Only on an explicit Lucid creation/update request, hand the same canonical paths/revisions and requested diagram IDs to architecture-to-lucid; no second normalization.

## Project output structure

Use this structure in the project specifications repository. Both `architecture.md` files use the shared [Architecture Markdown v1 schema](../../architecture-to-lucid/references/markdown-format.md) and [template](../../architecture-to-lucid/assets/architecture-template.md); create each only when its design level is needed:
```text
high-level-design/
  overview.md
  architecture.md
  review.md
low-level-design/
  overview.md
  architecture.md
  components/       # optional component specifications
  contracts/        # optional OpenAPI / event schemas
  orchestrators/    # optional state and transition specifications
decisions/          # minimal ADRs when a tradeoff needs traceability
interview/
  state.md
```

- `high-level-design/overview.md`: short human explanation of goals, boundaries, C1/C2 diagrams and main information flows. Link the canonical view IDs and explain what each useful derived diagram shows.
- `high-level-design/architecture.md`: canonical C1/C2 elements, relationships and views. Any useful high-level sequence belongs here once.
- `high-level-design/review.md`: lightweight team feedback, unresolved decisions and resulting actions. Link model questions and ADRs instead of restating the design. Create it when review is useful.
- `low-level-design/overview.md`: short human explanation of C3 and important interactions, with derived diagrams, canonical IDs and links to useful implementation details.
- `low-level-design/architecture.md`: canonical C3 structure and detailed sequences, using the same tables and PlantUML sections as HLD. Follow the shared schema’s context-reference rule for HLD elements needed by C3; there is no new schema or import syntax.
- `low-level-design/components/<component>.md`: only additional implementation specifications that do not fit in the short overview; no repeated C3 inventory or sequence definition.
- `low-level-design/contracts/`: machine-readable OpenAPI and event schemas, created for actual interfaces. Link them from canonical relationship Details and relevant specifications; do not repeat schemas in prose.
- `low-level-design/orchestrators/<orchestrator>.md`: states, transitions and behavior only when relevant; link canonical interactions instead of redefining them.
- `decisions/`: minimal ADRs, identifying their design level. `interview/state.md`: checkpoint with both model paths/revisions, selected IDs and next action.

Do not create a `sequences/` directory or scenario documents: each sequence is defined once in its owning structured model. Explain scenarios in the appropriate overview, using derived previews. Overviews, reviews and specifications are not alternative architecture definitions.
Create files only when useful; do not generate empty placeholders, speculative contracts or a component/orchestrator file for every element. Offer team review after C1/C2, before detailing C3; provisional continuation remains allowed.
For existing projects, follow the non-destructive source-to-output mapping above. Normalize sequences into their owning canonical model with provenance; keep original source documents and links intact, and do not maintain another canonical copy.

## Structure
Identify goals, actors, scope, constraints and system boundaries (C1); deployable/runnable containers, responsibilities and connections (C2); logical components and ownership (C3).
At C2, capture what information moves and where it originates without prematurely defining fields. Offer a short team review: choices, tradeoffs, risks, open decisions. Review status: draft, in-review, reviewed; never a mandatory gate.
Update canonical Elements, Relationships and Views first; reference C1/C2 views from high-level-design/overview.md and C3 views from low-level-design/overview.md. Derive only the useful affected Mermaid views with [canonical-rendering.md](canonical-rendering.md). For Existing Design, validate C1/C2 with the architect before detailing C3; preserve source artifacts and reuse already conforming Markdown unchanged.

Use the [HLD overview](../assets/templates/high-level-overview.md), [LLD overview](../assets/templates/low-level-overview.md), optional [component](../assets/templates/component.md) and [review](../assets/templates/review.md) templates when creating those artifacts.

## Sequence
In New Design, choose a concrete scenario with the architect. In Existing Design, reuse a documented scenario; ask only when a blocking gap requires it. Do not assume business scenarios exist. Include actors, receiving components, sync/async calls, correlation, retries and failure paths when relevant. Store each scenario once as a `## Sequence: seq_id` section in the owning canonical model, with the existing Field/Value metadata and PlantUML block. Use global element IDs as participant aliases and their Names as display names. Preserve ordering, sync/async and return semantics, branches, retries and failures. Derive Mermaid from this source for discussion; never author a second sequence in another artifact. Keep high-level or low-level scenario commentary at the appropriate design level.

Use the shared canonical template’s sequence guidance and the appropriate overview template for commentary. Skip diagrams for trivial interactions.

## Contracts
Identify the receiver/owner of every interface. Link each contract to its interaction; avoid repeating schemas in prose. Specify request/response or event schemas, validation, errors, authentication/authorization, idempotency, versioning and delivery semantics as relevant.
Use OpenAPI for HTTP contracts and an appropriate machine-readable event schema for messages. Keep undecided fields explicit; check syntax and available schema tooling before calling a contract valid.
Prefer approved project standards: REST Python, OAuth, enterprise messaging bus, or orchestrator templates only when supplied/approved for this project. Do not invent enterprise details or treat these examples as universal defaults.

Use the [OpenAPI skeleton](../assets/templates/contract.yaml) for HTTP only. Derive contracts after the relevant C3 structure and interactions; an early contract sketch is allowed when needed to decide, marked provisional.

## Implementation
Separate orchestration from resource creation when the accepted design requires it. Specify an orchestrator as states, transitions, triggers, failures, recovery and completion criteria.
Provide component responsibilities, contract links, dependencies, implementation constraints and verifiable acceptance criteria. Keep implementation repositories separate when project policy requires it.
For a changed upstream decision, update canonical records first, then affected sequences/contracts/specifications and derived previews only. Keep stable IDs across renames; carry the new Name into canonical participant declarations and regenerate affected Mermaid at the existing synchronization points. Record pending Lucid refreshes in the checkpoint without calling the connector; Lucid creation/update requires an explicit architect request for the selected diagrams, as described in [canonical-rendering.md](canonical-rendering.md#lucid-handoff-and-edits).

Use the [component](../assets/templates/component.md) and [orchestrator](../assets/templates/orchestrator.md) templates. Generate code only if separately requested.

## Minimal decision record
Use: ID/title; status (proposed/accepted/superseded); context; choice; consequence; source/standard links.
Use the [decision template](../assets/templates/decision.md). Do not create records for routine restatements.

## Reusable standards intake
Capture source, scope, applicability, rule, exceptions and approval status. Compare existing standards; show conflicts and request approval before changing the library. Apply approved standards by ID/path without copying them into every artifact.

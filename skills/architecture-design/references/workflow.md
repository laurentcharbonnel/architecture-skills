# Phase guidance

Read only the section needed for the current phase. Keep outputs in the project specifications repository, following the project output structure below.

## Project output structure

Use this structure in the project specifications repository. `architecture.md` follows the shared [Architecture Markdown v1 schema](../../c4-markdown-to-c4-lucid/references/markdown-format.md) and is the only source of elements, relationships, views and sequence markup:
```text
architecture.md
high-level-design/
  overview.md
  review.md
low-level-design/
  components/
  sequences/
  contracts/
  orchestrators/
decisions/
interview/
  state.md
```

Keep C1/C2 view IDs and main logical information-flow commentary in `high-level-design/overview.md`, and team review feedback/status in `high-level-design/review.md`.
Keep C3 view IDs and implementation specifications in `low-level-design/components/<component>.md`; detailed scenario commentary and canonical sequence IDs in `low-level-design/sequences/<scenario>.md`; OpenAPI and other schemas in `low-level-design/contracts/`; state machines and behavior in `low-level-design/orchestrators/<orchestrator>.md`.
These documents link to canonical IDs/sections and may embed derived Mermaid previews; they do not redefine elements, relationships or sequence messages. C1/C2 remain high level design, C3 and detailed implementation behavior remain low level design even though their canonical records share one file. Keep that grouping in the overview/component/scenario links, without adding schema fields. Contracts and state-machine details supplement canonical interactions; link contracts from relationship Details when relevant.
Put minimal ADRs in `decisions/`, recording whether each concerns high level design or low level design. Keep progress in `interview/state.md`.
Create files only when useful; do not generate empty placeholder documents or directories. Offer team review after C1/C2, before detailing C3; provisional continuation remains allowed.
For existing projects, map the current artifacts to this structure and propose a targeted migration; do not silently move files or create parallel duplicate specifications. Record the agreed mapping in the checkpoint.

## Structure
Identify goals, actors, scope, constraints and system boundaries (C1); deployable/runnable containers, responsibilities and connections (C2); logical components and ownership (C3).
At C2, capture what information moves and where it originates without prematurely defining fields. Offer a short team review: choices, tradeoffs, risks, open decisions. Review status: draft, in-review, reviewed; never a mandatory gate.
Update canonical Elements, Relationships and Views first; reference C1/C2 views from high-level-design/overview.md and C3 views from low-level-design/components/. Derive only the useful affected Mermaid views with [canonical-rendering.md](canonical-rendering.md). For existing projects, agree the mapping or migration before moving artifacts; reuse already conforming Markdown unchanged.

Use the [overview](../assets/templates/high-level-overview.md), [component](../assets/templates/component.md) and [review](../assets/templates/review.md) templates when creating those artifacts.

## Sequence
Choose a concrete scenario with the architect; do not assume business scenarios exist. Include actors, receiving components, sync/async calls, correlation, retries and failure paths when relevant. Store each scenario once as a `## Sequence: seq_id` section in the canonical Markdown, with the existing Field/Value metadata and PlantUML block. Use global element IDs as participant aliases and their Names as display names. Preserve ordering, sync/async and return semantics, branches, retries and failures. Derive Mermaid from this source for discussion; never author a second sequence in the flow document. Keep high-level or low-level scenario commentary at the appropriate design level.

Use the [flow template](../assets/templates/flow.md). Skip diagrams for trivial interactions.

## Contracts
Identify the receiver/owner of every interface. Link each contract to its interaction; avoid repeating schemas in prose. Specify request/response or event schemas, validation, errors, authentication/authorization, idempotency, versioning and delivery semantics as relevant.
Use OpenAPI for HTTP contracts and an appropriate machine-readable event schema for messages. Keep undecided fields explicit; check syntax and available schema tooling before calling a contract valid.
Prefer approved project standards: REST Python, OAuth, enterprise messaging bus, or orchestrator templates only when supplied/approved for this project. Do not invent enterprise details or treat these examples as universal defaults.

Use the [OpenAPI skeleton](../assets/templates/contract.yaml) for HTTP only. Derive contracts after the relevant C3 structure and interactions; an early contract sketch is allowed when needed to decide, marked provisional.

## Implementation
Separate orchestration from resource creation when the accepted design requires it. Specify an orchestrator as states, transitions, triggers, failures, recovery and completion criteria.
Provide component responsibilities, contract links, dependencies, implementation constraints and verifiable acceptance criteria. Keep implementation repositories separate when project policy requires it.
For a changed upstream decision, update canonical records first, then affected sequences/contracts/specifications and derived previews only. Keep stable IDs across renames; carry the new Name into canonical participant declarations and regenerate renderings. Record pending Lucid refreshes in the checkpoint; publishing remains a separate request.

Use the [component](../assets/templates/component.md) and [orchestrator](../assets/templates/orchestrator.md) templates. Generate code only if separately requested.

## Minimal decision record
Use: ID/title; status (proposed/accepted/superseded); context; choice; consequence; source/standard links.
Use the [decision template](../assets/templates/decision.md). Do not create records for routine restatements.

## Reusable standards intake
Capture source, scope, applicability, rule, exceptions and approval status. Compare existing standards; show conflicts and request approval before changing the library. Apply approved standards by ID/path without copying them into every artifact.

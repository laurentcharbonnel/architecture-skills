# Phase guidance

Read only the section needed for the current phase. Keep outputs in the project specifications repository, following the high-level-design/ and low-level-design/ separation in SKILL.md.

## Structure
Identify goals, actors, scope, constraints and system boundaries (C1); deployable/runnable containers, responsibilities and connections (C2); logical components and ownership (C3).
At C2, capture what information moves and where it originates without prematurely defining fields. Offer a short team review: choices, tradeoffs, risks, open decisions. Review status: draft, in-review, reviewed; never a mandatory gate.
Use the project output structure defined in SKILL.md: C1/C2 in high-level-design/overview.md and review.md; C3 and implementation details in low-level-design/. For existing projects, agree the mapping or migration before moving artifacts.

## Sequence
Choose a concrete scenario with the architect; do not assume business scenarios exist. Include actors, receiving components, sync/async calls, correlation, retries and failure paths when relevant. Trace messages to structure elements. Reuse stable names.

## Contracts
Identify the receiver/owner of every interface. Specify request/response or event schemas, validation, errors, authentication/authorization, idempotency, versioning and delivery semantics as relevant.
Use OpenAPI for HTTP contracts and an appropriate machine-readable event schema for messages. Keep undecided fields explicit; check syntax and available schema tooling before calling a contract valid.
Prefer approved project standards: REST Python, OAuth, enterprise messaging bus, or orchestrator templates only when supplied/approved for this project. Do not invent enterprise details or treat these examples as universal defaults.

## Implementation
Separate orchestration from resource creation when the accepted design requires it. Specify an orchestrator as states, transitions, triggers, failures, recovery and completion criteria.
Provide component responsibilities, contract links, dependencies, implementation constraints and verifiable acceptance criteria. Keep implementation repositories separate when project policy requires it.
For a changed upstream decision, list affected sequences/contracts/specifications and update only those.

## Minimal decision record
Use: ID/title; status (proposed/accepted/superseded); context; choice; consequence; source/standard links.
Do not create records for routine restatements.

## Reusable standards intake
Capture source, scope, applicability, rule, exceptions and approval status. Compare existing standards; show conflicts and request approval before changing the library. Apply approved standards by ID/path without copying them into every artifact.

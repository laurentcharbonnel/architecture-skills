---
name: implementation-planning
description: Convert a validated design or specification into an actionable implementation plan and small, testable tasks for human developers or coding agents. Supports greenfield and existing code across multiple repositories; planning only, without implementation.
---

# Implementation Planning

Turn an approved design into an execution handoff. This skill is independent: accept artifacts from architecture-design or any existing specification/design, in their original format. No sibling skill, canonical schema, vendor-specific tool, or design conversion is required.

## Boundaries

- Preserve approved architecture, technology choices, contracts, and repository boundaries. Do not redesign, silently resolve conflicting decisions, or invent missing requirements.
- Planning only: use read-only inspection of supplied designs and relevant repositories. Write only `implementation-plan.md` and `tasks.md` in the agreed project planning location (default: the current project directory). Do not modify specifications or implementation repositories, generate code, run application code/tests/builds, install dependencies, scaffold projects, or execute planned tasks.
- Treat repository inspection as evidence gathering, not execution. Use available file/search tools; no particular CLI, connector, or runtime is required.
- Require explicit human validation of the plan before implementation. End at the review handoff, even if the request also suggests starting implementation.

## Read Design → Inspect Repos → Identify Gaps → Plan Tasks

### 1. Read Design

Read the supplied entry document and only the linked sections needed for the requested scope: behavior, components, interactions, contracts, constraints, decisions, and acceptance expectations. For architecture-design outputs, use relevant design-docs, architecture-model sections, contracts, component details, or decisions only when needed; their presence is not required.

Identify the authoritative sources and their available revision/commit/version, the approved scope, exclusions, and design validation status. Do not treat silence as approval. If approval or source precedence is unclear, flag it for targeted confirmation and keep the plan a draft. Reference source paths/URLs and section or contract IDs; do not copy specifications into the plan.

### 2. Inspect Repos

Build a short repository map from supplied locations and design ownership: repository identifier, local path or URL, relevant revision when available, component responsibility, and **Greenfield** or **Existing Code** status. Assess each repo separately; mixed states are normal.

- **Greenfield:** Confirm the supplied location is new/empty or contains only starter material with a bounded top-level inspection. Plan only the minimum bootstrap needed by the approved stack and first vertical slice. Do not search for nonexistent implementations or choose an unspecified stack.
- **Existing Code:** Follow applicable repository instructions. Locate the relevant entry points with targeted path/text searches; inspect only affected modules, interfaces, nearby configuration, and representative tests. Identify what to reuse, extend, replace, or integrate, citing relevant paths/symbols. Stop reading once there is enough evidence to scope and verify the tasks.
- **Multiple repos:** Preserve ownership and independent build/release boundaries. Do not assume a monorepo, shared filesystem, shared pipeline, or atomic cross-repo commit. Record explicit producer/consumer contract and sequencing dependencies. Split cross-repo work into linked tasks with one target repo each.
- **Unavailable repos:** Distinguish unavailable/uninspected from empty. Record the access/evidence gap; do not fabricate code paths or claim inspection. Ask for access or a targeted excerpt only if it blocks useful planning.

### 3. Identify Gaps

Compare the design with the inspected starting point. Record only gaps that affect task scope, ownership, ordering, or verifiable completion.

Distinguish **blocking gaps** from **non-blocking assumptions**. For each blocker, identify the missing/conflicting fact, source reference, and affected task or phase. Ask the smallest set of targeted questions needed to unblock it; reuse answers already present. Never decide architecture on the user's behalf.

Continue planning independent work. Mark affected tasks blocked by a gap ID; do not present them as ready or invent detailed downstream steps. If the core design is insufficient, deliver a concise blocked draft with the missing decisions and only supportable tasks. Keep gap notes inside the two deliverables.

### 4. Plan Tasks

Prefer vertical slices that deliver an observable behavior across necessary layers. Add shared prerequisites only when they unblock concrete slices. Keep tasks small enough for one focused change and verification; split tasks with unrelated outcomes or independent acceptance. Avoid arbitrary task counts, speculative hardening, exhaustive future backlogs, and time estimates unless requested.

Sequence prerequisites, contract producers/consumers, integration, and any design-required migration or rollout steps. Parallelize only tasks with no real dependency or conflicting ownership. Do not assume independent repositories can deploy together; reflect compatibility or rollout constraints from the design, and flag missing decisions when they affect safe sequencing.

## Deliverables

Produce exactly these two Markdown files, in English, concise enough to review and use directly. Update existing plans in place when supplied; preserve stable IDs where possible. Do not add a gap report, README, diagrams, copied contracts, or extra tracking files.

### implementation-plan.md

Include:

- **Status and scope:** Draft — awaiting human validation (or Blocked draft); source references/revisions, design approval status, outcome, and exclusions.
- **Repository map:** Compact ownership and Greenfield/Existing Code summary, with inspection limits.
- **Phases:** Ordered phases with objectives, task IDs linked to `tasks.md`, prerequisites/dependencies, and a verifiable milestone or exit condition per phase. Reference tasks rather than repeating their details.
- **Gaps and assumptions:** Only material blockers (stable gap IDs), affected work, targeted questions, and explicitly labeled non-blocking assumptions.
- **Review gate:** Request explicit human validation of scope, order, dependencies, and acceptance criteria. State that implementation has not started and must wait for approval.

### tasks.md

Group tasks by phase. For each task include:

- **Stable ID and outcome:** One concrete, bounded change.
- **Target repo:** Exactly one mapped repository; relevant existing paths/symbols when inspected. Label proposed greenfield locations as proposed, not existing.
- **References:** Precise source sections/contract IDs (and code evidence when useful), without duplicating requirements or schemas.
- **Dependencies:** Task IDs, or None; blocking gap IDs and Blocked status when applicable. Cross-repo dependencies use the same global task IDs.
- **Acceptance criteria:** Observable pass/fail behavior and the focused verification method a developer should later use, including relevant contract/error cases required by the design. Describe intended checks without generating test code or running them. Avoid vague criteria such as "works" or "tests pass" without specifying the behavior.

Keep architectural rationale in the source design. Include only implementation context needed to perform and verify the task; no code or pseudocode.

## Final consistency check

Before handing off, check that scoped behavior is covered by tasks, references resolve or are explicitly marked unavailable, repository ownership is unambiguous, all task/gap IDs resolve, dependencies are acyclic and ordered, and milestones can be verified from task acceptance criteria. Ensure blocked work is visible and the human approval gate is explicit. Report only material limitations; do not claim runtime validation or measured token savings.

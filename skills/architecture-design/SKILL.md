---
name: architecture-design
description: Guide an architecture interview from a concept, diagram brief or existing specification to C4 structure, sequences, contracts and implementation handoff. Use to design, resume or revise software architecture with an architect.
---
# Architecture Design

Keep the architect in control. Write artifacts in English. Ask at most 3–4 related questions that change the design. Reuse validated answers; label assumptions and provisional decisions. Produce the first useful artifact early.

## Start or resume
1. Locate the project specifications and `interview/state.md`; ask for the project path only if unknown. Accept a brief, diagram, existing specs or an interview from scratch.
2. Read the checkpoint first, then only relevant linked artifacts and standards. Do not scan or reload the whole repository.
3. Resume its next action unless the user requests a different phase. Do not re-ask resolved questions. Read [workflow.md](references/workflow.md) only for the current phase.
4. Locate the configured shared standards library (or ask once for its path). Read [standards.md](references/standards.md) only for standards intake or conflicts. Use the [standard template](assets/templates/standard.md) when proposing a new entry.
5. Apply approved standards by reference without asking again for the same pattern. Surface conflicts. Require explicit approval to add, change or retire a reusable standard.

## Project output structure

Use this structure in the project specifications repository:
```text
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

Put C1/C2 and main logical information flows in `high-level-design/overview.md`, and team review feedback/status in `high-level-design/review.md`.
Put C3 and implementation specifications in `low-level-design/components/<component>.md`; detailed sequences in `low-level-design/sequences/<scenario>.md`; OpenAPI and other schemas in `low-level-design/contracts/`; state machines and behavior in `low-level-design/orchestrators/<orchestrator>.md`.
Put minimal ADRs in `decisions/`, recording whether each concerns high level design or low level design. Keep progress in `interview/state.md`.
Create files only when useful; do not generate empty placeholder documents or directories. Offer team review after C1/C2, before detailing C3; provisional continuation remains allowed.
For existing projects, map the current artifacts to this structure and propose a targeted migration; do not silently move files or create parallel duplicate specifications. Record the agreed mapping in the checkpoint.

## Workflow
- **Structure:** C1 context and C2 containers form the high level design; C3 components begin the low level design. Establish responsibilities, boundaries, dependencies and logical information flows. Recommend team review after C2; record feedback and review status, but allow provisional continuation. Before C3, summarize unresolved high level decisions and downstream risks without blocking.
- **Sequence:** model nontrivial scenarios after the relevant structure is clear. Cover important failure/retry paths; skip diagrams for trivial interactions.
- **Contracts:** derive API/event/data schemas after C3 and interactions. Make the receiving component own the contract. Link each contract to an interaction; avoid repeating schemas in prose.
- **Implementation:** provide component specifications, dependencies, acceptance criteria and open decisions. Include orchestrator state machines where applicable; generate code only if separately requested.

Use the relevant bundled template only when creating its artifact:
- Structure: [overview](assets/templates/high-level-overview.md), [component](assets/templates/component.md).
- Sequence: [flow](assets/templates/flow.md).
- Contracts: [OpenAPI skeleton](assets/templates/contract.yaml) for HTTP only.
- Implementation: [component](assets/templates/component.md), [orchestrator](assets/templates/orchestrator.md).
- Review or significant choice: [review](assets/templates/review.md), [decision](assets/templates/decision.md).
- Checkpoint: [interview state](assets/templates/interview-state.md).

Use Mermaid for C1/C2/C3 and useful sequences. Revisit earlier phases when evidence changes; sketch a contract early if needed to decide, marking it provisional. Do not force a C4 code diagram or developer-owned internal class layout.

## Save and keep context small
Update only changed artifacts and their dependants. Record a minimal decision only when a tradeoff needs traceability.
After a meaningful step, update `interview/state.md`: phase/component, validated and provisional decisions, artifact paths, applied standards, review status, open questions and the next concrete action.
Before compaction or a new worker, save this checkpoint and verify it is readable. Do not rely on transcript history.
Load [delegation.md](references/delegation.md) only when delegating or preparing a context handoff. Stay in the current agent for small tasks; do not silently change its model.
Finish when each artifact answers a concrete developer question; state unresolved blockers instead of inventing details.

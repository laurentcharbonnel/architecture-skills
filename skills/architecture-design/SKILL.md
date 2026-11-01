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
4. Apply approved standards by reference without asking again for the same pattern. Surface conflicts. Require explicit approval to add, change or retire a reusable standard.

## Workflow
- **Structure:** C1 context and C2 containers form the high level design; C3 components begin the low level design. Establish responsibilities, boundaries, dependencies and logical information flows. Recommend team review after C2; record review status, but allow provisional continuation.
- **Sequence:** model nontrivial scenarios after the relevant structure is clear. Cover important failure/retry paths; skip diagrams for trivial interactions.
- **Contracts:** derive API/event/data schemas after C3 and interactions. Make the receiving component own the contract. Link each contract to an interaction; avoid repeating schemas in prose.
- **Implementation:** provide component specifications, dependencies, acceptance criteria and open decisions. Include orchestrator state machines where applicable; generate code only if separately requested.

Use Mermaid for C1/C2/C3 and useful sequences. Revisit earlier phases when evidence changes. Do not force a C4 code diagram or developer-owned internal class layout.

## Save and keep context small
Update only changed artifacts and their dependants. Record a minimal decision only when a tradeoff needs traceability.
After a meaningful step, update `interview/state.md`: phase/component, validated and provisional decisions, artifact paths, applied standards, review status, open questions and the next concrete action.
Before compaction or a new worker, save this checkpoint and verify it is readable. Do not rely on transcript history.
Load [delegation.md](references/delegation.md) only when delegating or preparing a context handoff. Stay in the current agent for small tasks; do not silently change its model.
Finish when each artifact answers a concrete developer question; state unresolved blockers instead of inventing details.

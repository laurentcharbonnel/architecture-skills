---
name: architecture-design
description: Guide an architecture interview from a concept, diagram brief or existing specification to C4 structure, sequences, contracts and implementation handoff. Use to design, resume or revise software architecture with an architect.
---

# Architecture Design

Keep the architect in control. Converse in the user's language; write artifacts in English. Ask at most 3–4 related questions that change the design. Reuse validated answers; label assumptions and provisional decisions. Produce the first useful artifact early.

## Load only the selected workflow

- **Start or resume:** locate the specifications and `interview/state.md`; ask for the project path only if unknown. Read the checkpoint first, then relevant linked artifacts. Continue its next action unless redirected; do not re-ask resolved questions.
- **Design or revise:** read only the relevant phase and output paths in [workflow.md](references/workflow.md). Use its linked template when creating the artifact. Work through Structure → Sequence → Contracts → Implementation; revisit upstream choices when evidence changes.
- **Standards intake or conflict:** read [standards.md](references/standards.md). Locate the configured standards library (ask once if unknown) and save its path in the checkpoint. Use the [standard template](assets/templates/standard.md) for proposals. Apply approved standards by reference without asking again; require explicit approval to change the shared library.
- **Delegate or hand off:** read [delegation.md](references/delegation.md) only when needed. Stay in the current agent for small tasks; do not silently change its model.

## Architecture and evidence

C1/C2 form the high level design; C3 begins the low level design. Establish responsibilities, boundaries, dependencies and logical information flows before detailed contracts. Use Mermaid for useful structure and sequence diagrams. Do not force a code diagram or internal class layout.

Offer team review after C2, before C3. Record unresolved high level decisions and downstream risks; provisional continuation remains allowed. Preserve source evidence and approved standards; do not invent technologies or enterprise defaults. Agree a mapping before moving existing specifications or creating parallel artifacts. Generate code only if separately requested.

## Token budget and persistence

Keep project outputs in the specifications repository. Update affected artifacts and dependants only. Record minimal ADRs when tradeoffs need traceability. Do not scan or reload the whole repository.

After meaningful steps and before compaction or a fresh worker, save and verify `interview/state.md` using the [checkpoint template](assets/templates/interview-state.md): phase/component, decisions, artifact paths, standards, review status, open questions and next action. Do not rely on transcript history.

Finish when each artifact answers a concrete developer question; state unresolved blockers explicitly.

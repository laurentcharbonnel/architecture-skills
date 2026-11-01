---
name: architecture-design
description: Guide New Design interviews or turn existing architecture documentation into C4 structure, sequences, contracts and implementation handoff with Existing Design. Use to design, resume or revise software architecture with an architect.
---

# Architecture Design

Keep the architect in control. Converse in the user's language; write artifacts in English. In New Design, ask at most 3–4 related questions per batch that change the design; in Existing Design, ask only about blocking gaps, at most 3–4 targeted questions for intake. Reuse validated answers; label assumptions and provisional decisions. Produce the first useful artifact early.

## Load only the selected workflow

- **Start or resume:** locate the specifications and `interview/state.md`; ask for the project path only if unknown. Read the checkpoint first, then relevant linked artifacts. Continue its next action unless redirected; do not re-ask resolved questions.
- **Entry mode:** use **New Design** for a concept or brief needing design discovery; use **Existing Design** when explicitly requested (including “Existing Design mode”), or when the selected topic already has architecture documentation, even in another format. Follow [Existing Design intake](references/workflow.md#existing-design-intake): read only files relevant to the selected topic, reuse documented structure and behavior, distinguish facts/inferences/gaps, and never restart the full interview. Preserve source files in place without rewriting them. Present a short gap analysis and useful C1/C2 artifacts for architect validation before C3, sequences, contracts and implementation detail. These are entry modes, not additional workflow phases.
- **Canonical data:** before creating or changing structure/sequences, read the shared [Architecture Markdown v1 schema](../architecture-to-lucid/references/markdown-format.md) and reuse its [template](../architecture-to-lucid/assets/architecture-model-template.md). Maintain `high-level-design/architecture-model.md` for C1/C2 and `low-level-design/architecture-model.md` for C3 and detailed sequences, using that same schema. Record both paths/revisions in the checkpoint. Follow the shared schema’s context-reference rule; do not invent cross-file imports or duplicate sequence definitions. The sibling skill supplies this contract and validator; Lucid access is not needed.
- **Design or revise:** read only the relevant phase and output paths in [workflow.md](references/workflow.md). Use its linked template when creating the artifact. Work through Structure → Sequence → Contracts → Implementation; revisit upstream choices when evidence changes.
- **Standards intake or conflict:** read [standards.md](references/standards.md). Locate the authorized enterprise repository for standards and platform catalog (ask once if needed) and save its location in the checkpoint. Generic design patterns and artifact templates stay bundled with this public skill. Use the [standard template](assets/templates/standard.md) for proposals. Apply approved standards by reference without asking again; require explicit approval to change the shared library.
- **Delegate or hand off:** read [delegation.md](references/delegation.md) only when needed. Stay in the current agent for small tasks; do not silently change its model.

## Architecture and evidence

C1/C2 form the high level design; C3 begins the low level design. Establish responsibilities, boundaries, dependencies and logical information flows before detailed contracts. Elements, relationships, views and sequences belong in their owning canonical model; design documents explain them through short prose and derived diagrams. Create optional component, contract and orchestrator artifacts only when they answer a concrete implementation question; never create a separate `sequences/` artifact. Use [rendering guidance](references/canonical-rendering.md) with the execution timing below. Mermaid, Lucid and extracted JSON are disposable projections, never alternative architecture definitions. Do not force a code diagram or internal class layout.

- During interview back-and-forth, incrementally edit only affected records in the structured canonical model; do not regenerate Mermaid or human documents at every exchange.
- On validation of an existing phase/checkpoint, synchronize affected Mermaid diagrams and `design-doc.md` explanations from the canonical model.
- On an explicit preview request, generate only the requested Mermaid diagram from the current canonical model unless the architect explicitly requests Lucid.
- When revisiting a decision, update only impacted canonical records and dependent artifacts, applying the same synchronization timing.

Lucid generation is **STRICTLY on-demand**: never automatically call the Lucid connector or generate Lucid diagrams during interviews, checkpoints or artifact synchronization. Only an explicit architect request to create or update Lucid authorizes rendering; hand off to [architecture-to-lucid](../architecture-to-lucid/SKILL.md) using the existing canonical Markdown, without restarting the interview, and limit work to the explicitly requested C1/C2/C3 views or sequences. Prefer targeted updates to existing Lucid diagrams when the MCP supports them, rather than full recreation. Mermaid remains the default lightweight rendering in `design-doc.md`.

Keep Structure → Sequence → Contracts → Implementation unchanged; add no steps, files or Proposed/Accepted/Published lifecycle states. Preserve human-readable design documents, agent-readable canonical models and the shared architecture-to-lucid schema.

Offer team review after C2, before C3. Record unresolved high level decisions and downstream risks; provisional continuation remains allowed. Preserve source evidence and approved standards; do not invent technologies or enterprise defaults. Record the source-to-output mapping; preserve existing sources without moving or rewriting them, reuse conforming models, and avoid competing canonical outputs. Generate code only if separately requested.

## Readable Mermaid

For Mermaid diagrams in `design-doc.md`, prioritize readability over exhaustiveness: aim for 5–9 elements per view, show only essential relationships, use short labels and a consistent abstraction level. Split crowded diagrams into several focused views and add a short explanation of each view. `architecture-model.md` remains the complete canonical model; never remove information from it to simplify a diagram.

Apply the [Mermaid Clean / Minimal convention](references/canonical-rendering.md#mermaid-clean--minimal) when rendering these focused views; it aligns with the existing Lucid visual principles using Mermaid-native styles.

## Token budget and persistence

Keep project outputs in the specifications repository. Update affected artifacts and dependants only. Record minimal ADRs when tradeoffs need traceability. Do not scan or reload the whole repository.

After meaningful steps and before compaction or a fresh worker, save and verify `interview/state.md` using the [checkpoint template](assets/templates/interview-state.md): phase/component, canonical model paths and revisions, selected view/sequence IDs, decisions, artifact paths, standards, review status, open questions and next action. Do not rely on transcript history.

Finish when each artifact answers a concrete developer question; state unresolved blockers explicitly.

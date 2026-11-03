---
name: rapid-prototype
description: Frame a small technical experiment or visual prototype, write a concise specification and phased implementation plan, and hand it off to Codex or another developer. Implement and test the agreed phases only when requested. Use for prototypes and feasibility experiments, not production architecture.
---

# Rapid Prototype

Use **Technical POC** for technical feasibility and **Visual Prototype** for an interface, user flow, or simulation. Infer the mode from the request. Keep this skill standalone; no architecture-design or implementation-planning dependency is required.

## Workflow: Frame → Specify → Plan → Hand off → Implement → Evaluate

Default to preparation when the user wants to define a prototype or prepare work for Codex. Deliver the specification and execution plan before handing off implementation. Do not start coding merely because the word prototype appears. If the user explicitly asks to build, prepare the concise spec and plan first and then execute the authorized scope without an additional approval ceremony.

### 1. Frame the experiment
- State the hypothesis or experience to explore and the decision the prototype should inform.
- Identify users, the core demonstration scenario, constraints and the smallest useful scope. State exclusions.
- Reuse known answers. Ask at most 1–3 questions at a time, only when they materially change scope or block progress.
- Select observable success criteria and representative inputs. Respect time and token budgets.
- Separate confirmed requirements, reversible prototype assumptions and unresolved integration details. Do not turn assumptions into approved production decisions.

### 2. Write a concise specification
Write `spec.md`, or update the supplied specification in place.
Include the objective, scope/exclusions, core behavior, relevant interfaces or data examples, success criteria and labeled assumptions. Add failure behavior only where needed to make implementation unambiguous.
Use lightweight requirement IDs when they help link acceptance criteria to work.
Do not produce production architecture, C4 diagrams, extensive contracts or long design documents by default.

### 3. Create the implementation plan
Write `execution-plan.md`, or update the supplied plan in place.
Reference the spec rather than repeating it. Inspect only relevant existing code and repository instructions; distinguish unavailable repositories from empty ones.
Break the prototype into small ordered phases, preferably vertical slices with a demonstrable result. For each phase include:
- Stable ID, bounded outcome and target repository.
- Dependencies and relevant spec sections or requirement IDs.
- Concrete deliverables and observable acceptance criteria.
- Focused verification or demo steps.
- Temporary choices, mocks and integration gaps affecting that phase.

Identify the first assignment explicitly: which phase or small group of phases Codex should implement now, and which remain deferred. Do not ask it to build the whole roadmap automatically.
Preserve repository boundaries; never assume a monorepo or atomic changes across repositories.
Keep the plan proportional: a tiny visual prototype can have two short phases; do not manufacture a large backlog.

### 4. Resolve integration uncertainty without blocking unrelated work
Keep a compact gap table inside the plan: ID, confirmed issue or unverified assumption, impact, temporary substitute, required future validation, owner if known, affected phase.
Use reversible local defaults, fixtures, mocks and configurable adapters where they preserve the purpose of the experiment. State their limits.
Never mock the capability being validated and claim feasibility. If live integration is the hypothesis, mark it unverified until actually tested.
Missing credentials, network access or deployment choices should block only the dependent integration checks, not independent local work.
Ask for clarification only when no useful safe assumption preserves the agreed behavior. Record exact observed errors when available; do not guess why another coding session is blocked.

### 5. Hand off to Codex
Check that scope maps to phases, dependencies are ordered, references resolve, assumptions are explicit and each phase has testable completion criteria.
Provide a short English handoff prompt containing:
- Target repository and exact spec/plan paths.
- The first assignment and exclusions.
- Instructions to preserve existing work and reuse completed phases.
- Instructions to implement against the spec, run focused checks and report evidence.
- Instructions to record integration gaps for later resolution and continue independent work.
- Instructions to update phase status and the next action after each completed phase.

The default preparation deliverable is **spec + execution plan + a short handoff prompt**, not implementation code. Save in the requested project/repository when authorized and accessible; otherwise explain what is still needed for delivery.
For a preparation-only request, finish at handoff. Do not claim Codex has started or received the work automatically.

### 6. Implement and test when requested
Read the current spec, plan and existing work before coding. Implement only the assigned phases.
Write or update the minimal behavioral checks, implement the smallest solution and run focused verification.
- **Technical POC:** Exercise the capability under test with representative inputs and reproducible commands.
- **Visual Prototype:** Exercise the core interaction and inspect its state change; use sample data and label simulations. Use the existing UI stack or a self-contained HTML/CSS/JavaScript file when suitable.
Record phase status in the plan: TODO, IN_PROGRESS, DONE, BLOCKED or DEFERRED, with evidence and next action. Reuse an existing status file if present rather than creating duplicate tracking.
Distinguish simulated, SDK-stubbed and live integration checks. If execution is unavailable, provide manual steps and mark the result unverified. Never claim an unrun test passed.
Do not silently alter requirements to match the code. Record material deviations and their impact.

### 7. Evaluate
Report supported, rejected or inconclusive, with evidence, limitations and the next decision. For visual exploration, state what is demonstrated and what still needs user validation.
Stop when the assigned scope provides enough evidence. Do not automatically expand into production work.

## Keep preparation and implementation cheap
- Discuss in the user's language; write professional artifacts and handoff prompts in English.
- Prefer the lowest-cost suitable model when selection is available; never claim to switch models without a supported mechanism.
- Keep only the spec and plan mandatory. Add examples or tests when useful; avoid redundant README, task and tracking documents.
- Reuse existing dependencies, conventions and working code. Avoid broad repository scans, unnecessary installations and repeated checks.
- Use research or external services only when needed for the experiment or integration decisions.
- Do not deploy, publish an application or make destructive changes merely to demonstrate a prototype. Treat production work as a separately scoped follow-up.

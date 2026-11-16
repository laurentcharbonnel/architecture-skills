# AI-Driven Development Workflow — Integration Proposal

Status: proposed, not yet validated on a live feature.
Sources: https://github.com/mattpocock/skills and the existing skills in this repository.
Scope: reusable workflow guidance only. Do not store FactSet-specific artifacts here.

## Objective

Move from a business need to a reviewed pull request with explicit architecture decisions, low context-transfer overhead, and small verifiable increments. ChatGPT Work owns discovery/design; Codex owns implementation. GitHub is the durable source of truth. Preserve separate repositories (no monorepo assumption).

## Existing vs Matt Pocock skills

| Stage | Existing capability | Matt Pocock complement | Decision |
| --- | --- | --- | --- |
| Clarification | architecture-design interview / Existing Design | grill-with-docs (glossary + ADRs) | Borrow terminology discipline; avoid duplicate interviews |
| Architecture | architecture-design (HLD, LLD, contracts, ADRs) | domain-modeling / codebase-design | Keep architecture-design as authority |
| Implementation planning | implementation-planning (implementation-plan.md, tasks.md) | to-spec (user stories, test seams), to-tickets (vertical slices, blockers) | Extend handoff conventions; do not run both planners by default |
| Implementation | No production implementation skill here | implement, tdd | Use within Codex; small test-first slices at approved public seams |
| Verification | architecture review artifacts | code-review | Review against both specification and repository standards |
| Experiment | rapid-prototype | prototype | Keep rapid-prototype; use only to resolve a specific uncertainty |

Note: a standalone `handoff` skill was not found at `skills/engineering/handoff/SKILL.md` in Matt Pocock's repository. Treat handoff as our own artifact contract, not an attributed skill.

## Proposed flow

1. **Discover** (Work): capture problem, glossary, constraints, acceptance examples and open questions. Use targeted grilling only when information is missing.
2. **Design** (Work): use architecture-design for C1/C2 then C3, sequences, contracts and ADRs. Validate the architecture before implementation planning.
3. **Plan** (Work or Codex planning-only): use existing implementation-planning to inspect each target repository and produce implementation-plan.md and tasks.md. Borrow Matt's vertical tracer-bullet slicing and explicit blocker edges. Use to-spec only when a behavior-focused specification is missing; do not produce redundant parallel specs.
4. **Approve** (human): confirm repository boundaries, test seams, dependency ordering, acceptance criteria and integration risks.
5. **Execute** (Codex): one independently verifiable vertical slice at a time. Prefer test-first red/green at agreed public seams, run typechecks and focused tests frequently, and full checks at completion. Keep changes in the appropriate target repository.
6. **Review** (Codex + human): compare diff with the approved spec and with repo standards separately; record deviations and unresolved integration risks; create PR.
7. **Feedback** (Work): update only the impacted design/ADR/plan when implementation reveals a real architectural change.

## Handoff contract (per target repository)

- **Source references:** approved design revision, ADRs, API/message contracts, glossary.
- **Target:** repository, branch/PR convention, relevant modules, explicit cross-repository dependencies.
- **Scope:** user-observable behavior, non-goals, acceptance examples.
- **Execution:** ordered vertical slices with IDs and blockers; each fits one focused agent session.
- **Quality:** agreed test seams, commands for targeted tests/typecheck/full checks, review baseline.
- **Risks:** integration assumptions, external dependencies, unanswered questions; distinguish blockers from follow-ups.
- **Completion:** test evidence, PR link, deviations from design, remaining risks.

Use references rather than copying entire documents into agent prompts. Never silently turn unresolved decisions into implementation assumptions.

## Suggested pilot: Entity Resolution

This is a **generic test scenario only**, not an approved FactSet design:
- Input: a typed mention for a relative period, with an explicit company/calendar context.
- Expected output: a deterministic set of canonical period identifiers, or a typed unresolved/ambiguous result.
- Design questions: who interprets relative expressions; where calendar selection happens; ownership of the resolver API; deterministic vs LLM boundaries.
- Potential vertical slices: (1) contract and fixture-based public test, (2) one resolved relative-period path, (3) explicit unresolved/ambiguous path, (4) integration adapter if approved.
- Do not implement until architecture ownership, contracts and actual target repositories are confirmed.

## Lightweight evaluation criteria

Measure on the pilot: (a) number of unanswered questions at handoff, (b) number of agent iterations before first passing slice, (c) spec deviations found in review, (d) unnecessary duplicated artifacts, (e) time spent transferring context. Prefer fewer skills and shorter prompts if outcomes are equivalent.

## Next actions

1. Review this proposed workflow with the architect.
2. Select the pilot's actual target repository and approved design references.
3. Test one small feature end-to-end.
4. Only then decide whether to add a dedicated orchestration skill or a small AGENTS.md convention.

## References

- Matt Pocock: https://github.com/mattpocock/skills
- Existing repository: skills/architecture-design/, skills/implementation-planning/, skills/rapid-prototype/
- Matt's skills: skills/engineering/grill-with-docs/, to-spec/, to-tickets/, implement/, tdd/, code-review/

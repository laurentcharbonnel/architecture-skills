# AI-Driven Development Workflow — Integration Proposal

Status: proposed, not yet validated on a live feature.
Sources: https://github.com/mattpocock/skills and the existing skills in this repository.
Scope: reusable workflow guidance only. Do not store FactSet-specific artifacts here.

## Objective

Move from a business need to a reviewed pull request with explicit architecture decisions, low context-transfer overhead, and small verifiable increments. ChatGPT Work owns discovery, design and functional specifications; Codex owns the execution plan and implementation in the local repository clone. GitHub is the durable source of truth. Preserve separate repositories (no monorepo assumption).

## Default ownership and precedence

**Matt Pocock's skills are the default for every non-architecture stage. Our own skills are preferred only for architecture-specific work.** Keep existing skills available for backward compatibility, but do not invoke implementation-planning or rapid-prototype by default. Do not duplicate planning artifacts or interviews. This is a workflow selection policy, not an instruction to copy or modify Matt's upstream skills.

## Existing vs Matt Pocock skills

| Stage | Existing capability | Matt Pocock complement | Decision |
| --- | --- | --- | --- |
| Clarification | architecture-design interview / Existing Design | grill-with-docs (glossary + ADRs) | Prefer Matt's grill-with-docs and domain-modeling |
| Architecture | architecture-design (HLD, LLD, contracts, ADRs) | domain-modeling / codebase-design | Prefer our architecture-design, lucid-to-brief and architecture-to-lucid |
| Implementation planning | implementation-planning (implementation-plan.md, tasks.md) | to-spec (user stories, test seams), to-tickets (vertical slices, blockers) | Prefer Matt's to-spec then to-tickets; existing implementation-planning is fallback only |
| Implementation | No production implementation skill here | implement, tdd | Use within Codex; small test-first slices at approved public seams |
| Verification | architecture review artifacts | code-review | Review against both specification and repository standards |
| Experiment | rapid-prototype | prototype | Prefer Matt's prototype; rapid-prototype is fallback only |

Note: a standalone `handoff` skill was not found at `skills/engineering/handoff/SKILL.md` in Matt Pocock's repository. Treat handoff as our own artifact contract, not an attributed skill.

## Proposed flow

1. **Discover** (Work): use Matt's grill-with-docs and domain-modeling as needed to capture problem, glossary, constraints, acceptance examples and open questions.
2. **Design** (Work): use architecture-design for C1/C2 then C3, sequences, contracts and ADRs. Validate the architecture before implementation planning.
3. **Specify** (Work, published to GitHub) and **plan** (Codex in the local clone): prefer Matt's to-spec for a behavior-focused specification and to-tickets for vertical tracer-bullet tickets with explicit blocking edges. Respect the approved architecture, inspect each target repository, and avoid redundant artifacts. Existing implementation-planning is a fallback only when the Matt workflow cannot meet a specific constraint.
4. **Approve** (human): confirm repository boundaries, test seams, dependency ordering, acceptance criteria and integration risks.
5. **Execute** (Codex): prefer Matt's implement and tdd, one independently verifiable vertical slice at a time. Prefer test-first red/green at agreed public seams, run typechecks and focused tests frequently, and full checks at completion. Keep changes in the appropriate target repository.
6. **Review** (Codex + human): prefer Matt's code-review; compare diff with the approved spec and with repo standards separately; record deviations and unresolved integration risks; create PR.
7. **Feedback** (Work): update only the impacted design/ADR/plan when implementation reveals a real architectural change.

## Project-specific PR reviewer

Create and commit `.codex/agents/pr_reviewer.toml` when bootstrapping each project repository. For an existing project, add it when adopting this workflow. Each repository owns its reviewer configuration. Reference it from the repository's `AGENTS.md` and run the reviewer separately from implementation for every pull request.

Adapt the reviewer to the project's acceptance criteria, architecture and repository conventions, and name the CI jobs and validation commands that apply there. The reviewer works read-only against the ticket and the full diff, identifies the exact head commit it reviewed, and distinguishes blocking findings from suggestions. Run the review again after fixes change the head commit. The repository's merge policy governs how the result is used.

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
3. Test one small feature end-to-end with Matt's skills for discovery, specification, tickets, implementation and review, and our skills for architecture.
4. Only then decide whether to add a dedicated orchestration skill or a small AGENTS.md convention.

## References

- Matt Pocock: https://github.com/mattpocock/skills
- Existing repository: skills/architecture-design/, skills/implementation-planning/, skills/rapid-prototype/
- Matt's skills: skills/engineering/grill-with-docs/, to-spec/, to-tickets/, implement/, tdd/, code-review/

## Local execution ownership — adopted 19 November 2026

Work prepares functional specifications, acceptance criteria and constraints and commits them to GitHub. The user clones or updates the target repository locally and opens it in Codex. Codex reads the published specifications, builds and tracks the execution plan, implements, tests and coordinates the project reviewer. The user steers execution directly in Codex. GitHub records specifications, code, pull requests and review evidence.

The previous Work-to-Latitude background service and ticket queue are retired. Open the existing local Codex project to continue implementation. Work resumes specification work using the latest GitHub state.

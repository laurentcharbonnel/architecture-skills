# Rapid Prototyping — Operating Guide

## Purpose
Go from a technical idea to a working proof of concept quickly, with minimal tokens and documentation. Use the reusable `rapid-prototype` skill (Technical POC or Visual Prototype).

## Repeatable workflow
1. **Frame (ChatGPT Work):** State the hypothesis, target users, constraints, success criteria, and a tiny demonstrable scope. Ask only blocking questions.
2. **Prepare GitHub:** Create a dedicated repository for the POC. Add a concise `README.md`, a minimal `spec.md`, representative input examples, and an explicit definition of done. Keep skill definitions in the separate skills repository.
3. **Build (Codex or Claude Code):** Open the POC repository, make the `rapid-prototype` skill available, ask the agent to implement only the agreed minimal scope, run tests, and report limitations.
4. **Validate:** Execute the demo, inspect evidence and failures, then decide to stop, iterate, or move to a production architecture. Avoid premature production hardening.
5. **Record:** Capture result, constraints, decisions, cost/time, and next steps in the repository README.

## Reusable Codex prompt
Use the `rapid-prototype` skill in Technical POC mode.
Read README.md and spec.md in this repository.
Implement only the minimum demonstrable scope and tests.
Keep dependencies, token usage, and documentation minimal.
Run the tests and report what works, what fails, and how to reproduce.
Do not introduce production architecture or unrelated refactoring.

## Example POC: generic UI test automation
**Goal:** Given an application URL and declarative YAML test scenarios, execute browser-based UI tests and produce an understandable report, without needing the Vue.js source code.

**Design:** YAML scenarios -> Playwright runner -> pass/fail report + screenshots on failure. Prefer accessible role/name and label selectors; use stable `data-testid` for complex components. Missing or ambiguous elements fail explicitly. No LLM calls during normal execution. AI may assist in converting existing informal test cases into YAML.

**Initial scope:** Three representative YAML scenarios against a small Vue.js demo app. Then run the same generic runner against an actual authorized application. No production platform, CI integration, or complex agent framework in the first iteration.

**Success criteria:**
- The runner accepts a configurable application URL and YAML scenarios.
- It can navigate, fill fields, click named controls, and assert visible messages.
- It produces reproducible pass/fail results and actionable failure evidence.
- It does not need access to application source or invoke an LLM at runtime.

**Security:** Use only authorized test environments. Never commit credentials, personal data, or internal application URLs to a public repository. Configure secrets and test accounts outside YAML committed to Git.

## Responsibilities
- **Work:** Collaborative framing, short specifications, example inputs, review.
- **Codex:** Implementation, execution, debugging, test evidence.
- **GitHub:** Shared source of truth and handoff.
- **Claude Code alternative:** Can perform both framing and implementation in a single tool.

## Before starting each new POC
Specify: hypothesis; URL/environment or technical target; 1–3 sample scenarios; success criteria; repo visibility; whether secrets or company information are involved.

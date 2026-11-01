---
name: rapid-prototype
description: Quickly test a technical hypothesis with executable code or explore an interface, user flow, or simulation with a minimal interactive prototype. Use for small experiments, not production architecture.
---

# Rapid Prototype

Use **Technical POC** for technical feasibility and **Visual Prototype** for an interface, user flow, or simulation. Infer the mode from the request unless the distinction blocks progress. This skill is standalone; it does not require architecture-design or another skill.

## Workflow: Idea → Minimal Scope → Build → Test → Decide

1. **Idea:** State the hypothesis or experience to explore in one sentence. Ask only 1–3 genuinely blocking questions, and none when reasonable assumptions suffice. State assumptions briefly and start producing.
2. **Minimal Scope:** Pick one observable success criterion and the smallest experiment that can test it. Keep this to a few lines, not a separate plan. Respect any time or token budget.
3. **Build:** Produce a runnable artifact immediately after scoping, using the simplest available tools and fewest files.
   - **Technical POC:** Implement only the path needed to test the hypothesis. Use representative input and a minimal assertion, smoke test, or reproducible command.
   - **Visual Prototype:** Build the smallest interactive screen, flow, or simulation that makes the idea tangible. Use local sample data and mocked services where sufficient; label simulated behavior. Prefer a self-contained HTML/CSS/JavaScript file when it fits, or the existing UI stack.
4. **Test:** Run the smallest meaningful check against the success criterion.
   - **Technical POC:** Execute the code and minimal test; capture the observed result.
   - **Visual Prototype:** Exercise the core interaction and inspect the relevant state change or output. Use a browser only if available. If interaction cannot be checked, provide exact manual steps and mark it unverified.
   - Distinguish observed results from expectations. If execution is unavailable, say so; never claim a test passed.
5. **Decide:** Give a short conclusion: supported, rejected, or inconclusive; evidence; explicit limitations; and optional next steps. For visual exploration, say what the interaction demonstrates and what still needs user validation. Stop once the criterion provides enough evidence; if blocked or inconclusive, report the gap rather than expanding scope automatically.

## Keep the experiment cheap

- **From scratch:** Start in a small, self-contained location with an available runtime; avoid project generators and frameworks unless necessary.
- **Existing repository:** Follow applicable repository instructions. Locate the relevant entry point with a targeted path or text search; read only the files and nearby configuration needed for the experiment. Do not scan or summarize the entire repository. Keep unrelated code untouched.
- Skip research, broad repository reading, dependency installation, and external services unless the hypothesis requires them. Prefer existing dependencies or the standard library. Do not assume a specific CLI, connector, browser, or test runner is installed.
- Mock supporting behavior only; do not mock the capability being validated. Expose assumptions and mocks that limit the conclusion.
- Do not create production architecture, C4 diagrams, ADRs, long plans, extensive documentation, exhaustive tests, or production hardening by default.
- Deliver only the prototype/code and, when useful, a brief README or test result with run instructions. A concise final response is enough when no extra file is needed.
- Iterate through small edits and focused checks. Preserve working code; do not regenerate the whole prototype or repeat unrelated checks.
- Do not deploy, publish, or make destructive changes merely to demonstrate the prototype. Treat production work as an optional follow-up requiring its own scope.

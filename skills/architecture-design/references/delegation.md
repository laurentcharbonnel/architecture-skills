# Bounded delegation and recovery

Use this policy only when delegation or context renewal is useful. It is the canonical common policy; the diagram skill may use it when installed, but remains independent.

- Keep the coordinator focused on plan, validated decisions, artifact paths and progress.
- Prefer one bounded worker over a team. Delegate only when isolation or specialization repays startup and handoff cost.
- Choose architecture-extract (Haiku) for factual extraction, comparison and mechanical checks; choose architecture-review (Opus) for difficult tradeoffs, inconsistency resolution or design review. If unavailable, stay in the main session and state the limitation. Escalate uncertainty rather than repeatedly retrying a weak worker.
- Give a worker: objective, exact input paths/sections, relevant approved constraints, allowed output paths, completion condition and a concise return format. Do not send the whole conversation or ask it to read all specs.
- Return: findings, evidence paths, assumptions, unresolved questions and proposed changes. The coordinator/architect owns acceptance.
- Give concurrent workers disjoint write ownership. Never let a new worker overwrite unverified partial work.
- Before finishing a bounded task or renewing an agent, persist the checkpoint: phase, completed work, decisions with status, changed paths, pending work and next action. Verify it exists before relying on it.
- Start a fresh worker at natural phase boundaries when further delegation is useful. Load the checkpoint and its relevant files only. Renew the coordinator similarly by saving a checkpoint before a fresh session.
- If context pressure is visible, pause expansion and checkpoint. If a worker disappears before saving, inspect its artifacts and last verified checkpoint; mark partial work unverified.
- Do not claim precise remaining-context measurement or automatic termination/restart. These instructions provide a handoff protocol, not a monitoring runtime.

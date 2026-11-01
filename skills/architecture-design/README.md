# Architecture Design

A Claude Code skill for **concept or brief → architecture interview → HLD/LLD → implementation handoff**. It covers Structure → Sequence → Contracts → Implementation, with explicit decisions and resumable checkpoints.

## Install in Claude Code

Clone the repository if needed:

```bash
git clone https://github.com/laurentcharbonnel/architecture-skills.git
cd architecture-skills
mkdir -p ~/.claude/skills
cp -R skills/architecture-design ~/.claude/skills/
```

Run the copy from the repository root. Compare or back up an existing destination first. For project-only installation, copy the folder into the project's `.claude/skills/` instead. To update, run `git pull --ff-only` in the clone and repeat the copy after reviewing local changes. [Claude Code skills](https://code.claude.com/docs/en/skills).

## Prerequisites

Provide the project specifications path and any approved shared standards library. The skill records the standards path once and applies approved rules by reference. No technology or enterprise standard is pre-approved. Keep specifications and implementation repositories separate where project policy requires it.

No MCP connection is required for the interview. To extract a Lucid source first, use [lucidchart-to-brief](../lucidchart-to-brief/README.md); to publish C4 views, use [c4-markdown-to-c4-lucid](../c4-markdown-to-c4-lucid/README.md).

Optional agents are in [claude-agents/](../../claude-agents/). From the repository root:

```bash
mkdir -p ~/.claude/agents
cp claude-agents/architecture-extract.md claude-agents/architecture-review.md ~/.claude/agents/
```

Compare existing destinations before copying. For project scope, use `.claude/agents/`. Check availability with `/agents`. Extraction uses Haiku; design review uses Opus when available. The skill works without these agents and does not switch the main session's model. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents).

## Use it

### 1. Start from a concept or brief

```text
/architecture-design Start from docs/brief.md in this project. Establish C1/C2 and the main logical information flows. Ask only the next useful batch of questions and keep proposed choices explicit.
```

### 2. Resume the interview

```text
/architecture-design Resume from interview/state.md. Read the checkpoint and relevant artifacts, reuse resolved answers and continue the recorded next action.
```

### 3. Revise a decision

```text
/architecture-design Review the requested change in decisions/002-integration.md. Identify affected components, sequences and contracts, discuss the tradeoff, then update the agreed artifacts and checkpoint.
```

## Resources and output

The [workflow reference](references/workflow.md) defines output paths and phase guidance. C1/C2 belong in `high-level-design/overview.md`, with team feedback in `high-level-design/review.md`. C3 and implementation details belong in `low-level-design/components/`, `sequences/`, `contracts/` and `orchestrators/`. Store ADRs in `decisions/` and progress in `interview/state.md`. Create only useful artifacts; agree a mapping before migrating existing specifications.

Use the bundled [templates](assets/templates/), [standards guidance](references/standards.md) and optional [delegation protocol](references/delegation.md) for the relevant operation. Team review after C2 is recommended; provisional continuation remains possible. Code generation requires a separate request.

## Token efficiency

Read the checkpoint first and load only relevant artifacts, phase guidance and templates. Keep decisions and pending work in files; do not reload the full conversation or repository. Delegation uses bounded inputs and compact handoffs, without automatic fan-out or a context-monitoring runtime.

## Validation and limits

Check frontmatter, resource links and installation structure. In Claude Code, exercise start, resume and changed-decision scenarios on a representative project before relying on the skill at work. Structural checks do not prove interview quality, implementation readiness or token savings. No exact context monitor, automatic restart or automatic main-session model switching is provided.

## Integration

Accept the factual brief from `lucidchart-to-brief` as input. Keep architecture decisions here; request `c4-markdown-to-c4-lucid` separately to normalize and publish selected diagrams. Shared standards stay in their configured library.

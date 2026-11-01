# Architecture Design

A Claude Code skill with two entry modes: **New Design** (concept or brief → architecture interview) and **Existing Design** (existing documentation → useful High-Level Design/Low-Level Design artifacts). Both lead to implementation handoff. It covers Structure → Sequence → Contracts → Implementation, with explicit decisions and resumable checkpoints.

## Install in Claude Code

Clone the repository if needed:

```bash
git clone https://github.com/laurentcharbonnel/architecture-skills.git
cd architecture-skills
mkdir -p ~/.claude/skills
cp -R skills/architecture-design skills/architecture-to-lucid ~/.claude/skills/
```

Run the copy from the repository root. Compare or back up an existing destination first. Install both sibling folders together: architecture-design reuses the existing schema, template and validator from architecture-to-lucid. For project-only installation, copy both folders into the project's `.claude/skills/` instead. To update, run `git pull --ff-only` in the clone and repeat the copy after reviewing local changes. [Claude Code skills](https://code.claude.com/docs/en/skills).

## Prerequisites

Provide the project specifications path. Generic design patterns and artifact templates are bundled with this skill. When enterprise guidance is needed, provide access to an authorized enterprise GitHub repository containing standards and a platform catalog. The skill records its location once and applies approved rules by reference. It works without enterprise access, leaving enterprise choices unverified rather than inventing them. No technology or enterprise standard is pre-approved. Keep specifications and implementation repositories separate where project policy requires it.

Lucid is strictly on-demand: never call its connector automatically during interviews, checkpoints or artifact synchronization. Only an explicit architect request authorizes Lucid creation/update for the requested C1/C2/C3 views or sequences, reusing canonical Markdown without restarting the interview; prefer targeted updates when the MCP supports them. Mermaid remains the default lightweight rendering in `design-doc.md`. No MCP connection is required for the interview. To extract a Lucid source first, use [lucid-to-brief](../lucid-to-brief/README.md); to publish C4 views, use [architecture-to-lucid](../architecture-to-lucid/README.md).

Optional agents are in [claude-agents/](../../claude-agents/). From the repository root:

```bash
mkdir -p ~/.claude/agents
cp claude-agents/architecture-extract.md claude-agents/architecture-review.md ~/.claude/agents/
```

Compare existing destinations before copying. For project scope, use `.claude/agents/`. Check availability with `/agents`. Extraction uses Haiku; design review uses Opus when available. The skill works without these agents and does not switch the main session's model. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents).

## Use it

### 1. New Design — start from a concept or brief

```text
/architecture-design Start from docs/brief.md in this project. Establish C1/C2 and the main logical information flows. Ask only the next useful batch of questions and keep proposed choices explicit.
```

### 2. Existing Design — reuse architecture already documented

```text
/architecture-design Existing Design for the payments topic in docs/payments/. Reuse the relevant architecture documents without moving or rewriting sources. Produce a short gap analysis and C1/C2 HLD artifacts first; wait for my validation before C3, sequences, contracts and implementation detail. Ask at most 3–4 targeted questions only for blocking gaps; do not restart the full interview.
```

The [intake guidance](references/workflow.md#existing-design-intake) separates documented facts, inferences to validate and gaps, with source locators. It reuses existing components, relationships, decisions, scenarios and contracts, generates only useful outputs in the structure below, and keeps the same canonical format for Mermaid and architecture-to-lucid. No new skill or workflow phase is added.

### 3. Resume either mode

```text
/architecture-design Resume from interview/state.md. Read the checkpoint and relevant artifacts, reuse resolved answers and continue the recorded next action.
```

### 4. Revise a decision

```text
/architecture-design Review the requested change in decisions/002-integration.md. Identify affected components, sequences and contracts, discuss the tradeoff, then update the agreed artifacts and checkpoint.
```

## Resources and output

**Human-readable:** `design-doc.md` explains the design briefly with embedded Mermaid diagrams and concise explanations; `review.md` captures feedback and open decisions. Optional component/orchestrator specifications and minimal ADRs add implementation detail or rationale only when useful.

**Machine/agent-readable:** each `architecture-model.md` is a structured canonical model using the same [schema](../architecture-to-lucid/references/markdown-format.md) and [template](../architecture-to-lucid/assets/architecture-model-template.md). Agents use its tables and sequence PlantUML to generate Mermaid/Lucid. `contracts/` holds machine-readable OpenAPI/event schemas; `interview/state.md` is the resume checkpoint.

```text
high-level-design/
  design-doc.md          # short human explanation of C1/C2
  architecture-model.md  # canonical C1/C2 model
  review.md              # lightweight feedback and open decisions, when useful
low-level-design/
  design-doc.md          # short human explanation of C3 and interactions
  architecture-model.md  # canonical C3 model and detailed sequences
  components/            # optional component implementation specifications
  contracts/             # optional OpenAPI and event schemas
  orchestrators/         # optional states, transitions and behavior
decisions/             # minimal ADRs when needed
interview/state.md     # paths, revisions, decisions and next action
```

Create only useful files. Sequences live once inside the owning structured model; there is no separate `sequences/` artifact. Mermaid, Lucid and extracted JSON are derived outputs: change the canonical model first. Each model validates independently; necessary HLD context in LLD follows the shared schema’s reference rule. The [workflow](references/workflow.md) and [rendering guidance](references/canonical-rendering.md) define ownership and refresh behavior. Record a non-destructive source-to-output mapping for Existing Design; preserve sources in place and reuse conforming models.

Use the bundled [templates](assets/templates/), [standards guidance](references/standards.md) and optional [delegation protocol](references/delegation.md) for the relevant operation. Team review after C2 is recommended; provisional continuation remains possible. Code generation requires a separate request.

## Token efficiency

Read the checkpoint first and load only relevant artifacts, phase guidance and templates. Keep decisions and pending work in files; do not reload the full conversation or repository. Delegation uses bounded inputs and compact handoffs, without automatic fan-out or a context-monitoring runtime.

## Validation and limits

Check frontmatter, resource links and the paired installation structure. Validate each existing canonical model with the existing helper, from the repository root:

```bash
python3 skills/architecture-to-lucid/scripts/validate_markdown.py /project/specifications/high-level-design/architecture-model.md
python3 skills/architecture-to-lucid/scripts/validate_markdown.py /project/specifications/low-level-design/architecture-model.md
python3 skills/architecture-to-lucid/scripts/test_validate_markdown.py
```

The blank template is intentionally incomplete. During discovery, checkpoint unresolved errors; do not invent design to pass validation. Schema validation does not prove Mermaid rendering or semantic fidelity; compare derived previews against selected canonical IDs and original sequence semantics. In Claude Code, exercise New Design, Existing Design (including source preservation and blocking gaps), resume and changed-decision scenarios on a representative project before relying on the skill at work. Structural checks do not prove interview quality, implementation readiness or token savings. No exact context monitor, automatic restart or automatic main-session model switching is provided.

## Integration

Accept the factual brief from `lucid-to-brief` as input. Keep architecture decisions here and maintain the HLD/LLD canonical models in the shared format throughout the interview. Request `architecture-to-lucid` separately to validate and publish selected views/sequences from each owning model’s exact path/revision, without a normalization pass. Requested diagram edits update canonical Markdown first, then affected previews; mappings and JSON remain derived. Enterprise standards and the platform catalog stay in the authorized enterprise repository; generic patterns and artifact templates stay in this public skill.

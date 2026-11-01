---
name: lucidchart-to-brief
description: Extract a concise factual architecture input brief from a Lucidchart URL via the configured Lucidchart MCP, or a supplied export, screenshot or equivalent process diagram, using a short interview to resolve ambiguity.
---

# Lucidchart to Brief

Converse in the user's language; produce an English Markdown brief for architecture-design or independent use. Preserve business meaning; do not redesign the system.

## Load only the selected workflow

- **Read a Lucidchart URL:** discover the configured MCP tools and read [lucidchart-mcp.md](references/lucidchart-mcp.md). Retrieve the source before asking for a description or export. Never claim access to an unread URL. If setup is missing, point to the MCP prerequisites in [README.md](README.md); do not configure or authenticate automatically.
- **Read a supplied export or screenshot:** inspect it directly. State which labels, connectors and pages are observable; live retrieval is unnecessary unless requested or needed for missing evidence.
- **Draft a brief:** use [assets/brief-template.md](assets/brief-template.md), retaining useful sections only. Draft early, then ask at most 3–4 related questions that materially affect interpretation.
- **Resume or revise:** read `interview/brief-state.md` first, then only relevant source material and affected brief sections. Reuse resolved answers.

## Source fidelity

Preserve readable names, actors, blocks, boundaries and arrow direction. Separate observations from interpretations. Mark unreadable labels, ambiguous connectors and missing legends; proximity alone is not a relationship. Cite page/region, evidence IDs or element labels for important observations.

Keep logical information exchanges only where observable. Do not invent scenarios, components, APIs or technologies. Keep inferred details provisional and unresolved questions explicit. Disclose capability gaps; never modify the source or its sharing settings during extraction.

## Token budget and persistence

Scope and cache retrieval as described in the MCP reference. Update affected sections only. Save the brief at an agreed project path and `interview/brief-state.md` after meaningful steps: source/version, inspected evidence and gaps, resolved/open questions, brief path and next action.

Stay in the current agent for small tasks. For a large extraction, use architecture-extract if installed with exact inputs and a bounded output; retain architect review of uncertain meaning. Read architecture-design's delegation reference only if available and needed. Otherwise hand off findings, evidence, assumptions, open questions and next action. Checkpoint before a fresh worker; do not assume exact context monitoring or automatic restart.

Hand off the brief path to architecture-design when requested; do not automatically run the full design workflow.

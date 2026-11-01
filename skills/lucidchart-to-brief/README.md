# Lucidchart to Brief

A Claude Code skill for **Lucidchart diagram → evidence-backed Markdown brief → architecture input**. Preserve observed business meaning, separate interpretation from facts and record unresolved questions.

## Install in Claude Code

Clone the repository if needed:

```bash
git clone https://github.com/laurentcharbonnel/architecture-skills.git
cd architecture-skills
mkdir -p ~/.claude/skills
cp -R skills/lucidchart-to-brief ~/.claude/skills/
```

Run the copy from the repository root. Compare or back up an existing destination first. For project-only installation, copy the folder into the project's `.claude/skills/` instead. To update, run `git pull --ff-only` in the clone and repeat the copy after reviewing local changes. [Claude Code skills](https://code.claude.com/docs/en/skills).

## Prerequisites

For a Lucidchart URL, use the same connection as `c4-markdown-to-c4-lucid`.

Configure the Lucid MCP once in Claude Code:

```bash
claude mcp add --transport http lucid https://mcp.lucid.app/mcp
```

Then run `/mcp` in Claude Code and authorize Lucid. Team/Enterprise accounts require administrator enablement of MCP access; your AI tool administrator may also need to authorize the integration. Reuse an existing authorized connection rather than adding a duplicate. [Official Lucid setup](https://help.lucid.co/hc/en-us/articles/42578801807508-Integrate-Lucid-with-AI-tools-using-the-Lucid-MCP-server).

No credentials are bundled, and the skill does not configure or authenticate an account automatically.

For extraction only, Lucid also provides `https://mcp.lucid.app/mcp/readonly`; substitute that URL in the command if desired. It cannot support later diagram creation. The extraction workflow uses read-only operations with either connection.

A supplied export or screenshot can be read without MCP; the brief must state what could be inspected. Optional extraction agents follow the [architecture-design setup](../architecture-design/README.md#prerequisites), but are not required.

## Use it

### 1. Extract a Lucidchart document

Replace `<Lucidchart URL>` with the source link:

```text
/lucidchart-to-brief Read <Lucidchart URL> through the configured MCP and prepare docs/brief.md. Preserve source labels, boundaries and directed interactions. List evidence and uncertainties; do not redesign the system.
```

### 2. Use a supplied export

```text
/lucidchart-to-brief Extract docs/process-export.pdf into docs/brief.md. Distinguish readable observations from interpretations and state which connectors or labels cannot be verified.
```

### 3. Resume after clarification

```text
/lucidchart-to-brief Resume from interview/brief-state.md. Apply my answers to the affected brief sections and keep remaining ambiguities visible.
```

## Resources and output

The [MCP read procedure](references/lucidchart-mcp.md) covers tool discovery, provenance, retrieval gaps and access failures. The [brief template](assets/brief-template.md) provides reusable sections; omit sections that add no useful information.

Save the brief at an agreed project path and progress in `interview/brief-state.md`. Record the source/version, pages and evidence inspected, resolved and open questions, brief path and next action. The workflow does not change the Lucid source or its sharing settings.

## Token efficiency

Scope retrieval to relevant pages once the scope is known. Reuse cached source material and the checkpoint; refetch only when missing, stale or requested. Load the MCP procedure only for live retrieval and the brief template when creating a brief. Optional workers receive exact inputs and a bounded objective.

## Validation and limits

Check frontmatter, resource links and installation structure. In Claude Code, verify an accessible URL, an unavailable source, a supplied export and a resume after clarification. A successful read does not prove full topology: disclose missing pages, properties, unreadable labels and unsupported connector details. Live extraction quality and token savings are not established by structural checks.

## Integration

Pass the saved brief path to [architecture-design](../architecture-design/README.md) when requested. Extraction does not automatically start design or invent components, APIs or technologies. Use [c4-markdown-to-c4-lucid](../c4-markdown-to-c4-lucid/README.md) for the separate Markdown-to-diagram workflow.

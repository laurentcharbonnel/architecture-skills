# Markdown to Lucid kit

A compact Claude Code skill for **external documentation → structured Markdown → editable Lucid C4 and sequence diagrams**. Conversations can be in French; all professional artifacts are in English.

## Install in Claude Code

Copy the `skills/markdown-to-lucid` folder into your project's `.claude/skills/` directory, so the entry point is `.claude/skills/markdown-to-lucid/SKILL.md`. For use across projects, copy it into `~/.claude/skills/markdown-to-lucid/` instead. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

The skill uses the existing Lucid MCP connection. If not configured, run:

```bash
claude mcp add --transport http lucid https://mcp.lucid.app/mcp
```

Then run `/mcp` in Claude Code and authorize Lucid. Team/Enterprise accounts may require administrator enablement. This package contains no credentials and does not configure or authenticate an account automatically. [Official Lucid setup](https://help.lucid.co/hc/en-us/articles/42578801807508-Integrate-Lucid-with-AI-tools-using-the-Lucid-MCP-server).

## Use it

### 1. Normalize an external document

```text
/markdown-to-lucid Normalize docs/external-spec.md into docs/architecture.md using the bundled template. Preserve source references, mark inferred structure Proposed and list missing information. Do not create Lucid documents yet.
```

You can also copy [skills/markdown-to-lucid/assets/architecture-template.md](../skills/markdown-to-lucid/assets/architecture-template.md) and fill it yourself. The completed [domain-tasks-example.md](../skills/markdown-to-lucid/assets/domain-tasks-example.md) demonstrates C1, C2, a proposed logical C3 and a sequence with failure/retry branches.

### 2. Create Lucid from the Markdown

```text
/markdown-to-lucid Create the C1 and C2 views from docs/architecture.md in Lucid. Apply the convention, verify actual readback and visual output, and save the links and fidelity report.
```

Request C3 and sequence sections when needed. Missing details stay explicit; logical views need not select a stack. A plain request to normalize documentation does not publish it.

### 3. Review a manual change

```text
/markdown-to-lucid Compare the saved architecture.md and Lucid mapping with the current diagrams. Report changes, then update the Markdown to reflect my edits.
```

## Token efficiency

- The entry point is about 400 words; detailed references load by operation.
- Element definitions are shared across views, with stable ID lists for each view.
- Optional columns and document defaults avoid repeated status/source/technology cells.
- Validation runs as a Python script; its code and the long example need not enter model context.
- Readback is reduced to differences/counts; unchanged views are reused.

Token savings depend on the source and tool responses; this is not a fixed token-count guarantee.

## Local checks

Python 3.9+; standard library only. From the repository root:

```bash
python3 skills/markdown-to-lucid/scripts/validate_markdown.py markdown-to-lucid/assets/domain-tasks-example.md
python3 skills/markdown-to-lucid/scripts/validate_markdown.py docs/architecture.md --json > docs/architecture-model.json
python3 skills/markdown-to-lucid/scripts/test_validate_markdown.py
```

The blank template intentionally fails until populated. The helper checks structural consistency, not business correctness or Lucid renderability. Native sequence source must be read back because generic fetch was observed to omit actor/database interactions. Fidelity is assessed separately from visual quality.

## Integration with the architecture framework

Keep the existing architecture-design skill responsible for the interview, HLD and LLD. Use this complementary skill to normalize its output, publish selected views, and verify diagrams. No changes to shared standards or automatic synchronization are included.

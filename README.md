# Architecture Skills

Concise, interview-driven skills for Claude Code. Keep reusable methods here and project specifications in their own repositories. Publish no company information, credentials or internal diagrams.

| Skill | Purpose |
| --- | --- |
| architecture-design | Turn a concept or brief into implementation-ready architecture through Structure → Sequence → Contracts → Implementation. |
| lucidchart-to-brief | Read a Lucidchart URL through the configured MCP and turn the business diagram into a factual brief and open questions; do not invent technical architecture. |

## Install for your user (Linux/macOS)

Clone once:

```bash
git clone https://github.com/laurentcharbonnel/architecture-skills.git
cd architecture-skills
mkdir -p ~/.claude/skills
cp -R skills/architecture-design ~/.claude/skills/
cp -R skills/lucidchart-to-brief ~/.claude/skills/
```

If either destination already exists, compare or back it up before copying.
Open Claude Code in your project and invoke `/architecture-design` or `/lucidchart-to-brief`.
To update, run `git pull --ff-only` in this clone and repeat the copies after reviewing local changes.
For project-only installation, copy into the project's `.claude/skills/` instead.

Optional delegation: copy the two files in `claude-agents/` into `~/.claude/agents/` (or the project's `.claude/agents/`). Check them with `/agents`. Skills work without these agents. Model aliases resolve according to your Claude Code environment; availability and usage limits still apply.

## Lucidchart prerequisite

Configure and authorize your Lucidchart MCP in Claude Code before passing a document URL. The skill discovers its actual read tools; it does not assume server-specific names or install/authenticate a server. A supplied export is a fallback when access or capabilities are insufficient.

## Architecture resources and project separation

The architecture-design folder includes its templates and references, so copying that folder preserves the workflow. Load only the resource needed for the current artifact.
Keep project artifacts in their own repository, for example `high-level-design/`, `low-level-design/`, `decisions/` and `interview/state.md`; retain existing layouts when present.
Configure the external shared standards path once in that checkpoint. Use the bundled standard template for proposals; no enterprise standard is pre-approved here.
Keep frontend/backend implementation repositories separate where project policy requires it.

## Working agreement

- Discuss changes in batches. Keep a short list of validated decisions and open points; write to this repository when the user says “save”.
- Keep instructions precise and brief; load only relevant references and file sections.
- Ask at most 3–4 related questions per turn; reuse approved answers and standards.
- Update only affected artifacts. Do not regenerate the whole specification.
- Save a compact project checkpoint after meaningful steps and before handoff or compaction.
- Keep the architect responsible for decisions; record assumptions and provisional choices explicitly.
- Prefer direct execution for small tasks. Use Haiku for bounded extraction/checking and Opus for difficult tradeoffs; no automatic fan-out.
- Keep orchestration guidance as a reference, not a third skill or a runtime supervisor.
- Write professional artifacts in English; converse in the user's preferred language.

## Validation and limits

Before publishing a revision, check frontmatter, names, reference paths, installation structure, and start/resume/change scenarios. Test in Claude Code on a representative case before relying on the skills at work. Structural checks alone do not prove model behavior or token savings.
No exact context monitor, automatic process termination, automatic model switching in the main session, or measured savings are provided.

## Sources

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)

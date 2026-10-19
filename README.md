# Verification kit for Claude Code

AI answers sound equally sure whether they are right or wrong. This kit makes Claude show its work: where a claim comes from, whether the source really says it, and where a person has to decide.

It is four small pieces you add to [Claude Code](https://claude.com/claude-code):

| Piece | What it does | How you use it |
|---|---|---|
| `skills/why-chain/` | Asks "why is that true, and how do we know?" until every step ends in a measured fact, a definition, or "unknown." Flags circular reasoning, and marks citations it hasn't checked as UNCHECKED. | Type "why-chain this" after any answer. |
| `agents/research-verify.md` | Checks one factual claim against primary sources and returns a verdict, its evidence, and a confidence level | Ask: "use research-verify to check: …" |
| `rules/CONFIRM-BEFORE-ACTING.md` | Standing rules: confirm facts at their source before building on them; stop when something can't be confirmed; drafts, not actions | Paste into your `CLAUDE.md` |
| `hooks/settings-snippet.json` | A reminder that runs on every message, so the checking happens even when you forget to ask | Merge into `~/.claude/settings.json` |

## Install

1. Install Claude Code, if you haven't: https://claude.com/product/claude-code has the current instructions.
2. From this folder, run:

   ```
   python3 install.py
   ```

   It creates `~/.claude/skills/` and `~/.claude/agents/` if they are missing, copies the skill and the agent there, and adds the reminder hook to `~/.claude/settings.json` without disturbing anything already in that file. `python3 install.py --dry-run` shows the plan first. Python 3.8 or newer; standard library only.
3. Paste the rules you want from `rules/CONFIRM-BEFORE-ACTING.md` into `~/.claude/CLAUDE.md`. Create the file if it doesn't exist. The installer leaves this file alone on purpose: it is yours.
4. Start a new Claude Code session. The skill and the agent load at startup.

### By hand, if you prefer

```
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R skills/why-chain ~/.claude/skills/why-chain
cp agents/research-verify.md ~/.claude/agents/research-verify.md
```

Then the hook. If `~/.claude/settings.json` does not exist, copy `hooks/settings-snippet.json` to that path. If it does exist, open it and add the `"UserPromptSubmit"` entry from the snippet inside its `"hooks"` object (create `"hooks"` if there isn't one), keeping everything else as it is.

## What it costs

The fact-checking agent reads full papers, not just abstracts, so it is slow and uses real model capacity. In testing, one check read three full papers and took about 15 minutes at the maximum reasoning-effort setting. Save it for claims that matter. The why-chain skill is much faster; in testing it took about two and a half minutes at the same setting, and less at lower effort.

## What it can't do

- It does not make the AI right. It makes the AI say what it knows, how it knows it, and what it doesn't know.
- It is only as good as the sources it can reach. Paywalled papers are flagged, not read.
- A person still decides. For medical, legal, or financial questions, the verdict is something to bring to a professional, not a replacement for one.

## Origin

Built and used daily by its author while studying biochemistry and building AI tools. The validity check in the why-chain skill was added after a real error: a correctly sourced fact sitting inside an invalid inference.

## License

MIT. See `LICENSE`.

#!/usr/bin/env python3
"""Install the verification kit into Claude Code's user folder (~/.claude by default).

    python3 install.py            # install
    python3 install.py --dry-run  # show what would change
    python3 install.py --home /some/dir   # use another folder (for testing)

What it does, and nothing more:
  1. creates <home>/skills and <home>/agents if missing;
  2. copies skills/why-chain/ and agents/research-verify.md there (overwriting older copies of the same files);
  3. adds the reminder hook to <home>/settings.json, keeping everything already in that file;
  4. prints where the rules file is, for you to paste into <home>/CLAUDE.md yourself.
Standard library only.
"""
import argparse, json, pathlib, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent

def merge_hook(settings_path, hook_entry, dry_run):
    data = {}
    if settings_path.exists():
        try:
            data = json.loads(settings_path.read_text(encoding="utf-8") or "{}")
        except json.JSONDecodeError as e:
            sys.exit(f"{settings_path} is not valid JSON ({e}); fix it or move it aside, then rerun.")
        if not isinstance(data, dict):
            sys.exit(f"{settings_path} does not hold a JSON object; not touching it.")
    hooks = data.setdefault("hooks", {})
    lst = hooks.setdefault("UserPromptSubmit", [])
    wanted = hook_entry["hooks"][0]["command"]
    for entry in lst:
        for h in entry.get("hooks", []):
            if h.get("command") == wanted:
                return "already present"
    lst.append(hook_entry)
    if not dry_run:
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        settings_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return "added"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--home", default=str(pathlib.Path.home() / ".claude"), help="Claude Code user folder (default ~/.claude)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan; change nothing")
    a = ap.parse_args()
    home = pathlib.Path(a.home).expanduser()
    skill_src, agent_src = HERE / "skills" / "why-chain", HERE / "agents" / "research-verify.md"
    for p in (skill_src / "SKILL.md", agent_src, HERE / "hooks" / "settings-snippet.json"):
        if not p.exists(): sys.exit(f"missing {p}; run this from the kit's folder")
    skill_dst, agent_dst = home / "skills" / "why-chain", home / "agents" / "research-verify.md"
    print(("would copy" if a.dry_run else "copying"), skill_src.relative_to(HERE), "->", skill_dst)
    print(("would copy" if a.dry_run else "copying"), agent_src.relative_to(HERE), "->", agent_dst)
    if not a.dry_run:
        skill_dst.parent.mkdir(parents=True, exist_ok=True); agent_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(skill_src, skill_dst, dirs_exist_ok=True); shutil.copy2(agent_src, agent_dst)
    snippet = json.loads((HERE / "hooks" / "settings-snippet.json").read_text(encoding="utf-8"))
    entry = snippet["hooks"]["UserPromptSubmit"][0]
    result = merge_hook(home / "settings.json", entry, a.dry_run)
    print(("hook:" if not a.dry_run else "hook would be:"), result, "in", home / "settings.json")
    print("rules: paste what you want from", HERE / "rules" / "CONFIRM-BEFORE-ACTING.md", "into", home / "CLAUDE.md")
    print("then start a new Claude Code session.")

if __name__ == "__main__":
    main()

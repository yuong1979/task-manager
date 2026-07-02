# Agent Instructions — Task Manager Tutorial

This project follows a 12-phase full-cycle tutorial for building a Task Manager web app (Flask + React).

## Session Start

At the start of every session, you MUST read both of these files:

1. **`project-lifecycle.md`** — Contains the full-cycle workflow overview, architecture, and phase descriptions.
2. **`todo.md`** — Contains the granular checklist with checkboxes. This is the source of truth for what's been done and what's next.

After reading them, determine:
- Which phase we're currently in (find the first unchecked item)
- What the previous session accomplished
- What the next actionable step is

## Workflow

Follow the phases sequentially. Do not skip ahead. If the user asks to jump phases, confirm it's intentional.

## Headroom Proxy

This project uses Headroom as a context-compression proxy between OpenCode and
OpenRouter. Read `headroom-setup.md` for full setup details, architecture, and
troubleshooting.

### Session Start
Check if Headroom is running:
```bash
python3 -c "
import urllib.request
try:
    r = urllib.request.urlopen('http://127.0.0.1:8787/livez', timeout=3)
    print('Headroom is running')
except:
    print('Headroom is DOWN')
    exit(1)
"
```
If DOWN, start it:
```bash
bash start-headroom.sh
```

### Key Facts (for the agent)
- Headroom runs on port 8787, bound to 0.0.0.0
- Only the `openrouter` provider routes through Headroom (set in
  `opencode.jsonc`). The `opencode` (Zen) provider bypasses it.
- Use `--model openrouter/deepseek/deepseek-v4-flash` to go through Headroom
- Deps live in `/tmp/headroom_deps/` — `/tmp` gets wiped, so `start-headroom.sh`
  must be re-run after a wipe
- Two common failure modes: missing numpy (install it) or transformers runtime
  dep check (run `patch-transformers.py`)
- View live requests: `tail -f /tmp/headroom-stderr.log`

## Tone

Concise, practical. No unnecessary explanations.

# Headroom Setup & Known Issues

Created: 2026-07-02
Purpose: Reference doc for Headroom context compression proxy.

## Current Status

Headroom is running on PID 7 with command:
```
/opt/venv/bin/python3 /opt/venv/bin/headroom proxy --port 8787 --host 0.0.0.0 --backend openrouter
```

It proxies requests to OpenRouter successfully (HTTP 200). However, token savings are effectively zero in practice.

## Known Issues (revisit later)

### Issue 1: Compression inflation (no token savings)

Every request either shows `tok_saved=0` or the pipeline inflates tokens:

```
Optimization inflated tokens (13080 -> 13968), reverting to original messages
```

Root cause: Pipeline overhead (CCR markers, CacheAligner tail, restructuring) exceeds savings on small-to-medium conversations (~13k-23k tokens). Headroom's safety mechanism detects this and reverts.

Reference: `/workspace/archive/headroom-issues.md` — Issues 5-6 document this thoroughly.

### Issue 2: No compression env vars set

The process env has no compression-related variables. Last session had these working:
- `HEADROOM_COMPRESS_USER_MESSAGES=true`
- `HEADROOM_SAVINGS_PROFILE=balanced`

But they weren't persisted across restarts.

### Issue 3: Savings history permission denied

```
Failed to save savings history to /home/user/.headroom/proxy_savings.json: Permission denied
```

Root cause: Docker uid mismatch. Process runs as `node` (uid 1000) but `/home/user/.headroom` is owned by `user` (uid 1002). Non-blocking since savings are always 0 anyway.

### Fix Plan (when revisited)

Apply conservative profile and fix permissions:
```
HEADROOM_LOSSLESS_ONLY=1
HEADROOM_MIN_TOKENS_TO_COMPRESS=500
HEADROOM_COMPRESS_USER_MESSAGES=true
chown -R 1000:1000 /home/user/.headroom
```

See `/workspace/archive/headroom-issues.md` Issue 6 for detailed proposed solutions.

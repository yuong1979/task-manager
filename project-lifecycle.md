# Project Lifecycle - Full Cycle Management

## Standard Files in a Project Root for Full-Cycle Management

### Root-level config files (machine-readable)

| File | Purpose |
|------|---------|
| `README.md` | Setup, run, deploy instructions |
| `CHANGELOG.md` | Auto-generated from conventional commits |
| `CONTRIBUTING.md` | Branch strategy, commit format, PR process |
| `LICENSE` | Licensing terms |
| `.github/workflows/` | CI/CD pipeline definitions |
| `.husky/` | Git hooks config |
| `package.json` / `pyproject.toml` | Scripts for each cycle step |
| `.env.example` | Documented required env vars |
| `docker-compose.yml` | Local dev environment |
| `Makefile` or `Taskfile.yml` | Shorthand for common commands (lint, test, build, deploy) |

### Docs folder (`docs/`)

| File | Purpose |
|------|---------|
| `docs/architecture.md` | ADRs, data model, key decisions |
| `docs/specs.md` or `docs/requirements.md` | User stories, acceptance criteria |
| `docs/api.md` | Endpoint contracts |
| `docs/deployment.md` | Deploy steps, rollback procedure |
| `docs/monitoring.md` | Alerts, dashboards, SLIs |

### Minimal viable set (simpler projects)

```
README.md
CHANGELOG.md
CONTRIBUTING.md
.env.example
.github/workflows/ci.yml
```

## Solo AI-Assisted Full-Cycle Workflow (Recommended)

### The Forward Flow (ideal path)

1. **Plan** — Describe feature to AI, generate spec + acceptance criteria in docs/specs.md
2. **Branch** — git checkout -b feat/<name> from main
3. **Code** — AI generates implementation. Linter/formatter runs on save (editor auto)
4. **Tests** — AI writes unit/integration tests alongside code. Run locally once before push
5. **Push** — git push, open a PR
6. **CI (auto)** — lint → type check → unit tests → integration tests → build
7. **Preview deploy (auto)** — CI deploys branch to staging URL. AI agent runs automated smoke check (e.g., browser-use, Playwright + LLM)
8. **Merge to main** — CI gates must be green
9. **CD (auto)** — merge triggers production deploy
10. **Post-deploy smoke (auto)** — AI agent or script hits production URL, checks critical paths
11. **Repeat** — back to step 1

### Feedback Loops (when things go wrong)

Each stage can reject the current state and loop back to an earlier step:

| Failure at | Loop back to | What to do |
|------------|-------------|------------|
| CI (lint/typecheck) | Step 3 (Code) | Fix formatting or types, push again |
| CI (unit/integration test) | Step 4 (Tests) | Fix broken test or the code it tests, push again |
| Preview smoke check | Step 3 (Code) | Fix the issue, push again, re-trigger CI + preview |
| Code review (logic/design) | Step 1 (Plan) or Step 3 (Code) | Revisit spec or rewrite implementation |
| Post-deploy smoke | Step 3 (Code) → hotfix branch | Rollback previous deploy, fix on a branch, push + merge |
| Production bug discovered later | Step 1 (Plan) | New feature branch with the fix, full cycle repeats |

### Key Principle

Each gate (CI, preview, code review) exists precisely to catch failures early. The further downstream a failure is caught, the more expensive it is to fix. The loops get shorter and cheaper the earlier you catch them.

---

## Full-Cycle Tutorial: Task Manager Web App

A hands-on walkthrough covering all lifecycle phases using a simple Task Manager (Flask + SQLite → Supabase, Railway deploy, Vercel frontend).

### Prerequisites (set these up before starting)

| Resource | Purpose | Signup link | Free tier? |
|----------|---------|-------------|------------|
| GitHub account | Repository, CI/CD (GitHub Actions), PR management | github.com | Yes |
| Railway account | Backend hosting, preview deploys, CD | railway.com | Yes (free tier) |
| Supabase account | Production database (PostgreSQL) | supabase.com | Yes (free tier) |
| Vercel account | Frontend hosting | vercel.com | Yes (free tier) |
| Python 3.10+ | Local development | python.org | Free |
| Node.js 18+ | Frontend tooling (Vite) | nodejs.org | Free |
| Git | Version control | git-scm.com | Free |
| OpenCode / Claude Code | AI-assisted dev throughout all phases | — | — |

Recommended: have these accounts created and a new GitHub repo initialized before starting.

### Tutorial Phases (12 phases)

| # | Phase | Key Activities |
|---|-------|----------------|
| 1 | Plan | Write spec doc, user stories, acceptance criteria, data model |
| 2 | Setup | Project structure, docs folder, env files, Makefile, PR template |
| 3 | Migrations | Alembic setup, initial schema, seed data, versioned migrations |
| 4 | Branch | Feature branching, conventional commits, PR template |
| 5 | Code | Build the app (AI generates, you review and approve) |
| 6 | Test | Unit + integration tests, run locally, coverage report |
| 7 | CI | GitHub Actions: lint → typecheck → test → build |
| 8 | Preview | Railway staging deploy per branch, live URL |
| 9 | Debug loop | Deliberate bug → CI fails → AI reads logs → fix → re-deploy |
| 10 | Rollback | Deploy bad code, git revert, re-deploy to production |
| 11 | CD | Merge to main → auto-deploy to production (Railway) |
| 12 | Post-deploy | AI smoke test, log review, monitoring setup |

### How to Start

Open a terminal in the project directory and run:

```
bash start_full_cycle_tutorial.sh
```

The script will guide you through each phase interactively with AI assistance. Your role: review, approve, supervise. AI does the implementation.

---

## Task Manager — Full-Cycle Tutorial Checklist

### Architecture Overview
- Backend: Flask REST API (Python)
- Database (dev): SQLite
- Database (prod): Supabase (PostgreSQL)
- Database migrations: Alembic
- Frontend: React + Vite (JavaScript)
- CI/CD: GitHub Actions
- Hosting (backend): Railway
- Hosting (frontend): Vercel
- AI assistant: OpenCode / Claude Code

### Phase 0 — Prerequisites (done before tutorial)
- [ ] GitHub account created
- [ ] Railway account created (free tier)
- [ ] Supabase account created (free tier)
- [ ] Vercel account created (free tier)
- [ ] Python 3.10+ installed
- [ ] Node.js 18+ installed
- [ ] Git installed and configured
- [ ] New empty GitHub repo initialized (e.g., task-manager)
- [ ] GitHub repo cloned locally

### Phase 1 — Plan
- [ ] 1.1 — Write docs/spec.md: one-paragraph product description
- [ ] 1.2 — Define 3-5 user stories
- [ ] 1.3 — Define acceptance criteria per user story
- [ ] 1.4 — Design the data model
- [ ] 1.5 — Define REST API endpoints (GET/POST/PUT/DELETE /api/tasks)
- [ ] 1.6 — Define frontend routes/pages
- [ ] 1.7 — Write docs/architecture.md: ADR for stack choices

### Phase 2 — Setup
- [ ] 2.1 — Create backend directory structure (backend/app/, backend/tests/)
- [ ] 2.2 — Create backend/requirements.txt
- [ ] 2.3 — Create backend/.env.example
- [ ] 2.4 — Create Flask app factory stub in backend/app/__init__.py
- [ ] 2.5 — Create config classes in backend/app/config.py
- [ ] 2.6 — Create SQLAlchemy Task model in backend/app/models.py
- [ ] 2.7 — Create backend/Makefile (install, run, test, lint, migrate targets)
- [ ] 2.8 — Install Python dependencies
- [ ] 2.9 — Scaffold frontend with Vite + React
- [ ] 2.10 — Add frontend/Makefile
- [ ] 2.11 — Create .gitignore
- [ ] 2.12 — Create root Makefile
- [ ] 2.13 — Configure linter (Ruff)
- [ ] 2.14 — Create CONTRIBUTING.md
- [ ] 2.15 — Create .github/PULL_REQUEST_TEMPLATE.md
- [ ] 2.16 — Make initial git commit and push to main

### Phase 3 — Migrations
- [ ] 3.1 — Initialize Alembic in backend/
- [ ] 3.2 — Configure alembic.ini for SQLite
- [ ] 3.3 — Write initial migration: create tasks table
- [ ] 3.4 — Run migration, verify table
- [ ] 3.5 — Create seed data script (backend/seed.py)
- [ ] 3.6 — Add migration targets to backend/Makefile
- [ ] 3.7 — Commit migration + seed script

### Phase 4 — Branch
- [ ] 4.1 — Create feat/task-crud branch from main
- [ ] 4.2 — Explain conventional commit format
- [ ] 4.3 — Push branch, open draft PR against main

### Phase 5 — Code
- [ ] 5.1 — Implement Flask app factory
- [ ] 5.2 — Implement config classes (dev/prod)
- [ ] 5.3 — Implement SQLAlchemy models
- [ ] 5.4 — Implement CRUD routes (app/routes/tasks.py)
- [ ] 5.5 — Implement error handlers (404, 400, 500)
- [ ] 5.6 — Wire up CORS
- [ ] 5.7 — Create run.py entrypoint
- [ ] 5.8 — Test API manually (curl/httpie)
- [ ] 5.9 — Create React app shell with router
- [ ] 5.10 — Create TaskList component
- [ ] 5.11 — Create TaskForm component
- [ ] 5.12 — Create TaskItem component
- [ ] 5.13 — Style with basic CSS
- [ ] 5.14 — Test frontend talks to backend (dev mode)
- [ ] 5.15 — Commit all, push to feat/task-crud

### Phase 6 — Test
- [ ] 6.1 — Write unit tests for models
- [ ] 6.2 — Write unit tests for routes
- [ ] 6.3 — Write test fixtures (test client, test DB)
- [ ] 6.4 — Run tests locally, all pass
- [ ] 6.5 — Commit tests, push to feat/task-crud

### Phase 7 — CI
- [ ] 7.1 — Create .github/workflows/ci.yml
- [ ] 7.2 — Job: lint (ruff check)
- [ ] 7.3 — Job: type check (mypy)
- [ ] 7.4 — Job: test (pytest with SQLite)
- [ ] 7.5 — Job: build (pip install check)
- [ ] 7.6 — Push, verify CI runs green on the PR

### Phase 8 — Preview (Staging Deploy)
- [ ] 8.1 — Add backend/Procfile for Railway
- [ ] 8.2 — Add backend/railway.json config
- [ ] 8.3 — Connect Railway project to GitHub repo
- [ ] 8.4 — Configure Railway to deploy the backend/ directory
- [ ] 8.5 — Configure Railway environment variables
- [ ] 8.6 — Trigger preview deploy from PR branch
- [ ] 8.7 — Verify Railway staging URL is live
- [ ] 8.8 — Connect Vercel project to GitHub
- [ ] 8.9 — Configure Vercel with backend staging URL
- [ ] 8.10 — Deploy frontend preview, test end-to-end

### Phase 9 — Debug Loop
- [ ] 9.1 — Introduce deliberate bug into the code
- [ ] 9.2 — Push bug, watch CI fail
- [ ] 9.3 — Read CI logs, identify the failure
- [ ] 9.4 — Fix the bug, push again
- [ ] 9.5 — Confirm CI passes, preview green

### Phase 10 — Rollback
- [ ] 10.1 — Deploy a bad change to production (simulated)
- [ ] 10.2 — Identify the failure
- [ ] 10.3 — git revert the bad commit
- [ ] 10.4 — Push revert, verify CI + deploy
- [ ] 10.5 — Document the rollback

### Phase 11 — CD (Continuous Deploy)
- [ ] 11.1 — Configure Railway: auto-deploy on push to main
- [ ] 11.2 — Configure Vercel: auto-deploy on push to main
- [ ] 11.3 — Merge feat/task-crud PR to main
- [ ] 11.4 — Verify Railway auto-deploys backend
- [ ] 11.5 — Verify Vercel auto-deploys frontend
- [ ] 11.6 — Test production URLs end-to-end

### Phase 12 — Post-Deploy
- [ ] 12.1 — Write automated smoke test script
- [ ] 12.2 — Add smoke test to CI/CD post-deploy step
- [ ] 12.3 — Set up Railway dashboard alerts
- [ ] 12.4 — Set up uptime monitoring (e.g., Upptime, Better Uptime)
- [ ] 12.5 — Write docs/monitoring.md
- [ ] 12.6 — Final review: document remaining todos/issues

### Completion
- [ ] All 12 phases complete
- [ ] Production app is live and tested
- [ ] Monitoring and alerts configured
- [ ] You understand the full lifecycle from plan to post-deploy
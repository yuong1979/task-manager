# Architecture Decision Record

## Stack Choices

### Backend: Flask (Python)
- **Why**: Lightweight, minimal boilerplate, well-suited for simple REST APIs. The tutorial scope (CRUD + migrations) doesn't warrant Django's overhead.
- **Alternative considered**: FastAPI — faster async performance but adds complexity for this scope.

### Database (dev): SQLite
- **Why**: Zero-config, file-based, perfect for local development. No server process needed.
- **Production**: Supabase PostgreSQL — managed, free tier, supports Alembic migrations.

### ORM: SQLAlchemy + Alembic
- **Why**: Industry standard for Python DB access. Alembic provides versioned migrations that work with both SQLite and PostgreSQL.

### Frontend: React + Vite
- **Why**: Vite is the standard React build tool (fast HMR, simple config). React is the most widely used frontend framework.

### Hosting (backend): Railway
- **Why**: Simple GitHub-connected deploys, free tier, supports Dockerfile and Procfile.

### Hosting (frontend): Vercel
- **Why**: Native React/Vite support, auto-deploys from GitHub, generous free tier.

### CI/CD: GitHub Actions
- **Why**: Free for public/private repos, tight GitHub integration, large ecosystem of actions.

## Key Decisions

1. **No auth in v1** — Skipping user auth keeps the scope focused on CRUD + deployment lifecycle. Can add later.
2. **Monorepo structure** — Backend and frontend in one repo under `backend/` and `frontend/` directories. Simplifies CI and repo management.
3. **Dev database only** — Phase 3 targets SQLite. Supabase migration is a later-phase enhancement.
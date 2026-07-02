# Contributing

## Branch Strategy

- `main` — production-ready code
- `feat/<name>` — feature branches off main
- `fix/<name>` — bugfix branches off main

## Commit Format

Use conventional commits:

```
<type>: <description>

feat: add task CRUD endpoints
fix: handle empty title validation
docs: add API docs
```

Types: `feat`, `fix`, `docs`, `chore`, `test`, `refactor`.

## PR Process

1. Create branch from main
2. Commit with conventional format
3. Push and open PR against main
4. Ensure CI passes
5. Request review if pair programming
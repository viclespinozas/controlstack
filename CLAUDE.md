# ControlStack: guidance for Claude

Personal finance API built with FastAPI, PostgreSQL and JWT. This is the owner's real Python project. They want to understand the whole stack and be able to explain it in interviews.

## How we work
- **The owner writes the code.** Claude explains concepts, reviews what was written and says what to improve. Don't write the solution unless asked.
- Claude handles the non-code work: Trello updates, `CLAUDE.md`, `CONTEXT.md`, `HISTORY.md`, and git and PR mechanics when asked.
- One card at a time. Keep at most one card in Doing. Only mark a card done when the owner says so.
- Review against the card's "Done when" and "Be ready to explain" sections.
- After each finished card, update `CONTEXT.md`, add a "Here's what landed" entry to `HISTORY.md`, and update this file if a convention changed.
- Each `HISTORY.md` entry records the time spent on the card, and the time log table at the top gets a new row. Use the session's message timestamps for session time and Trello for Doing → Done. Count solo time only when a timestamp proves it, such as a commit, an image build or a file's modified time.

## Stack
- Python 3.12, FastAPI, Pydantic v2
- SQLAlchemy 2 (async) with asyncpg, Alembic
- PostgreSQL 16 and the API both run through Docker Compose
- Planned: JWT auth, argon2 hashing, pytest, GitHub Actions with Ruff

## Commands
```bash
make build   # build the images (needed after changing requirements.txt)
make up      # start the API and Postgres in the background
make down    # stop them
make logs    # follow API logs
make shell   # open a shell in the API container
docker compose up -d --wait   # start both and wait for healthchecks to pass
docker compose ps    # check container health
```

The API runs at http://localhost:8000, with interactive docs at `/docs`. Only Postgres has a healthcheck, so use `GET /health` to check the API.

## Layout
- `main.py`: app entry point and router registration
- `routes/`: HTTP endpoints
- `services/`: business logic
- `repositories/`: data access
- `models/`: database models
- `schemas/`: request and response validation
- `core/`: configuration and database setup
- `alembic/`, `alembic.ini`: migrations

## Rules
- Settings come from environment variables. Never hardcode secrets. `.env` is gitignored and `.env.example` is committed.
- Read the migration SQL before applying it.
- Money uses `Numeric` and `Decimal`, never float.
- Every transaction query is scoped to the current user. Another user's record returns 404, not 403.

## Docs
- `CONTEXT.md`: current state, next step and open decisions. Read this first in a new session.
- `HISTORY.md`: local study log of what landed and why. It is gitignored, so never commit it.
- `README.md`: public project description.

## Task tracking
Trello board: https://trello.com/b/e41OyIBt/controlstack-fastapi-postgres-jwt

The board is the source of truth for cards and points. The original plan is `~/Downloads/CONTROLSTACK_STATUS.md`, but its order and points are out of date.

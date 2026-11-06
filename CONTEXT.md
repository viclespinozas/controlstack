# Context: where the project stands

Last updated: Fri Nov 6, 2026. The compose card is done, and the config split card is in Doing. The latest code commit is `09b1f79`.

Branch: `refactor/migrate-data-layer-from-mongodb-to-postgresql`, in draft [PR #5](https://github.com/viclespinozas/controlstack/pull/5). GitHub has the latest commit, but the local branch has no upstream set, so `git push` needs `-u` the first time.

## What exists
| Piece | State |
| --- | --- |
| `docker-compose.yml` | Postgres 16 with a working healthcheck. The API waits for a healthy database. No Mongo blocks left |
| `.env.example` | Committed. It lists `DATABASE_URL`, `POSTGRES_USER`, `POSTGRES_PASSWORD` and `POSTGRES_DB` |
| `Makefile` | `make logs` now targets `api`. The stale `alembic_init` target is still there |
| `core/config.py` | Mixes the engine, session, `Base`, `get_db` and leftover Mongo settings |
| `core/database.py` | Still the Mongo (`motor`) client |
| `GET /health` | Works against Postgres |
| `/transactions` | Still Mongo code. It can't work because compose has no Mongo |
| `Transaction` | Pydantic class with only `id`, `name`, `description` |
| Roles | Model, schema, repository and routes exist, but the router isn't registered and `relationship("UserRole")` is broken |
| Alembic | Initialised with the sync template, needs redoing as async. No migrations |

## What does not exist yet
- Auth, users and JWT
- Tests and CI
- A self-contained Docker image (the `COPY` line is commented out)

The README still describes the Mongo version. That gets fixed on the Block 4 README card.

## Verified
Checked on Nov 6 against the running containers:
- Postgres reports healthy, and `psql` connects inside its container
- `GET /health` returns `{"status":"connected"}`
- The API logs show up through `docker-compose logs api`, the command behind `make logs`
- The packages installed in the API image match `requirements.txt` for `sqlalchemy`, `asyncpg`, `alembic` and `motor`

Not verified:
- **Fresh clone using only `.env.example`.** This is the one "Done when" item on the compose card nobody has run.
- **API health in Docker.** The `api` service has no healthcheck, so `up --wait` printing "Healthy" for it doesn't test the app. `GET /health` is the real check.

## Next
Config split card, in Doing:
1. Add `pydantic-settings` to `requirements.txt` and rebuild. The current image dates from June 4, so this is also the first rebuild since then.
2. Write `Settings` in `core/config.py`, with `DATABASE_URL` required and SQL logging controlled by an env var.
3. Move the engine, session factory, `Base` and `get_db` into `core/database.py`.
4. Keep the Mongo client and settings, marked `TEMP`.

## Small leftovers
- **`POSTGRES_USER` is unused.** `.env` and `.env.example` set it, but compose hardcodes `postgres` in the service, `DATABASE_URL` and `pg_isready`. Use the variable everywhere or drop it. Fold this into the next commit.
- **Compose warns that `POSTGRES_*` variables aren't set.** Line 1 of the local `.env` uses them in `DATABASE_URL` before they're defined. The values still resolve, so it's only noise. A test with fake values showed that moving `DATABASE_URL` to the last line stops the warnings.
- **The PR #5 description is ahead of the code.** It says Mongo dependencies and repository patterns are removed, but `motor` and the Mongo repository are still there until the Transaction card. Fix this before taking the PR out of draft.

## Plan
| Block | Due | Points | Cards, in order |
| --- | --- | --- | --- |
| 1: Finish the migration | Sun Nov 15 | 14 (12 left) | ~~Compose (2)~~, config split (2), Roles (1), Alembic (2), Transaction (5), per-request `Depends` (2) |
| 2: Auth and ownership | Sun Nov 29 | 11 | User model (3), register and token (3), `get_current_user` (2), scope queries (3) |
| 3: Tests and CI | Sun Dec 13 | 15 | Test setup (5), tests (3), pagination (2), errors (3), GitHub Actions (2) |
| 4: Signal | Sun Dec 20 | 7 | Dockerfile (2), README (2), interview drill (3) |

Total: 47 points, 2 done. The pace target is about 8 points a week, so the 12 left in Block 1 are tight for the 9 days to Nov 15.

## Open decisions
- **Roles:** delete (the card's default, 1 point) or keep (closer to 3 points). Decide before the Alembic card.
- **Where `commit` lives:** repository, service or a shared unit of work. Decide on the `Depends` card.

## Sequencing to remember
- Don't remove `motor` until the Transaction card, because the transaction routes still import it.
- The config split must keep the Mongo client and settings, marked `TEMP`, because `transaction_repo.py` still imports them. The Transaction card removes them.
- Transaction and per-request `Depends` go together, because a SQLAlchemy repository needs a session per request.
- `user_id` and its index are added on the Block 2 User card, because the `users` table doesn't exist before then.

# Context: where the project stands

Last updated: Thu Nov 5, 2026, with the compose card in Doing. The latest commit is `a82059d`.

Branch: `refactor/migrate-data-layer-from-mongodb-to-postgresql`. It's on GitHub, but the local branch has no upstream set, so the first push needs `git push -u`.

## What exists
| Piece | State |
| --- | --- |
| `docker-compose.yml` | Postgres 16 replaced Mongo. The API waits for a healthy database, but the healthcheck looks broken |
| `core/config.py` | Mixes the engine, session, `Base`, `get_db` and leftover Mongo settings |
| `core/database.py` | Still the Mongo (`motor`) client |
| `GET /health` | Written against Postgres, not run yet |
| `/transactions` | Still Mongo code. It can't work because compose has no Mongo |
| `Transaction` | Pydantic class with only `id`, `name`, `description` |
| Roles | Model, schema, repository and routes exist, but the router isn't registered and `relationship("UserRole")` is broken |
| Alembic | Initialised with the sync template, needs redoing as async. No migrations |

## What does not exist yet
- `.env.example`
- Auth, users and JWT
- Tests and CI
- A self-contained Docker image (the `COPY` line is commented out)

The README still describes the Mongo version. That gets fixed on the Block 4 README card.

## Verified
Nothing has been run yet. Everything above comes from reading the code. The healthcheck bug is unconfirmed until `make up` runs.

## Next
Finish the compose card:
1. Fix the healthcheck
2. Add `.env.example`, and use or remove `POSTGRES_USER`
3. Fix the Makefile `logs` target (`backend` should be `api`)
4. Delete the commented-out Mongo blocks from compose

Don't remove `motor` on this card. The transaction routes still import it, so that moved to the Transaction card.

## Plan
| Block | Due | Points | Cards, in order |
| --- | --- | --- | --- |
| 1: Finish the migration | Sun Nov 15 | 14 | Compose (2), config split (2), Roles (1), Alembic (2), Transaction (5), per-request `Depends` (2) |
| 2: Auth and ownership | Sun Nov 29 | 11 | User model (3), register and token (3), `get_current_user` (2), scope queries (3) |
| 3: Tests and CI | Sun Dec 13 | 15 | Test setup (5), tests (3), pagination (2), errors (3), GitHub Actions (2) |
| 4: Signal | Sun Dec 20 | 7 | Dockerfile (2), README (2), interview drill (3) |

Total: 47 points. The pace target is about 8 points a week, so Block 1 is tight.

## Open decisions
- **Roles:** delete (the card's default, 1 point) or keep (closer to 3 points). Decide before the Alembic card.
- **Where `commit` lives:** repository, service or a shared unit of work. Decide on the `Depends` card.

## Sequencing to remember
- The config split must keep the Mongo client and settings, marked `TEMP`, because `transaction_repo.py` still imports them. The Transaction card removes them.
- Transaction and per-request `Depends` go together, because a SQLAlchemy repository needs a session per request.
- `user_id` and its index are added on the Block 2 User card, because the `users` table doesn't exist before then.

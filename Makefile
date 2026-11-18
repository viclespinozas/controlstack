build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f api

shell:
	docker exec -it control_backend bash

alembic_init:
	docker-compose exec api alembic init alembic
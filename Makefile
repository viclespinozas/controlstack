build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f backend

shell:
	docker exec -it control_backend bash

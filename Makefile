COMPOSE := docker compose
WEB := $(COMPOSE) exec web

help:
	@echo "Available commands:"
	@echo "  make bash           - Open a shell inside the web container"
	@echo "  make superuser      - Create a Django superuser"
	@echo "  make lint           - Run Ruff linter"
	@echo "  make migrate        - Run makemigrations and migrate"
	@echo "  make test           - Run Django test suite"
	@echo "  make up             - Build and start all containers"
	@echo "  make down           - Stop and remove containers"

bash:
	$(WEB) bash

superuser:
	$(WEB) python manage.py createsuperuser

lint:
	$(WEB) ruff check .

migrate:
	$(WEB) python manage.py makemigrations
	$(WEB) python manage.py migrate

test:
	$(WEB) python manage.py test

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down

# Case Management System

This app includes a simple case management interface where users can upload and view files.
Uploads are stored in `MinIO`, which mimics `AWS S3`, and data is kept in a `PostgreSQL` database.

## Tech Stack

- Python / Django – core web framework
- PostgreSQL – relational database
- MinIO – local S3-compatible object storage
- Docker Compose – container orchestration
- Ruff – linting and code formatting

## Getting Started

Run the app in a docker container:
```
docker compose up --build
```

This will make the app available at `http://localhost:8000`.
MinIO’s console is available at `http://localhost:9001` (default login: minioadmin:minioadmin).

## Available URLs

| Path | Description |
|------|--------------|
| `/demo/hello` | Simple intro demo page |
| `/applications/submit` | Upload form for new applications |
| `/applications` | View a list of uploaded applications |
| `/admin/applications/application` | Django admin dashboard *(requires superuser)* |

## Commands

Access the docker container shell:
```
docker compose exec web bash
```
Apply migrations:
```
docker compose exec web python manage.py migrate
```
Create a superuser:
```
docker compose exec web python manage.py createsuperuser
```
Run the linter:
```
docker compose exec web ruff check .
```
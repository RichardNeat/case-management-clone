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
| `/` | Simple intro demo page |
| `/applications/submit` | Upload form for new applications |
| `/applications` | View a list of uploaded applications |
| `/admin` | Django admin dashboard *(requires superuser)* |

## Commands

This project has a `MakeFile` which exposes the following commands:

| Command | Description |
|----------|--------------|
| `make up` | Build and start all containers |
| `make down` | Stop and remove containers |
| `make bash` | Open an interactive shell in the web container |
| `make migrate` | Run `makemigrations` and `migrate` |
| `make superuser` | Create a Django superuser |
| `make lint` | Run Ruff linter |
| `make test` | Run Django tests |
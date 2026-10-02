# Makefile for personal diary application

.PHONY: build dev up down logs test lint typecheck verify backup restore clean help

# Build the Docker images
build:
	docker compose build

# Start the application in detached mode
up:
	docker compose up -d

# Stop the application
down:
	docker compose down

# View application logs
logs:
	docker compose logs -f

# Run tests
test:
	docker compose run --rm backend python -m pytest tests/

# Run linting
lint:
	docker compose run --rm backend ruff check .

# Run type checking
typecheck:
	docker compose run --rm backend mypy .

# Run all verification checks
verify: lint typecheck test

# Create backup
backup:
	docker compose run --rm backend python -m app.cli.backup

# Restore from backup (requires backup file as argument)
restore:
	docker compose run --rm backend python -m app.cli.restore $(backup_file)

# Clean up containers and volumes
clean:
	docker compose down -v

# Show help
help:
	@echo "Available commands:"
	@echo "  build     - Build Docker images"
	@echo "  up        - Start application"
	@echo "  down      - Stop application"
	@echo "  logs      - View application logs"
	@echo "  test      - Run tests"
	@echo "  lint      - Run linter"
	@echo "  typecheck - Run type checker"
	@echo "  verify    - Run all verification checks"
	@echo "  backup    - Create backup"
	@echo "  restore   - Restore from backup"
	@echo "  clean     - Clean up containers and volumes"
	@echo "  help      - Show this help"
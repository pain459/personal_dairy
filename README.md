# Personal Diary

A private, local diary application for recording thoughts and memories with photos.

## Features

- Calendar view with daily entries
- Rich text diary entries
- Photo upload and management
- Tags and mood tracking
- Search functionality
- Backup and export capabilities
- Responsive design with dark mode support

## Quick Start

```bash
git clone <repository>
cd personal_diary

cp .env.example .env

docker compose up -d --build
```

Then open http://localhost:8888

## Architecture

The application uses FastAPI for the backend and React with TypeScript for the frontend, all running in Docker containers.

## Data Storage

All data is stored locally on your machine:
- SQLite database for diary entries
- Local filesystem for photos
- Configuration in `.env`

## Privacy

Your diary is stored locally. No data leaves your machine unless you explicitly export it.
# Fibonacci Analytics Platform

Production style full stack platform for Fibonacci computation, benchmarking, analytics, and visualization.

## Stack

Backend:
- FastAPI
- Pydantic
- Uvicorn
- Pytest

Frontend:
- React
- TypeScript
- Vite
- Recharts

DevOps:
- Docker
- Docker Compose
- GitHub Actions

## Features

- Multiple Fibonacci algorithms
- Iterative
- Fast doubling
- Matrix exponentiation
- Continuous range generation
- Runtime benchmarking
- REST API
- Interactive dashboard
- Unit tests
- Health checks
- Type safe request and response models

## Repo layout

```text
fibonacci-analytics-platform/
  backend/
  frontend/
  .github/workflows/
  docker-compose.yml
```

## Local run

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Docker

```bash
docker compose up --build
```

Frontend runs on port 5173.
Backend runs on port 8000.

## API examples

```bash
curl "http://localhost:8000/api/v1/fibonacci?n=100&algorithm=fast_doubling"
curl "http://localhost:8000/api/v1/range?start=0&end=25&algorithm=matrix"
curl "http://localhost:8000/api/v1/benchmark?n=10000"
```

## Tests

```bash
cd backend
pytest
```

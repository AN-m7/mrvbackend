# MRV Backend Starter

A production-ready starter full-stack application with:
- Python FastAPI backend
- React + TypeScript frontend
- PostgreSQL database
- JWT authentication
- Dashboard with charts
- Admin CRUD panel
- Docker support for local runs

## Tech stack
- Backend: FastAPI, SQLAlchemy, PostgreSQL, JWT
- Frontend: React, TypeScript, Vite, Recharts
- Containerization: Docker Compose

## Project structure

```text
.
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   └── alembic.ini (optional future migrations)
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   ├── vite.config.ts
│   └── .env.example
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Quick start

### 1) Clone and configure environment

```bash
cp .env.example .env
```

### 2) Start with Docker Compose

```bash
docker compose up --build
```

This will start:
- PostgreSQL on http://localhost:5432
- Backend API on http://localhost:8000
- Frontend app on http://localhost:5173

### 3) Default login

```text
Email: admin@example.com
Password: admin123
```

## Backend setup manually

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend setup manually

```bash
cd frontend
npm install
cp .env.example .env
npm run dev -- --host 0.0.0.0
```

## API docs

Open:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Production notes
- Replace default JWT secret and admin credentials
- Use env-backed secrets in deployment
- Configure a real Postgres instance instead of local compose database
- Add HTTPS and reverse proxy in production environments

## Features included
- Secure login with JWT
- Role-based admin access
- Dashboard summary cards and chart data
- User management CRUD
- Product management CRUD
- Responsive UI and simple layout

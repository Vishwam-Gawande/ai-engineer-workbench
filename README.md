# AI Engineer Workbench

AI Engineer Workbench is a production-style AI engineering project built to explore modern LLM infrastructure and AI system design.

## Features

- FastAPI backend
- Modular API routers
- Centralized configuration management
- Structured logging
- Application lifecycle management
- Environment-based configuration
- Production-ready project structure

## Tech Stack

- Python
- FastAPI
- Pydantic Settings
- Uvicorn

## Project Structure

```
backend/
├── app/
│   ├── api/
│   ├── core/
│   └── main.py
├── requirements.txt
└── .env.example
```

## Running Locally

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

## License

MIT License
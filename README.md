# DT Office Assistant

An internal policy assistant for DT employees. The FastAPI backend answers policy questions using the documents in `data/knowledge` and can retrieve employee leave information from PostgreSQL. A lightweight browser frontend is served by the same FastAPI process.

## Features

- Ask questions about leave, travel and expenses, work from home, information security, and the employee handbook.
- Look up an employee's leave balance with an employee ID.
- Combine a policy answer with an employee's leave balance.
- Use the browser UI at `/` or the interactive API documentation at `/docs`.

## Requirements

- Python 3.12 or newer
- PostgreSQL with the employee and leave-balance tables
- Ollama running locally
- Ollama models `nomic-embed-text` and `qwen2.5:1.5b`

## Setup

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Update `.env` with the local PostgreSQL connection details. Do not commit `.env` or put credentials in `.env.example`.

Start Ollama and download the models:

```bash
ollama serve
ollama pull nomic-embed-text
ollama pull qwen2.5:1.5b
```

## Build the knowledge base

Place policy PDFs in `data/knowledge`, then run ingestion from the project root:

```bash
python -m app.rag.ingest
```

This creates the local `chroma_db` directory. It is generated runtime data and is ignored by Git.

## Run the application

```bash
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/> in a browser.

Useful endpoints:

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Browser frontend |
| `GET` | `/health` | Health check |
| `POST` | `/ask` | Ask the assistant |
| `GET` | `/docs` | FastAPI interactive documentation |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/ask \
	-H "Content-Type: application/json" \
	-d '{"question":"What is the leave policy?","employee_id":null}'
```

Example response:

```json
{
	"answer": "..."
}
```

## Project structure

```text
app/
	agents/       Question routing and assistant orchestration
	api/routes/   FastAPI endpoints
	database/     PostgreSQL connection
	rag/          PDF ingestion and policy retrieval
	tools/        Employee data lookup
frontend/       Static browser interface
data/knowledge/ Policy PDFs
scripts/        Manual smoke-test scripts
tests/          Database test entry point
```

## Testing

The scripts in `scripts/` are manual smoke tests for routing, RAG, employee lookup, and database connectivity. Run them from the project root with the virtual environment activated, for example:

```bash
python scripts/test_router.py
python scripts/test_agent.py
```

The database scripts require PostgreSQL, and the RAG scripts require Ollama plus an ingested `chroma_db`.

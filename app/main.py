from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes.assistant import router as assistant_router


app = FastAPI(
    title="DT Office Assistant",
    description="Agentic AI assistant for DT employees",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "dt-office-assistant"
    }


app.include_router(assistant_router)

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
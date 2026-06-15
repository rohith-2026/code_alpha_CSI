from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.prediction import router as prediction_router


BASE_DIR = Path(__file__).resolve().parents[1]

app = FastAPI(
    title="Credit Scoring Intelligence System",
    description="Portfolio-grade fintech ML application for XGBoost credit risk scoring.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.include_router(prediction_router)


@app.get("/", response_class=HTMLResponse, name="home")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/health", name="health")
async def health():
    return {"status": "ok", "service": "credit-scoring-intelligence-system"}

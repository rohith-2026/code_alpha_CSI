from uuid import uuid4

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app.services.model_service import model_service


router = APIRouter()
templates = Jinja2Templates(directory="templates")
RESULT_STORE = {}


class ApplicantPayload(BaseModel):
    gender: str = Field(pattern="^(F|M|XNA)$")
    age: int = Field(ge=18, le=100)
    annual_income: float = Field(gt=0)
    loan_amount: float = Field(gt=0)
    annuity_amount: float = Field(gt=0)
    employment_days: int = Field(ge=0)
    children: int = Field(ge=0, le=20)
    family_members: int = Field(ge=1, le=30)


@router.get("/assessment", response_class=HTMLResponse, name="assessment")
async def assessment(request: Request):
    return templates.TemplateResponse(request, "assessment.html", {"errors": []})


@router.post("/assessment", name="submit_assessment")
async def submit_assessment(
    gender: str = Form(...),
    age: int = Form(..., ge=18, le=100),
    annual_income: float = Form(..., gt=0),
    loan_amount: float = Form(..., gt=0),
    annuity_amount: float = Form(..., gt=0),
    employment_days: int = Form(...),
    children: int = Form(..., ge=0, le=20),
    family_members: int = Form(..., ge=1, le=30),
):
    applicant = {
        "gender": gender,
        "age": age,
        "annual_income": annual_income,
        "loan_amount": loan_amount,
        "annuity_amount": annuity_amount,
        "employment_days": employment_days,
        "children": children,
        "family_members": family_members,
    }
    result = model_service.predict(applicant)
    result_id = str(uuid4())
    RESULT_STORE[result_id] = result
    return RedirectResponse(url=f"/processing/{result_id}", status_code=303)


@router.post("/api/predict", name="api_predict")
async def api_predict(payload: ApplicantPayload):
    return model_service.predict(payload.model_dump())


@router.get("/processing/{result_id}", response_class=HTMLResponse, name="processing")
async def processing(request: Request, result_id: str):
    return templates.TemplateResponse(
        request,
        "processing.html",
        {"result_id": result_id},
    )


@router.get("/result/{result_id}", response_class=HTMLResponse, name="result")
async def result(request: Request, result_id: str):
    result_data = RESULT_STORE.get(result_id)
    if result_data is None:
        result_data = {
            "status": "Result expired",
            "risk_score": None,
            "risk_category": "Unavailable",
            "risk_class": "high",
            "recommendation": "Please run a new assessment.",
            "decision_summary": "The previous assessment session is no longer available.",
            "confidence": 0,
            "error": "No assessment result was found for this session.",
            "features": {},
            "drivers": [],
            "model_note": "Run a new assessment.",
        }
    return templates.TemplateResponse(
        request,
        "result.html",
        {"result": result_data},
    )

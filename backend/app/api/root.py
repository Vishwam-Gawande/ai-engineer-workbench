from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse)
def root():
    return HealthResponse(
        message="Welcome to AI Engineer Workbench API!"
    )
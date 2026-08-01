from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.core.security import verify_api_key

from app.models.models import Prompt

from app.schemas.prompt import PromptCreate
from app.schemas.prompt_update import PromptUpdate
from app.schemas.prompt_response import PromptResponse

from app.services.prompt_service import PromptService


router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
    dependencies=[Depends(verify_api_key)],
)


def get_prompt_service(
    db: Session = Depends(get_db),
):
    return PromptService(db)


@router.get(
    "/",
    response_model=list[PromptResponse],
)
def list_prompts(
    service: PromptService = Depends(get_prompt_service),
):
    return service.list_prompts()


@router.get(
    "/{prompt_id}",
    response_model=PromptResponse,
)
def get_prompt(
    prompt_id: int,
    service: PromptService = Depends(get_prompt_service),
):
    prompt = service.get_prompt(prompt_id)

    if not prompt:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found.",
        )

    return prompt


@router.post(
    "/",
    response_model=PromptResponse,
)
def create_prompt(
    data: PromptCreate,
    service: PromptService = Depends(get_prompt_service),
):
    prompt = Prompt(**data.model_dump())

    return service.create_prompt(prompt)
from fastapi import APIRouter, HTTPException, status

from app.schemas.prompt import PromptRequest
from app.schemas.prompt_response import PromptResponse

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
)


@router.post(
    "/",
    response_model=PromptResponse,
    status_code=status.HTTP_201_CREATED,
)
def submit_prompt(request: PromptRequest):
    return PromptResponse(
        received_prompt=request.prompt
    )


@router.get("/{prompt_id}")
def get_prompt(prompt_id: int):
    if prompt_id > 100:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found",
        )

    return {
        "prompt_id": prompt_id
    }
from fastapi import APIRouter, HTTPException, Path, Query, status

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
def get_prompt(
    prompt_id: int = Path(
        ge=1,
    ),
):
    if prompt_id > 100:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found",
        )

    return {
        "prompt_id": prompt_id
    }


@router.get("/")
def list_prompts(
    limit: int = Query(default=10, ge=1, le=100),
    search: str | None = None,
):
    return {
        "limit": limit,
        "search": search,
    }
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)


from app.core.security import verify_api_key
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
        title="Prompt ID",
        description="Unique ID of the prompt.",
        examples=[1],
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
    _: str = Depends(verify_api_key),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        title="Limit",
        description="Maximum number of prompts to return.",
        examples=[20],
    ),
    search: str | None = Query(
        default=None,
        alias="q",
        title="Search",
        description="Optional keyword used to filter prompts.",
        examples=["rag"],
        min_length=2,
        max_length=50,
        pattern=r"^[A-Za-z0-9 _-]+$",
    ),
    category: str | None = Query(
        default=None,
        title="Category",
        description="Optional prompt category filter.",
        examples=["rag"],
    ),
):
    # Reject whitespace-only searches
    if search is not None and search.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Search query cannot contain only whitespace.",
        )

    return {
        "limit": limit,
        "search": search,
        "category": category,
    }
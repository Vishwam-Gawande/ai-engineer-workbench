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


from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.prompt import Prompt


router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
)


@router.post(
    "/",
    response_model=PromptResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "description": "Invalid prompt data."
        },
        401: {
            "description": "Unauthorized."
        },
        500: {
            "description": "Internal server error."
        },
    },
)
def submit_prompt(
    prompt: PromptRequest,
    db: Session = Depends(get_db),
):
    db_prompt = Prompt(
    title=prompt.title,
    tags=", ".join(prompt.tags),
)

    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)

    return PromptResponse(
        id=db_prompt.id,
        title=db_prompt.title,
        tags=db_prompt.tags.split(", "),
        status="success",
        version="v1",
)


@router.get(
    "/{prompt_id}",
    response_model=PromptResponse,
)
def get_prompt(
    prompt_id: int = Path(
        ge=1,
        title="Prompt ID",
        description="Unique ID of the prompt.",
    ),
    db: Session = Depends(get_db),
):
    prompt = db.get(Prompt, prompt_id)

    if prompt is None:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found",
        )

    return PromptResponse(
        id=prompt.id,
        title=prompt.title,
        tags=prompt.tags.split(", "),
        status="success",
        version="v1",
    )


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
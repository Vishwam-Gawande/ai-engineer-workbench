from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)

from sqlalchemy.orm import Session

from app.core.security import verify_api_key
from app.db.dependencies import get_db

from app.services.prompt_service import PromptService

from app.schemas.prompt import PromptRequest
from app.schemas.prompt_update import PromptUpdateRequest
from app.schemas.prompt_response import PromptResponse


router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
)


@router.post(
    "/",
    response_model=PromptResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Invalid prompt data."},
        401: {"description": "Unauthorized."},
        500: {"description": "Internal server error."},
    },
)
def submit_prompt(
    prompt: PromptRequest,
    db: Session = Depends(get_db),
):
    service = PromptService(db)

    db_prompt = service.create_prompt(prompt)

    return PromptResponse(
    id=db_prompt.id,
    title=db_prompt.title,
    tags=[tag.strip() for tag in db_prompt.tags.split(",")] if db_prompt.tags else [],
    category=db_prompt.category,
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
    service = PromptService(db)

    prompt = service.get_prompt(prompt_id)

    if prompt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prompt not found.",
        )

    return PromptResponse(
    id=prompt.id,
    title=prompt.title,
    tags=[tag.strip() for tag in prompt.tags.split(",")] if prompt.tags else [],
    category=prompt.category,
    status="success",
    version="v1",
    )


@router.put(
    "/{prompt_id}",
    response_model=PromptResponse,
)
def update_prompt(
    prompt_id: int,
    prompt_update: PromptUpdateRequest,
    db: Session = Depends(get_db),
):
    service = PromptService(db)

    updated_prompt = service.update_prompt(
        prompt_id,
        prompt_update,
    )

    if updated_prompt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prompt not found.",
        )

    return PromptResponse(
    id=updated_prompt.id,
    title=updated_prompt.title,
    tags=[tag.strip() for tag in updated_prompt.tags.split(",")] if updated_prompt.tags else [],
    category=updated_prompt.category,
    status="success",
    version="v1",
    )


@router.delete(
    "/{prompt_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_prompt(
    prompt_id: int,
    db: Session = Depends(get_db),
):
    service = PromptService(db)

    deleted = service.delete_prompt(prompt_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prompt not found.",
        )


@router.get(
    "/",
    response_model=list[PromptResponse],
)
def list_prompts(
    _: str = Depends(verify_api_key),
    db: Session = Depends(get_db),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    search: str | None = Query(
        default=None,
        alias="q",
    ),
    category: str | None = Query(
        default=None,
    ),
):
    if search is not None and search.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Search query cannot contain only whitespace.",
        )

    service = PromptService(db)

    prompts = service.list_prompts(
        limit=limit,
        search=search,
        category=category,
    )

    return [
        PromptResponse(
            id=p.id,
            title=p.title,
            tags=[tag.strip() for tag in p.tags.split(",")] if p.tags else [],
            category=p.category,
            status="success",
            version="v1",
        )
        for p in prompts
    ]
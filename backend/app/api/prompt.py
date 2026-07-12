from fastapi import APIRouter

from app.schemas.prompt import PromptRequest

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
)


@router.post("/")
def submit_prompt(request: PromptRequest):
    return {
        "received_prompt": request.prompt
    }


@router.get("/{prompt_id}")
def get_prompt(prompt_id: int):
    return {
        "prompt_id": prompt_id
    }
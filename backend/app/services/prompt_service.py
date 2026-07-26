from sqlalchemy.orm import Session

from app.repositories.prompt_repository import PromptRepository

from app.schemas.prompt import PromptRequest
from app.schemas.prompt_update import PromptUpdateRequest


class PromptService:
    def __init__(self, db: Session):
        self.repository = PromptRepository(db)

    def create_prompt(
        self,
        prompt: PromptRequest,
    ):
        return self.repository.create(prompt)

    def get_prompt(
        self,
        prompt_id: int,
    ):
        return self.repository.get_by_id(prompt_id)

    def update_prompt(
        self,
        prompt_id: int,
        prompt_update: PromptUpdateRequest,
    ):
        db_prompt = self.repository.get_by_id(prompt_id)

        if db_prompt is None:
            return None

        return self.repository.update(
            db_prompt,
            prompt_update,
        )

    def delete_prompt(
        self,
        prompt_id: int,
    ):
        db_prompt = self.repository.get_by_id(prompt_id)

        if db_prompt is None:
            return False

        self.repository.delete(db_prompt)

        return True

    def list_prompts(
        self,
        limit: int,
        search: str | None,
        category: str | None,
    ):
        return self.repository.get_all(
            limit=limit,
            search=search,
            category=category,
        )
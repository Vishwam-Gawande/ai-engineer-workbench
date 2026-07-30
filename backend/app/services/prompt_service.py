from sqlalchemy.orm import Session

from app.models.models import Prompt
from app.repositories.prompt_repository import PromptRepository


class PromptService:

    def __init__(self, db: Session):
        self.repository = PromptRepository(db)

    def create_prompt(self, prompt: Prompt):
        return self.repository.create(prompt)

    def get_prompt(self, prompt_id: int):
        return self.repository.get_by_id(prompt_id)

    def list_prompts(self):
        return self.repository.get_all()
from sqlalchemy.orm import Session

from app.models.prompt import Prompt
from app.schemas.prompt import PromptRequest
from app.schemas.prompt_update import PromptUpdateRequest


class PromptRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, prompt: PromptRequest) -> Prompt:
        db_prompt = Prompt(
            title=prompt.title,
            tags=", ".join(prompt.tags),
        )

        self.db.add(db_prompt)
        self.db.commit()
        self.db.refresh(db_prompt)

        return db_prompt

    def get_all(self) -> list[Prompt]:
        return self.db.query(Prompt).all()

    def get_by_id(self, prompt_id: int) -> Prompt | None:
        return (
            self.db.query(Prompt)
            .filter(Prompt.id == prompt_id)
            .first()
        )

    def update(
        self,
        db_prompt: Prompt,
        prompt: PromptUpdateRequest,
    ) -> Prompt:

        db_prompt.title = prompt.title
        db_prompt.tags = ", ".join(prompt.tags)

        self.db.commit()
        self.db.refresh(db_prompt)

        return db_prompt

    def delete(self, db_prompt: Prompt) -> None:
        self.db.delete(db_prompt)
        self.db.commit()
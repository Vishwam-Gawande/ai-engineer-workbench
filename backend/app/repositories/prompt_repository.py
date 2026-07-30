from sqlalchemy.orm import Session

from app.models.models import Prompt


class PromptRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, prompt: Prompt):
        self.db.add(prompt)
        self.db.commit()
        self.db.refresh(prompt)
        return prompt

    def get_by_id(self, prompt_id: int):
        return (
            self.db.query(Prompt)
            .filter(Prompt.id == prompt_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Prompt).all()

    def delete(self, prompt: Prompt):
        self.db.delete(prompt)
        self.db.commit()
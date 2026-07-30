from pydantic import BaseModel


class PromptCreate(BaseModel):
    user_id: int
    name: str
    version: int
    template: str
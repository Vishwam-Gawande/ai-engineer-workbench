from pydantic import BaseModel


class PromptUpdate(BaseModel):
    name: str | None = None
    version: int | None = None
    template: str | None = None
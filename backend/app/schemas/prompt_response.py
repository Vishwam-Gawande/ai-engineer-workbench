from pydantic import BaseModel


class PromptResponse(BaseModel):
    id: int
    title: str
    tags: list[str]
    category: str
    status: str
    version: str
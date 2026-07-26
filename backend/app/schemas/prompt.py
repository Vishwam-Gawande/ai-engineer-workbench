from pydantic import BaseModel


class PromptRequest(BaseModel):
    title: str
    tags: list[str]
    category: str = "general"
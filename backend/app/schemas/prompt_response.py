from pydantic import BaseModel


class PromptResponse(BaseModel):
    id: int
    title: str
    tags: list[str]
    status: str = "success"
    version: str = "v1"
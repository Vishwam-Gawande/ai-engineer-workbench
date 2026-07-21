from pydantic import BaseModel, Field


class PromptResponse(BaseModel):
    prompt_id: int = Field(serialization_alias="id")

    title: str

    tags: list[str]

    status: str = "success"

    version: str = "v1"
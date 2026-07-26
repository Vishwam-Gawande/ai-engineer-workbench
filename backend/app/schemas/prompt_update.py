from pydantic import BaseModel, Field


class PromptUpdateRequest(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=255,
    )

    tags: list[str] = Field(
        min_length=1,
    )

    category: str = Field(
        min_length=3,
        max_length=100,
    )
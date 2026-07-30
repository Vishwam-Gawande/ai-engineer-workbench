from pydantic import BaseModel, ConfigDict


class PromptResponse(BaseModel):
    id: int
    user_id: int
    name: str
    version: int
    template: str

    model_config = ConfigDict(from_attributes=True)
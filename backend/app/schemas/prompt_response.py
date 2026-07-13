from pydantic import BaseModel


class PromptResponse(BaseModel):
    received_prompt: str
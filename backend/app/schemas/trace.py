from pydantic import BaseModel, ConfigDict


class TraceCreate(BaseModel):
    user_id: int
    trace_name: str
    status: str
    model_name: str
    latency_ms: int
    total_tokens: int
    total_cost: float


class TraceUpdate(BaseModel):
    trace_name: str | None = None
    status: str | None = None


class TraceResponse(BaseModel):
    id: int
    user_id: int
    trace_name: str
    status: str
    model_name: str
    latency_ms: int
    total_tokens: int
    total_cost: float

    model_config = ConfigDict(from_attributes=True)
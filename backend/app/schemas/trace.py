from pydantic import BaseModel


class TraceResponse(BaseModel):
    id: int
    trace_name: str
    model: str
    latency: str
    tokens: str
    cost: str
    status: str

    class Config:
        from_attributes = True


class TraceCreate(BaseModel):
    trace_name: str
    model: str
    latency: str
    tokens: str
    cost: str
    status: str


class TraceUpdate(BaseModel):
    trace_name: str | None = None
    model: str | None = None
    latency: str | None = None
    tokens: str | None = None
    cost: str | None = None
    status: str | None = None
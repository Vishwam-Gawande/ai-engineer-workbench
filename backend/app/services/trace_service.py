from app.models.trace import Trace
from app.repositories.trace_repository import TraceRepository
from app.schemas.trace import TraceCreate, TraceUpdate


class TraceService:
    def __init__(self, repository: TraceRepository):
        self.repository = repository

    def get_traces(self):
        return self.repository.get_all()

    def get_trace(self, trace_id: int):
        return self.repository.get_by_id(trace_id)

    def create_trace(self, trace_data: TraceCreate):
        trace = Trace(
            trace_name=trace_data.trace_name,
            model=trace_data.model,
            latency=trace_data.latency,
            tokens=trace_data.tokens,
            cost=trace_data.cost,
            status=trace_data.status,
        )

        return self.repository.create(trace)

    def update_trace(
        self,
        trace: Trace,
        trace_data: TraceUpdate,
    ):
        updates = trace_data.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(trace, field, value)

        return self.repository.update(trace)

    def delete_trace(self, trace: Trace):
        self.repository.delete(trace)
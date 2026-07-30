from sqlalchemy.orm import Session

from app.models.models import Trace
from app.repositories.trace_repository import TraceRepository


class TraceService:

    def __init__(self, db: Session):
        self.repository = TraceRepository(db)

    def create_trace(self, trace: Trace):
        return self.repository.create(trace)

    def get_trace(self, trace_id: int):
        return self.repository.get_by_id(trace_id)

    def list_traces(self):
        return self.repository.get_all()
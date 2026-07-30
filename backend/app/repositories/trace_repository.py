from sqlalchemy.orm import Session

from app.models.models import Trace


class TraceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, trace: Trace):
        self.db.add(trace)
        self.db.commit()
        self.db.refresh(trace)
        return trace

    def get_by_id(self, trace_id: int):
        return (
            self.db.query(Trace)
            .filter(Trace.id == trace_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Trace).all()

    def delete(self, trace: Trace):
        self.db.delete(trace)
        self.db.commit()
from sqlalchemy.orm import Session

from app.models.trace import Trace


class TraceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(Trace)
            .order_by(Trace.id)
            .all()
        )

    def get_by_id(self, trace_id: int):
        return (
            self.db.query(Trace)
            .filter(Trace.id == trace_id)
            .first()
        )

    def create(self, trace: Trace):
        self.db.add(trace)
        self.db.commit()
        self.db.refresh(trace)
        return trace

    def update(self, trace: Trace):
        self.db.commit()
        self.db.refresh(trace)
        return trace

    def delete(self, trace: Trace):
        self.db.delete(trace)
        self.db.commit()
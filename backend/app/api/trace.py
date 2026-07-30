from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.models import Trace

from app.schemas.trace import (
    TraceCreate,
    TraceResponse,
)

from app.services.trace_service import TraceService


router = APIRouter(
    prefix="/traces",
    tags=["Traces"],
)


def get_trace_service(
    db: Session = Depends(get_db),
):
    return TraceService(db)


@router.get(
    "/",
    response_model=list[TraceResponse],
)
def list_traces(
    service: TraceService = Depends(get_trace_service),
):
    return service.list_traces()


@router.get(
    "/{trace_id}",
    response_model=TraceResponse,
)
def get_trace(
    trace_id: int,
    service: TraceService = Depends(get_trace_service),
):
    trace = service.get_trace(trace_id)

    if not trace:
        raise HTTPException(
            status_code=404,
            detail="Trace not found.",
        )

    return trace


@router.post(
    "/",
    response_model=TraceResponse,
)
def create_trace(
    data: TraceCreate,
    service: TraceService = Depends(get_trace_service),
):
    trace = Trace(**data.model_dump())

    return service.create_trace(trace)
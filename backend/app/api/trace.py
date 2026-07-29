from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.trace import Trace

from app.repositories.trace_repository import TraceRepository
from app.schemas.trace import (
    TraceCreate,
    TraceResponse,
    TraceUpdate,
)
from app.services.trace_service import TraceService

router = APIRouter(
    prefix="/traces",
    tags=["Traces"],
)


def get_trace_service(db: Session = Depends(get_db)):
    repository = TraceRepository(db)
    return TraceService(repository)


@router.get(
    "/",
    response_model=list[TraceResponse],
)
def list_traces(
    service: TraceService = Depends(get_trace_service),
):
    return service.get_traces()


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
    trace_data: TraceCreate,
    service: TraceService = Depends(get_trace_service),
):
    return service.create_trace(trace_data)


@router.put(
    "/{trace_id}",
    response_model=TraceResponse,
)
def update_trace(
    trace_id: int,
    trace_data: TraceUpdate,
    service: TraceService = Depends(get_trace_service),
):
    trace = service.get_trace(trace_id)

    if not trace:
        raise HTTPException(
            status_code=404,
            detail="Trace not found.",
        )

    return service.update_trace(
        trace,
        trace_data,
    )


@router.delete(
    "/{trace_id}",
)
def delete_trace(
    trace_id: int,
    service: TraceService = Depends(get_trace_service),
):
    trace = service.get_trace(trace_id)

    if not trace:
        raise HTTPException(
            status_code=404,
            detail="Trace not found.",
        )

    service.delete_trace(trace)

    return {
        "message": "Trace deleted successfully."
    }
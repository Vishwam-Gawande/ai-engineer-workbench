from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.root import router as root_router
from app.core.config import settings
from app.core.logging import logger

logger.info("Starting AI Engineer Workbench...")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup complete.")

    yield

    logger.info("Application shutdown complete.")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(root_router)
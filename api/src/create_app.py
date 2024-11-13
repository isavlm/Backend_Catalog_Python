from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from adapters.src.repositories import Connection, SessionManager, SQLConnection

from api.src.routes import health_check_router, product_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    connection: Connection = SQLConnection()
    SessionManager.initialize_session(connection)
    yield
    SessionManager.close_session()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(health_check_router, tags=["health check"])
    app.include_router(product_router, tags=["products"])
    return app

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

health_check_router = APIRouter(prefix="/health_check")


class HealthCheck(BaseModel):
    status: Literal["OK", "ERROR"]


@health_check_router.get("/", response_model=HealthCheck)
async def check_health() -> HealthCheck:
    return HealthCheck(status="OK")

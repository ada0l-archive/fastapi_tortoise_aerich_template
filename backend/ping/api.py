from fastapi import APIRouter, HTTPException
from pydantic import conint
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.queryset import QuerySet

from backend.core.schemas import Status
from backend.ping.models import Ping, Ping_Pydantic, PingIn_Pydantic

router = APIRouter()


@router.get("/pings", response_model=list[Ping_Pydantic])
async def get_pings(limit: conint(ge=1, le=100, strict=False)):
    return await Ping_Pydantic.from_queryset(QuerySet(Ping).limit(limit).order_by("id").all())


@router.get("/ping/{ping_id}", response_model=Ping_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def ping(ping_id: int):
    return await Ping_Pydantic.from_queryset_single(Ping.get(id=ping_id))


@router.post("/ping", response_model=Ping_Pydantic)
async def create_ping(ping_in: PingIn_Pydantic):
    user_obj = await Ping.create(**ping_in.dict(exclude_unset=True))
    return await Ping_Pydantic.from_tortoise_orm(user_obj)


@router.put("/ping/{ping_id}", response_model=Ping_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_ping(ping_id: int, ping_in: PingIn_Pydantic):
    await Ping.filter(id=ping_id).update(**ping_in.dict(exclude_unset=True))
    return await Ping_Pydantic.from_queryset_single(Ping.get(id=ping_id))


@router.delete("/ping/{ping_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_ping(ping_id: int):
    deleted_count = await Ping.filter(id=ping_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Ping {ping_id} not found")
    return Status(message=f"Deleted ping {ping_id}")

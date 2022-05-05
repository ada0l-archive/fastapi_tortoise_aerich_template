import pytest
from httpx import AsyncClient

from backend.ping.models import Ping, Ping_Pydantic, PingIn_Pydantic
from main import app


@pytest.mark.asyncio
async def test_ping_create():
    ping_in = PingIn_Pydantic(**{"name": "ping"})

    assert await Ping.filter(name=ping_in.name).count() == 0

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/ping", json=ping_in.dict())
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == ping_in.name
        await ac.post("/ping", json=ping_in.dict())

    assert await Ping.filter(name=ping_in.name).count() == 2
    assert (await Ping_Pydantic.from_queryset_single(Ping.get(id=1))).name == ping_in.name

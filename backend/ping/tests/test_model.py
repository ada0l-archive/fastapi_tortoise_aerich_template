import pytest

from backend.ping.models import Ping, Ping_Pydantic, PingIn_Pydantic


@pytest.mark.asyncio
async def test_ping_create():
    ping_in = PingIn_Pydantic(**{"name": "pong"})

    assert await Ping.filter(name=ping_in.name).count() == 0
    ping = await Ping.create(**ping_in.dict(exclude_unset=True))

    assert ping.name == ping_in.name

    assert await Ping.filter(name=ping_in.name).count() == 1
    assert (await Ping_Pydantic.from_queryset_single(Ping.get(id=1))).name == ping_in.name

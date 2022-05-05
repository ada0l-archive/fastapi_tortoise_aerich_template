from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from backend.core.settings import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url,
    },
    "apps": {
        "models": {
            "models": ["aerich.models"] + settings.models,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.database_url,
        modules={"models": settings.models},
        generate_schemas=True,
        add_exception_handlers=True,
    )

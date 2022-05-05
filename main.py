from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.database import init_db
from backend.core.settings import settings
from backend.ping import api as ping

settings.configure_logging()
app = FastAPI(**settings.fastapi_kwargs)

if settings.allowed_hosts:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    init_db(app)


app.include_router(ping.router)

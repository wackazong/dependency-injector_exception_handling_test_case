from fastapi import FastAPI
import sys

from api.containers import Application
from api.core import Settings
from api.routes import listener_router
import requests



def main() -> FastAPI:
    app = FastAPI(
    )
    app.include_router(listener_router.router, prefix="/listener", tags=["listener"])
    return app


application = Application()
application.config.from_pydantic(Settings())
application.wire(modules=[sys.modules[__name__], listener_router])
app = main()
app.container = application  # type: ignore


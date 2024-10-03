from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.routes import main_router
from app.api.middlewares import AuthMiddleware

from app.settings import SETTINGS
from app.utils.mongodb import MongoDB


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())
app.include_router(main_router)


@app.on_event("startup")
async def app_startup():
    # Setup MongoDB
    MongoDB.setup(
        SETTINGS.MONGODB_URL.get_secret_value(), SETTINGS.MONGODB_DB.get_secret_value()
    )

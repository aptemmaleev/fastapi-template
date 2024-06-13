import asyncio

from fastapi import FastAPI
from uvicorn import Config, Server
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.settings import SETTINGS
from app.api.routes import main_router
from app.api.middlewares import AuthMiddleware


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())
app.include_router(main_router)

def start_api(loop = None):
    if loop is None:
        loop = asyncio.get_running_loop()
    server_config = Config(
        app=app, 
        host=SETTINGS.API_HOST, 
        port=int(SETTINGS.API_PORT), 
        loop=loop
    )
    server = Server(config=server_config)
    loop.create_task(server.serve())
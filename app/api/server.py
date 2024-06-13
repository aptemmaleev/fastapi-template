import asyncio

from fastapi import FastAPI
from uvicorn import Config, Server
from starlette.responses import JSONResponse

from app.settings import SETTINGS
from app.api.routes import main_router


app = FastAPI()
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
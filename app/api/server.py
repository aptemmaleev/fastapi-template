from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.routes import main_router
from app.api.middlewares import AuthMiddleware


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())
app.include_router(main_router)
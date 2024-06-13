from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.settings import SETTINGS
from app.utils.mongo import MongoDB

router = APIRouter()


@router.get("/")
async def root():
    return JSONResponse(status_code=200, content={"message": "Bober Rostislav"})
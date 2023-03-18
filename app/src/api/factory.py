from fastapi import FastAPI
from src.api.resources.paint_mall.router import paint_mall_router


def create_api() -> FastAPI:
    api = FastAPI()

    api.include_router(paint_mall_router)

    return api

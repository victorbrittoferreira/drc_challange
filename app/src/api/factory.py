from fastapi import FastAPI

from src.api.resources.paint_cans_calculator.router import paint_mall_router_v1


def create_api() -> FastAPI:
    """
    Creates a new instance of the FastAPI application and includes the paint mall API router.

    Returns:
    --------
    api: FastAPI
        The created instance of the FastAPI application.
    """
    api = FastAPI()

    api.include_router(paint_mall_router_v1)

    return api

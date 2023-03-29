from fastapi import APIRouter

from .room_analyzer_paint_cans import register_post_paint_cans_needed_view

paint_mall_router_v1 = APIRouter(
    prefix="/api/v1",
    tags=["Paint Mall Endpoints"],
)

register_post_paint_cans_needed_view(paint_mall_router_v1)

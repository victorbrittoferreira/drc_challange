from fastapi import APIRouter

from .buy_list import register_post_paint_cans_buy_list_view

# calculator paint cans needed
paint_mall_router = APIRouter(
    prefix="/paint_mall",
    # tags=["paint_mall"],
)

register_post_paint_cans_buy_list_view(paint_mall_router)

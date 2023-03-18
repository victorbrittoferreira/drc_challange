from fastapi import APIRouter
from src.entities.paint_can import PaintCanToBuy
from src.entities.room import Room
from src.services.validators import validate_room_data
from src.use_cases.paint_mall import get_paint_can_buy_list

# TODO: TRY/RESPONSE_MODEL/SUMARIZAR/DESCRICAO/CONTENT(EXAMPLE)


def register_post_paint_cans_buy_list_view(router: APIRouter):
    @router.post(
        path="/amount_paint_can_calculator",
        response_model=PaintCanToBuy,
        summary="",  # noqa: 501
        responses={
            200: {
                "description": "",  # noqa: 501
                "content": {"application/json": {"example": {"payload": {}}}},
            },
            422: {
                "description": "Validation error",
                "content": {
                    "application/json": {
                        "example": {
                            "message": "You probably missed data structure or type."  # noqa: 501
                        }
                    }
                },
            },
        },
    )
    # TODO: OUTPUT
    def post_paint_cans_buy_list(room: Room):
        validate_room_data(room)
        paint_cans_buy_list = get_paint_can_buy_list(room)
        return paint_cans_buy_list

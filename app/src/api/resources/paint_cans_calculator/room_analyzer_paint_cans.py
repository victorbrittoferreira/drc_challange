from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.controllers.main_controller import PaintCansController
from src.schemas.request.room import Room
from src.schemas.response.paint_cans_needed import PaintCansNeeded


def register_post_paint_cans_needed_view(router: APIRouter):
    @router.post(
        path="/paint_mall/paint_cans_needed",
        response_model=PaintCansNeeded,
        status_code=200,
        summary="Calculate the amount of paint cans needed to paint a room.",
        responses={
            200: {
                "description": "The amount of paint cans needed.",
                "content": {
                    "application/json": {
                        "example": {
                            "paint_cans": {
                                "18.0": 1,
                                "3.6": 2,
                                "2.5": 0,
                                "0.5": 2,
                            }
                        }
                    }
                },
            },
            422: {
                "description": "Validation error",
                "content": {
                    "application/json": {
                        "example": {
                            "detail": [
                                {
                                    "loc": ["body", "walls", 0, "width"],
                                    "msg": "ensure this value is greater than 0",
                                    "type": "value_error.number.not_gt",
                                    "ctx": {"limit_value": 0},
                                }
                            ]
                        }
                    }
                },
            },
            500: {
                "description": "Server error",
                "content": {
                    "application/json": {
                        "example": {
                            "detail": "An error occurred on the server."
                        }
                    }
                },
            },
        },
    )
    def post_paint_cans(room: Room) -> JSONResponse | PaintCansNeeded:
        """Calculate the amount of paint cans needed to paint a room.

        ## Request Body

        The request body should be a JSON object containing an array of walls,
        where each wall is defined by the following properties:

        - `width` (float): The width of the wall in feet.
        - `height` (float): The height of the wall in feet.
        - `number_doors` (int): The number of doors on the wall.
        - `number_windows` (int): The number of windows on the wall.

        Example:

        ```json
        {
          "walls": [
            {
              "width": 7.1,
              "height": 5.2,
              "number_doors": 1,
              "number_windows": 2
            },
            {
              "width": 7.1,
              "height": 5.2,
              "number_doors": 2,
              "number_windows": 2
            },
            {
              "width": 7.1,
              "height": 5.2,
              "number_doors": 0,
              "number_windows": 0
            },
            {
              "width": 7.1,
              "height": 5.2,
              "number_doors": 0,
              "number_windows": 0
            }
          ]
        }
        ```
        ## Error Responses

        - `422` (Validation error): If the request body fails validation,
            returns a JSON object with the following properties:
            detail (array): An array of objects containing details
             about each validation error.
        - `500` (Server error): If an unexpected error occurs on the
            server, returns a JSON object with the following properties:
            detail (string): A description of the error.

        """

        try:
            paint_cans_needed = PaintCansController(room)
            response = (
                paint_cans_needed.calculate_paint_cans_needed_controller()
            )

        except ValidationError as error:
            return JSONResponse(status_code=422, content=error.errors())
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="An internal error occurred on the server.",
            )

        return response

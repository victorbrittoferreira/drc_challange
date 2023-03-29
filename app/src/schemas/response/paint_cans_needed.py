from typing import Dict, NewType

from pydantic import BaseModel, validator

PaintCans = NewType("PaintCans", Dict[float, int])


class PaintCansNeeded(BaseModel):
    # """
    # Represent the required number of paint cans for cover a given area.

    # Attributes:
    # ----------
    # paint_cans: A dictionary where each key is a size and the value
    # is the number of cans required for that size.
    #
    # Raises:
    # ------
    # ValuerError: an unexpected error happened
    # """

    paint_cans: PaintCans

    @validator("paint_cans")
    def validate_amount_paint_cans_needed(cls, paint_cans_needed) -> PaintCans:
        for can in paint_cans_needed.values():
            if can < 0:
                raise ValueError("Server error. An interal error occurred.")
        return paint_cans_needed

    class Config:
        extra = "forbid"
        frozen = True
        schema_extra = {
            "example": {
                "paint_cans": {"18.0": 1, "3.6": 2, "2.5": 0, "0.5": 2}
            }
        }

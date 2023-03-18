from typing import List

from pydantic import BaseModel


class PaintCanToBuy(BaseModel):
    paint_can_list: List[float]

    # class Config:
    #     extra = "forbid"

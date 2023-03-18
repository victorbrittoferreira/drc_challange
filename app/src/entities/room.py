from typing import Tuple

from pydantic import BaseModel
from src.entities.door import DEFAULT_DOOR
from src.entities.wall import Wall
from src.entities.window import DEFAULT_WINDOW


class Room(BaseModel):
    walls: Tuple[Wall, Wall, Wall, Wall]

    @property
    def walls_area(self) -> float:
        # return sum([wall.area for wall in self.walls])
        return sum(wall.area for wall in self.walls)

    @property
    def windows_area(self) -> float:
        # windows_area = 0
        # for wall in self.walls:
        #     windows_area += wall.windows * DEFAULT_WINDOW.area
        # return windows_area
        return sum(wall.windows * DEFAULT_WINDOW.area for wall in self.walls)

    @property
    def doors_area(self) -> float:
        # doors_area = 0
        # for wall in self.walls:
        # doors_area += wall.doors * DEFAULT_DOOR.area
        # return doors_area
        return sum(wall.doors * DEFAULT_DOOR.area for wall in self.walls)

    class Config:
        extra = "forbid"

from dataclasses import dataclass


@dataclass
class Door:
    height: float
    width: float

    @property
    def area(self):
        return self.width * self.height


DEFAULT_DOOR: Door = Door(0.8, 1.9)

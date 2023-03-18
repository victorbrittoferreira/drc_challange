from dataclasses import dataclass


@dataclass
class Window:
    height: float
    width: float

    @property
    def area(self):
        return self.width * self.height


DEFAULT_WINDOW: Window = Window(2.0, 1.2)

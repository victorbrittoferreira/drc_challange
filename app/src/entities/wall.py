from pydantic import BaseModel


class Wall(BaseModel):
    width: float
    height: float
    doors: int = 0
    windows: int = 0

    @property
    def area(self):
        return self.width * self.height

    class Config:
        extra = "forbid"

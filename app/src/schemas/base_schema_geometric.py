from abc import ABCMeta
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Rectangle(metaclass=ABCMeta):
    """A dataclass representing a rectangle with a given width and height.

    This class provides a simple way to create and manipulate rectangle objects. It includes a property for computing the area of the rectangle based on its width and height, and it raises a ValueError if either the width or height is less than or equal to zero.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Example usage:
        >>> rect = Rectangle(3.0, 4.0)
        >>> rect.area
        12.0
    """

    width: float
    height: float

    def __post_init__(self) -> None:
        if not isinstance(self.width, (int, float)):
            raise ValueError("Width must be an integer or float.")
        if not isinstance(self.height, (int, float)):
            raise ValueError("Height must be an integer or float.")
        if self.width <= 0:
            raise ValueError("Width must be greater than 0.")
        if self.height <= 0:
            raise ValueError("Height must be greater than 0.")

    @property
    def area(self) -> float:
        return self.width * self.height

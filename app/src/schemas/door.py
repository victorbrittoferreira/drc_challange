from dataclasses import dataclass

from .base_schema_geometric import Rectangle


@dataclass(slots=True, frozen=True)
class Door(Rectangle):
    """A dataclass representing a door with a given width and height.

    This class provides a simple way to create and manipulate door
    objects. It includes a property for computing the area of the door
    based on its width and height, and it raises a ValueError if either
      the width or height is less than or equal to zero.

    Attributes:
        width (float): The width of the door.
        height (float): The height of the door.

    Example usage:
        >>> rect = Rectangle(3.0, 4.0)
        >>> rect.area
        12.0
    """

    pass


DEFAULT_DOOR: Door = Door(0.8, 1.9)

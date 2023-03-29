from dataclasses import dataclass

from .base_schema_geometric import Rectangle


@dataclass(slots=True, frozen=True)
class Window(Rectangle):
    """A dataclass representing a window with a given width and height.

    This class provides a simple way to create and manipulate window
    objects. It includes a property for computing the area of the window
    based on its width and height, and it raises a ValueError if either
      the width or height is less than or equal to zero.

    Attributes:
        width (float): The width of the window.
        height (float): The height of the window.

    Example usage:
        >>> rect = Rectangle(3.0, 4.0)
        >>> rect.area
        12.0
    """

    pass


DEFAULT_WINDOW: Window = Window(2.0, 1.2)

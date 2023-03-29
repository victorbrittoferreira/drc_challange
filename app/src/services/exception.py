# ------------------------------- VALIDATOR ------------------------------------


class InvalidRoomDimensionError(Exception):
    """
    Raised when the room dimensions are invalid, such as when they are not
    too much taller, smaller, narrower. When the dimensions do not form a valid shape
    """

    pass


class WallAreaOutOfRangeError(Exception):
    """
    Raised when the area of a wall is outside the allowable range.
    """

    pass


class InsufficientWallFreeAreaError(Exception):
    """
    Raised when a wall does not have enough free area to paint due to the presence of windows and doors.
    """

    pass


class WallNotTallerThanDoorError(Exception):
    """
    Raised when a wall is not taller than a door by at least a minimum height difference.
    """

    pass


class WallNotTallerThanWindowError(Exception):
    """Raised when a wall is not taller than a window by at least the minimum height difference."""

    pass


class WallNotWiderThanDoorWindowError(ValueError):
    pass
    """Raised when a given wall is not wider than width of a given amount of doors and windows."""


# ------------------------------- PAINT CANS NEEDED CALCULATOR------------------

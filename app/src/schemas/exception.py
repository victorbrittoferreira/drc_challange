# ----------------- WAll --------------------------
class NegativeWallAreaError(Exception):
    """
    Raised when the calculated a wall area is negative.
    """

    pass


class NegativeWindowsAreaWallError(Exception):
    """
    Raised when the calculated a total windows area in a wall is negative.
    """

    pass


class NegativeDoorsAreaWallError(Exception):
    """
    Raised when the calculated a total doors area in a wall is negative.
    """

    pass

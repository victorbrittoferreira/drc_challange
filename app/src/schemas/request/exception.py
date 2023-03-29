# ----------------- Room --------------------------
class NegativeWallAreaRoomError(Exception):
    """
    Raised when the calculated a total wall area in a room is negative.
    """

    pass


class NegativeWindowsAreaRoomError(Exception):
    """
    Raised when the calculated a total windows area in a room is negative.
    """

    pass


class NegativeDoorsAreaRoomError(Exception):
    """
    Raised when the calculated a total doors area in a room is negative.
    """

    pass

from pydantic import BaseModel, Field

from src.schemas.door import DEFAULT_DOOR, Door
from src.schemas.exception import (
    NegativeDoorsAreaWallError,
    NegativeWallAreaError,
    NegativeWindowsAreaWallError,
)
from src.schemas.window import DEFAULT_WINDOW, Window


class WallBase(BaseModel):
    pass


class Wall(WallBase):
    # """
    # Represents a  schemal of wall in a building.

    # A wall has a width and height, and may have zero or more doors and windows.

    # Attributes:
    # ----------
    # width : float
    #     The width of the wall in meters.
    # height : float
    #     The height of the wall in meters.
    # number_doors : int, optional
    #     The number of doors in the wall (default 0).
    # number_windows : int, optional
    #     The number of windows in the wall (default 0).

    # Raises:
    # ------
    # NegativeWallAreaError : if wall area is negative.
    # NegativeWindowsAreaWallError : if windows area is negative.
    # NegativeDoorsAreaWallError : if door area is negative.

    # """

    width: float = Field(
        gt=0, description="The width must be greater than zero"
    )
    height: float = Field(
        gt=0, description="The height must be greater than zero"
    )
    number_doors: int = Field(
        ge=0,
        default=0,
        description="The amount of doors must be equal or greater than zero",
    )
    number_windows: int = Field(
        ge=0,
        default=0,
        description="The amount of windows must be equal or greater than zero",
    )

    @property
    def area(self):
        """
        Computes the area of the wall.

        Returns:
        -------
        float : the area of the wall in square meters.

        Raises:
        ------
        NegativeWallAreaError : if wall area is negative.
        """
        wall_area = self.width * self.height
        if wall_area <= 0:
            raise NegativeWallAreaError(
                f"The wall area is negative {wall_area:.2}m2"
            )
        return wall_area

    @property
    def windows_area(self) -> float:
        """
        Computes the total area of all the windows in the wall.

        Returns:
        -------
        float : the total area of all the windows in the wall in square meters.

        Raises:
        ------
        NegativeWindowsAreaWallError : if windows area is negative.
        """
        windows_area_ = self.window.area * self.number_windows
        if windows_area_ < 0:
            raise NegativeWindowsAreaWallError(
                f"The windows area is negative {windows_area_:.2}m2"
            )
        return windows_area_

    @property
    def doors_area(self) -> float:
        """
        Computes the total area of all the doors in the wall.

        Returns:
        -------
        float : the total area of all the doors in the wall in square meters.

        Raises:
        ------
        NegativeDoorsAreaWallError : if door area is negative.
        """
        doors_area_ = self.door.area * self.number_doors
        if doors_area_ < 0:
            raise NegativeDoorsAreaWallError(
                f"The door area is negative {doors_area_:.2f}m2"
            )
        return doors_area_

    @property
    def door(self) -> Door:
        """
        Returns the default door object for the wall.

        Returns:
        -------
        Door : the default door object for the wall.
        """
        return DEFAULT_DOOR

    @property
    def window(self) -> Window:
        """
        Returns the default window object for the wall.

        Returns:
        -------
        Window : the default window object for the wall.
        """
        return DEFAULT_WINDOW

    class Config:
        extra = "forbid"
        frozen = True

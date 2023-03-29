from typing import NewType, Tuple

from pydantic import BaseModel

from src.schemas.request.exception import (
    NegativeDoorsAreaRoomError,
    NegativeWallAreaRoomError,
    NegativeWindowsAreaRoomError,
)
from src.schemas.wall import Wall

Walls = NewType("Walls", Tuple[Wall, Wall, Wall, Wall])


class RoomBase(BaseModel):
    pass


class Room(RoomBase):
    # """
    # Represents a room with four walls, where each wall has doors and windows

    # Parameters:
    # -----------
    # walls : tuple
    #     The tuple that contains four walls of the room.
    #     The walls must be represented by instances of the Wall model.

    # Raises:
    # -------
    # NegativeWallAreaRoomError:
    #     If the total area of the room walls is less than or equal to zero.
    # NegativeDoorsAreaRoomError:
    #     If the total area of the room doors is less than zero.
    # NegativeWindowsAreaRoomError:
    #     If the total area of the room windows is less than zero.

    # Attributes:
    # -----------
    # walls_area : float
    #     The total area of all four walls of the room.
    # windows_area : float
    #     The total area of all windows in the room.
    # doors_area : float
    #     The total area of all doors in the room.

    # Raises:
    # ------
    # NegativeWallAreaRoomError : if in room total wall area is negative.
    # NegativeWindowsAreaRoomWallError : if in a room total windows area is negative.
    # NegativeDoorsAreaRoomWallError : if in room total door area is negative.
    # """

    walls: Walls

    @property
    def walls_area(self) -> float:
        """
        Calculates the total area of all four walls in the room.

        Returns:
        --------
        float:
            The total area of all four walls in the room.

        Raises:
        -------
        NegativeWallAreaRoomError:
            If the total area of the room walls is less than or equal to zero.
        """
        walls_area_ = sum(wall.area for wall in self.walls)
        if walls_area_ <= 0:
            raise NegativeWallAreaRoomError(
                f"The walls area is negative {walls_area_:.2}m2"
            )
        return walls_area_

    @property
    def windows_area(self) -> float:
        """
        Calculates the total area of all windows in the room.

        Returns:
        --------
        float:
            The total area of all windows in the room.

        Raises:
        -------
        NegativeWindowsAreaRoomError:
            If the total area of the room windows is less than zero.
        """
        windows_area_ = sum(wall.windows_area for wall in self.walls)
        if windows_area_ < 0:
            raise NegativeWindowsAreaRoomError(
                f"The windows area in room is negative {windows_area_:.2}m2"
            )
        return sum(wall.windows_area for wall in self.walls)

    @property
    def doors_area(self) -> float:
        """
        Calculates the total area of all doors in the room.

        Returns:
        --------
        float:
            The total area of all doors in the room.

        Raises:
        -------
        NegativeDoorsAreaRoomError:
            If the total area of the room doors is less than zero.
        """
        doors_area_ = sum(wall.doors_area for wall in self.walls)
        if doors_area_ < 0:
            raise NegativeDoorsAreaRoomError(
                f"The door area is negative {doors_area_:.2f}m2"
            )
        return doors_area_

    class Config:
        extra = "forbid"

from src.extensions.logger import log_exceptions
from src.schemas.request.room import Room
from src.schemas.response.paint_cans_needed import PaintCans
from src.services.interfaces.paint_cans_interface import PaintCansInterface


class PaintCansCalculator(PaintCansInterface):
    """
    A class that calculates the number of paint cans required to cover a given
    room area.

    Class `PaintCansCalculator` provides a method `calculate_paint_cans_needed()`
    to calculate the amount of paint cans required to cover a given area, based
    on the dimensions of the room.

    Usage:
    - Instantiate the `PaintCansCalculator` class with the dimensions of the
    room.
    - Call the `calculate_paint_cans_needed()` method to calculate the amount
    of paint cans required to cover the room.
    - The method returns a dictionary that contains the number of paint cans
    required for each size.

    Class-level Attributes:
        _PAINT_COVERAGE_PER_M2 (int): The amount of paint coverage in square meters per liter of paint.
        _PAINT_CAN_SIZES_IN_LITERS (tuple): A tuple of valid paint can sizes in liters.

    Attributes:
        _room (Room): The room whose room area will be painted.

    Methods:
        calculate_paint_cans_needed: Calculates the number of paint cans needed to cover the room area.

    Raises:
        TypeError: If the room argument is not an instance of the Room class.
    """

    __slots__ = "_room"

    _PAINT_COVERAGE_PER_M2 = 5
    _PAINT_CAN_SIZES_IN_LITERS = (0.5, 2.5, 3.6, 18)

    def __init__(self, room: Room) -> None:
        """
        Initializes a new instance of the PaintCansCalculator class.

        Args:
            room (Room): The room whose room area will be painted.

        Raises:
            TypeError: If the room argument is not an instance of the Room class.
        """

        self._room = room

        if not isinstance(room, Room):
            raise TypeError(
                "The room argument must be an instance of the Room class."
            )

    @property
    def room_free_area(self) -> float:
        """
        Calculates the total area of the room that is free from any doors or windows.

        Returns:
            float: The total area of the room that is free from any doors or windows.

        Examples:
            >>> room = Room(walls=[Wall(width=4), Wall(width=4)])
            >>> calculator = PaintCansCalculator(room)
            >>> calculator.room_free_area
            29.0


        """
        try:
            valid_room_free_area = self._room.walls_area - (
                self._room.windows_area + self._room.doors_area
            )
        except Exception:
            raise

        return valid_room_free_area

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"paint_cans_calculator": "calculate_paint_cans_needed"},
    )
    def calculate_paint_cans_needed(self) -> PaintCans:
        """
        Calculates the amount of paint cans needed to paint a room, giving preference
        to the largest possible cans. Ensures that there is no area without paint
        coverage by adding an extra can of the smallest size if necessary.

        Args:
            None

        Returns:
            A dictionary containing the amount of paint cans needed for each size of
            paint can. The keys are the sizes of the paint cans in liters, and the values
            are the number of cans needed for each size.

        Example:
        >>> room = Room(walls=[Wall(width=4.5), Wall(width=3.5, windows=[Window(width=1), Window(width=0.5)]),
                            Wall(width=4.5, doors=[Door(width=1), Door(width=0.8)]), Wall(width=3.5, doors=[Door(width=1), Door(width=0.8)])])
        >>> calculator = PaintCansCalculator(room)
        >>> calculator.calculate_paint_cans_needed()
        {18: 1, 4: 1, 1: 1}

        The above example means that for the given room, one paint can of 18 liters,
        one of 4 liters, and one of 1 liter are needed to paint the walls, ensuring
        that there is no area without paint coverage.

        """

        room_free_area = self.room_free_area
        paint_cans_needed = {}

        try:
            for size in PaintCansCalculator._PAINT_CAN_SIZES_IN_LITERS[::-1]:
                paint_cans_needed[size] = int(
                    room_free_area
                    / PaintCansCalculator._PAINT_COVERAGE_PER_M2
                    / size
                )

                room_free_area -= (
                    paint_cans_needed[size]
                    * PaintCansCalculator._PAINT_COVERAGE_PER_M2
                    * size
                )

            if room_free_area > 0:
                extra_can = 1
                paint_cans_needed[
                    min(PaintCansCalculator._PAINT_CAN_SIZES_IN_LITERS)
                ] += extra_can

        except Exception:
            raise

        return paint_cans_needed

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of this PaintCansCalculator object.

        Returns:
            str: A string representation of the object.
        """
        return f"""
        Paint Cans Calculator:
            room: {self._room}
            room area: {self._room.walls_area:.2f} m²
            windows area: {self._room.windows_area:.2f} m²
            doors area: {self._room.doors_area:.2f} m²
            walls free area: {self.room_free_area:.2f} m²
        """

    def __repr__(self) -> str:
        """
        Returns a string representation of this PaintCansCalculator object.

        Returns:
            str: A string representation of the object.
        """
        return (
            f"PaintCansCalculator(room= {self._room},"
            f"room area= {self._room.walls_area:.2f} m²,"
            f"windows area= {self._room.windows_area:.2f} m²,"
            f"doors area= {self._room.doors_area:.2f} m²,"
            f"walls free area= {self.room_free_area:.2f} m²)"
        )

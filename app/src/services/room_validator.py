from itertools import product
from typing import Callable, Iterator, Tuple

from src.extensions.logger import log_exceptions
from src.schemas.request.room import Room
from src.schemas.wall import Wall
from src.services.exception import (
    InsufficientWallFreeAreaError,
    InvalidRoomDimensionError,
    WallAreaOutOfRangeError,
    WallNotTallerThanDoorError,
    WallNotTallerThanWindowError,
    WallNotWiderThanDoorWindowError,
)

from .interfaces.geometric_validator_interface import (
    GeometricValidatorInterface,
)


class RoomValidator(GeometricValidatorInterface):
    """
    Class `RoomValidator` provides a method `validate_dimensions()` to
    validate the dimensions of a room. After instantiating the class,
    call this method to check if all dimensions are consistent.
    If the dimensions are invalid, the method raises an
    `InvalidRoomDimensionError` exception with a dictionary of invalid errors.

    Usage:
    - Instantiate the `RoomValidator` class with the dimensions of the room.
    - Call the `validate_dimensions()` method to validate the dimensions.
    - If the method returns True, the dimensions are consistent.
    - If the method raises an `InvalidRoomDimensionError`, catch the exception
      to handle the errors.

    Class-level Attributes:
        _MIN_WALL_AREA (float): The minimum allowable total wall area for the room.
        _MAX_WALL_AREA (float): The maximum allowable total wall area for the room.
        _MIN_WALL_FREE_AREA_RATE (float): The minimum allowable ratio of free wall area to total wall area.
        _MIN_DIFFERENCE_WALL_HEIGHT_TALLER_THAN_DOOR_METER (float): The minimum allowable difference between wall free area
            and door + window area

    Attributes:
        room (Room): The room to be validated.

    Methods:
        _validate_dimensions_looper() -> Iterator[Tuple[int, Wall, Callable, Tuple]]:
            Creates a generator to assistant the validate_dimensions() iterating each
            function validator

        validate_dimensions() -> Dict[str, str]:
            Validates the dimensions of the room by checking the wall area range,
            wall free area rate, and the height and width of each wall, door, and window.

        wall_area_within_given_area_range(wall: Wall) -> str | bool:
            Checks if the area of a given wall is within the allowable range.

        wall_free_area_to_paint(wall: Wall) -> float:
            Calculates the amount of free wall area available to paint on a given wall.

        wall_taller_than_door(wall: Wall) -> str | bool:
            Checks if a given wall is taller than the associated door.

        wall_taller_than_window(wall: Wall) -> str | bool:
            Checks if a given wall is taller than the associated window.

        wall_wider_than_amount_door_window(wall: Wall) -> str | bool:
            Checks if a given wall is wider than the associated window.


    Raises:
        TypeError: If the room, door, or window argument is not an instance of the appropriate class.
    """

    __slots__ = "_room"

    _MIN_WALL_AREA = 1
    _MAX_WALL_AREA = 50
    _MIN_WALL_FREE_AREA_RATE = 0.5
    _MIN_DIFFERENCE_WALL_HEIGHT_TALLER_THAN_DOOR_METER = 0.3

    def __init__(self, room: Room) -> None:
        """
        Initializes a new instance of the RoomValidator class.

        Args:
            room: The room to be validated.

        Raises:
            TypeError: If the wall argument is not an instance of the Room class.
        """
        self._room = room

        if not isinstance(room, Room):
            raise TypeError(
                "The room argument must be an instance of the Room class."
            )
        self._room

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "validate_dimensions"},
    )
    def validate_dimensions(self) -> bool:
        """
        Validates the dimensions of the room using the following validation methods:
        - wall_area_within_given_area_range
        - wall_free_area_to_paint
        - wall_taller_than_door
        - wall_taller_than_window
        - wall_wider_than_amount_doors_windows

        Returns:
            If all validations pass, returns True. Otherwise, returns a dictionary containing details of the failed
            validations. The dictionary has the following format:
            {
                "Wall_1": ["error_1", "error_2", ...],
                "Wall_2": ["error_1", "error_2", ...],
                ...
                "Wall_n": ["error_1", "error_2", ...]
            }

        Raises:
            InvalidRoomDimensionError: If any of the validation methods fail.
        """
        try:
            invalid_dimensions_values = {}
            for item in self._validate_dimensions_looper():
                try:
                    index, wall, method, args = [*item]
                    method(wall, *args)

                except (
                    WallAreaOutOfRangeError,
                    InsufficientWallFreeAreaError,
                    WallNotTallerThanDoorError,
                    WallNotTallerThanWindowError,
                    WallNotWiderThanDoorWindowError,
                ) as error:
                    invalid_dimensions_values.setdefault(
                        f"Wall_{index+1}", []
                    ).append(error.args[0])

            if invalid_dimensions_values:
                raise InvalidRoomDimensionError(invalid_dimensions_values)
        except InvalidRoomDimensionError:
            raise
        except Exception:
            raise
        return True

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "_validate_dimensions_looper"},
    )
    def _validate_dimensions_looper(
        self,
    ) -> Iterator[Tuple[int, Wall, Callable, Tuple]]:
        """
        This is a private method that loops through the validation methods and their
        arguments and returns a generator that yields a tuple containing the index of
        the wall being validated, the wall itself, the validation method to be used,
        and the arguments to be passed to the validation method.

        Returns:
            An iterator that yields a tuple containing the index of the wall being
            validated, the wall itself, the validation method to be used, and the
            arguments to be passed to the validation method.
        """
        validation_methods = {
            self.wall_area_within_given_area_range: (),
            self.wall_free_area_to_paint: (),
            self.wall_taller_than_door: (),
            self.wall_taller_than_window: (),
            self.wall_wider_than_amount_doors_windows: (),
        }
        try:
            for index_wall, method_args in product(
                enumerate(self._room.walls), validation_methods.items()
            ):
                index, wall = index_wall[0], index_wall[1]
                method, args = method_args[0], method_args[1]

                yield (index, wall, method, args)
        except Exception:
            raise

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "wall_area_within_given_area_range"},
    )
    def wall_area_within_given_area_range(self, wall: Wall) -> str | bool:
        """
        Checks if the area of a given wall is within the allowable range.

        Args:
            wall (Wall): The wall to be validated.

        Returns:
            bool: Returns True if the wall area is within the allowable range.

        Raises:
            WallAreaOutOfRangeError: If the wall area is out of range.

        Examples:
        >>> wall1 = Wall(width=5, height=2)
        >>> validator = RoomValidator()
        >>> validator.wall_area_within_given_area_range(wall1)
        True
        """
        try:
            wall_area_in_valid_range = (
                RoomValidator._MIN_WALL_AREA
                <= wall.area
                <= RoomValidator._MAX_WALL_AREA
            )
            if not wall_area_in_valid_range:
                raise WallAreaOutOfRangeError(
                    f"The wall area, {wall.area:.2f}m2, is out of "
                    f"range between {RoomValidator._MIN_WALL_AREA}m2 "
                    f"and {RoomValidator._MAX_WALL_AREA}m2."
                )
        except WallAreaOutOfRangeError:
            raise
        except Exception:
            raise
        return wall_area_in_valid_range

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "wall_free_area_to_paint"},
    )
    def wall_free_area_to_paint(self, wall: Wall) -> str | bool:
        """
        Checks if the wall has enough free area to paint, considering the presence of windows and doors.

        Args:
            wall (Wall): The wall to check.

        Returns:
            str | bool: Returns True if the wall has enough free area for the
            openings. If the wall does not have enough free area, returns a string
            explaining the validation error.

        Raises:
        - InsufficientWallFreeAreaError: Raised when a wall does not have enough free area to paint
            due to the presence of windows and doors.

        Examples:
        validator = RoomValidator()
        assert validator.wall_free_area_to_paint(wall, window, door) is True
        """
        try:
            if wall.number_windows or wall.number_doors:
                min_wall_area = wall.area * self._MIN_WALL_FREE_AREA_RATE
                total_area_doors_windows = wall.windows_area + wall.doors_area
                validate_result = min_wall_area >= total_area_doors_windows

                if not validate_result:
                    raise InsufficientWallFreeAreaError(
                        f"The wall free area,"
                        f" {min_wall_area:.2f}"
                        f"m2, must be >= of the total area of"
                        f" windows + doors, {total_area_doors_windows:.2f}m2."
                    )
            validate_result = True
        except InsufficientWallFreeAreaError:
            raise
        except Exception:
            raise
        return validate_result

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "wall_taller_than_door"},
    )
    def wall_taller_than_door(self, wall: Wall) -> str | bool:
        """
        Checks if a wall is taller than a door by at least a minimum height difference.

        Args:
            wall (Wall): The wall to check.

        Returns:
            bool | str: Returns True if the wall is taller than the door by at least
            the minimum height difference, else returns a string explaining how much
            shorter the wall is than the door.

        Raises:
            WallNotTallerThanDoorError: If the wall is not taller than the door by at
            least the minimum height difference.

        Examples:
            >>> wall = Wall(height=3.5, width=10)
            >>> door = Door(height=2.0, width=0.9)
            >>> validator = RoomValidator()
            >>> validator.wall_taller_than_door(wall, door)
            True
        """

        try:
            if wall.number_doors:
                min_wall_height = (
                    wall.door.height
                    + RoomValidator._MIN_DIFFERENCE_WALL_HEIGHT_TALLER_THAN_DOOR_METER
                )
                validate_result = wall.height >= min_wall_height

                if not validate_result:
                    difference_height_door_wall = min_wall_height - wall.height
                    raise WallNotTallerThanDoorError(
                        f"Wall is "
                        f"{difference_height_door_wall:.2f}"
                        f"m shorter than the door."
                    )
            validate_result = True
        except WallNotTallerThanDoorError:
            raise
        except Exception:
            raise
        return validate_result

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "wall_taller_than_window"},
    )
    def wall_taller_than_window(self, wall: Wall) -> str | bool:
        """
        Check if a given wall is taller than a given window.

        Args:
            wall (Wall): The wall to check.
            window (Window): The window to compare against.

        Returns:
            bool | str: Returns True if the wall is taller than the window,
            else returns a string message indicating the height difference
            between the wall and the window.

        Raises:
            WallNotTallerThanWindowError: If the wall is not taller than the window by at least the minimum height difference.

        Example:
            >>> wall = Wall(height=3.5, windows=[Window(height=1.5)])
            >>> window = Window(height=2.5)
            >>> validator = RoomValidator()
            >>> validator.wall_taller_than_window(wall, window)
        "Wall is 1.00m shorter than the window."
        """
        try:
            if wall.number_windows:
                validate_result = wall.height >= wall.window.height

                if not validate_result:
                    difference_height_window_wall = (
                        wall.window.height - wall.height
                    )
                    raise WallNotTallerThanWindowError(
                        f"Wall is {difference_height_window_wall:.2f}m"
                        f" shorter than the window."
                    )
            validate_result = True
        except WallNotTallerThanWindowError:
            raise
        except Exception:
            raise
        return validate_result

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"room_validator": "wall_taller_than_window"},
    )
    def wall_wider_than_amount_doors_windows(self, wall: Wall) -> str | bool:
        """
        Check if the widht of a given amount of doors and walls is wider than a given wall.

        Args:
            wall (Wall): The wall to check.

        Returns:
            bool | str: Returns True if the wall is wider than the window(s),
            else returns a string message indicating the width difference
            between the wall and the window(s).

        Raises:
            WallNotWiderThanDoorWindowError: If the total width of the
              window(s)+ door(s) is wider than the width of the wall.

        Example:
            >>> validator.wall_wider_than_amount_window(wall)
            True
        """
        try:
            if wall.number_windows or wall.number_doors:
                total_window_width = wall.number_windows * wall.window.width
                total_door_width = wall.number_doors * wall.door.width

                total_door_window_width = total_window_width + total_door_width
                validate_result = wall.width >= total_door_window_width

                if not validate_result:
                    raise WallNotWiderThanDoorWindowError(
                        f"Wall is {(total_door_window_width - wall.width):.2f}m"
                        f" narrower than the width of amount of window(s) + doors."
                    )

            validate_result = True
        except WallNotWiderThanDoorWindowError:
            raise
        except Exception:
            raise
        return validate_result

    def __str__(self) -> str:
        """
        Returns a string representation of the RoomValidator instance.

        Returns:
            str: A string containing information about the RoomValidator instance.
        """
        return f"""
        Room Validator:
            _room: {self._room}
            room area: {self._room.walls_area:.2f} m²
            windows area: {self._room.windows_area:.2f} m²
            doors area: {self._room.doors_area:.2f} m²
        """

    def __repr__(self) -> str:
        """
        Returns a string representation of the RoomValidator instance.

        Returns:
            str: A string containing information about the RoomValidator instance.
        """
        return (
            f"RoomValidator(room= {self._room},"
            f"room area= {self._room.walls_area:.2f} m²,"
            f"windows area= {self._room.windows_area:.2f} m²,"
            f"doors area= {self._room.doors_area:.2f} m²,"
        )

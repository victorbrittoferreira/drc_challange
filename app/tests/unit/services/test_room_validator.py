import pytest

from src.services.exception import (
    InsufficientWallFreeAreaError,
    InvalidRoomDimensionError,
    WallAreaOutOfRangeError,
    WallNotTallerThanDoorError,
    WallNotTallerThanWindowError,
    WallNotWiderThanDoorWindowError,
)
from src.services.room_validator import RoomValidator


# ------------------------Class-level Attributes ---------------------------
def test_min_wall_area():
    """
    Tests if the minimum wall area is equal to 1.
    """
    assert RoomValidator._MIN_WALL_AREA == 1


def test_max_wall_area():
    """
    Tests if the maximum wall area is equal to 50.
    """
    assert RoomValidator._MAX_WALL_AREA == 50


def test_min_wall_free_area_rate():
    """
    Tests if the minimum wall free area rate is equal to 0.5.
    """
    assert RoomValidator._MIN_WALL_FREE_AREA_RATE == 0.5


def test_min_difference_wall_height_taller_than_door_meter():
    """
    Tests if the minimum difference between wall height and door height
      is equal to 0.3 meters.
    """
    assert (
        RoomValidator._MIN_DIFFERENCE_WALL_HEIGHT_TALLER_THAN_DOOR_METER == 0.3
    )


# ------------------------------- init ---------------------------
def test_init_with_invalid_arguments():
    """
    Tests if TypeError is raised when an invalid argument is passed as
      input to the constructor of RoomValidator.
    """
    with pytest.raises(TypeError):
        RoomValidator("not a room")


def test_init_with_valid_arguments(validated_room):
    """
    Tests if an instance of RoomValidator is created when valid arguments
      are passed as input to the constructor of RoomValidator.
    """
    room_validator = RoomValidator(validated_room)
    assert room_validator._room == validated_room


# ---------------------------- validate_dimensions ---------------------------
def test_valid_validate_dimensions(validated_room):
    """
    Tests if the method validate_dimensions() returns True when a valid
      room is passed as input.
    """
    room_validator = RoomValidator(validated_room)
    validated_dimensions = room_validator.validate_dimensions()
    assert validated_dimensions is True


def test_invalid_validate_dimensions(validated_room_inconsistent_dimensions):
    """
    Tests if InvalidRoomDimensionError is raised when an invalid room
    with inconsistent dimensions is passed as input to the method
    validate_dimensions().
    """
    room_validator = RoomValidator(validated_room_inconsistent_dimensions)
    with pytest.raises(InvalidRoomDimensionError):
        room_validator.validate_dimensions()


def test_invalid_validate_dimensions_dict_errors(
    validated_room_inconsistent_dimensions, expected_fail_to_process_dimensions
):
    """
    Tests if the exception message from the InvalidRoomDimensionError
    exception is the expected message when an invalid room with inconsistent
      dimensions is passed as input to the method validate_dimensions().
    """
    room_validator = RoomValidator(validated_room_inconsistent_dimensions)
    try:
        room_validator.validate_dimensions()
    except InvalidRoomDimensionError as error:
        assert error.args[0] == expected_fail_to_process_dimensions


# ---------------------- _validate_dimensions_looper -------------------------
def test_raises__validate_dimensions_looper(validated_room):
    """
    Tests if the method _validate_dimensions_looper() returns the expected
      results for a given valid room.
    """
    room_validator = RoomValidator(validated_room)

    expected_results = [
        (i, wall, method, ())
        for i, wall in enumerate(room_validator._room.walls)
        for method in [
            room_validator.wall_area_within_given_area_range,
            room_validator.wall_free_area_to_paint,
            room_validator.wall_taller_than_door,
            room_validator.wall_taller_than_window,
            room_validator.wall_wider_than_amount_doors_windows,
        ]
    ]
    assert (
        list(room_validator._validate_dimensions_looper()) == expected_results
    )


# --------------------- wall_area_within_given_area_range ------------------
def test_valid_wall_area_within_given_area_range(validated_room):
    """
    Tests if the method wall_area_within_given_area_range()
    returns True for a given valid wall.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_area_within_given_area_range(
            room_validator._room.walls[0]
        )
        is True
    )


def test_invalid_bellow_range_wall_area_within_given_area_range(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if WallAreaOutOfRangeError is raised when a wall
      with an area bellow the minimum value is passed as input to the method
        wall_area_within_given_area_range().
    """
    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)
    with pytest.raises(WallAreaOutOfRangeError):
        room_validator.wall_area_within_given_area_range(
            room_validator._room.walls[0]
        )


def test_invalid_above_range_wall_area_within_given_area_range(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if WallAreaOutOfRangeError is raised when a wall with an area
    above the maximum value is passed as input to the
      method wall_area_within_given_area_range().
    """

    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)

    with pytest.raises(WallAreaOutOfRangeError):
        room_validator.wall_area_within_given_area_range(
            room_validator._room.walls[0]
        )


# --------------------- wall_free_area_to_paint ----------------------
def test_valid_wall_free_area_to_paint(validated_room):
    """
    Tests if the method wall_free_area_to_paint() returns True for a given
      valid wall.
    """
    room_validator = RoomValidator(validated_room)

    assert (
        room_validator.wall_free_area_to_paint(room_validator._room.walls[0])
        is True
    )


def test_valid_wall_free_area_to_paint_without_doors_windows(validated_room):
    """
    Tests if the method wall_free_area_to_paint() returns True for a given
      valid wall without doors and windows.
    """
    room_validator = RoomValidator(validated_room)

    assert (
        room_validator.wall_free_area_to_paint(room_validator._room.walls[3])
        is True
    )


def test_insufficient_free_area_wall_free_area_to_paint(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if InsufficientWallFreeAreaError is raised when a wall with
    insufficient free area is passed as input to the method
    wall_free_area_to_paint().
    """
    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)

    with pytest.raises(InsufficientWallFreeAreaError):
        room_validator.wall_free_area_to_paint(room_validator._room.walls[0])


# --------------------- wall_taller_than_door ----------------------
def test_wall_taller_than_door_returns_true_when_wall_is_taller_than_door(
    validated_room,
):
    """
    Tests if the method wall_taller_than_door() returns True for a given
      valid wall that is taller than the minimum height required for a door.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_taller_than_door(room_validator._room.walls[0])
        is True
    )


def test_wall_taller_than_door_returns_true_when_wall_has_no_doors(
    validated_room,
):
    """
    Tests if the method wall_taller_than_door() returns True for a given
    valid wall that has no doors.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_taller_than_door(room_validator._room.walls[3])
        is True
    )


def test_wall_taller_than_door_raises_error_when_wall_is_shorter_than_door(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if WallNotTallerThanDoorError is raised when a wall with
    insufficient width is passed as input to the
    method wall_wider_than_amount_doors_windows:"""
    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)
    with pytest.raises(WallNotTallerThanDoorError):
        room_validator.wall_taller_than_door(room_validator._room.walls[0])


# --------------------- wall_taller_than_window ----------------------
def test_wall_taller_than_window_with_tall_wall(validated_room):
    """
    Tests that the method wall_taller_than_window_with_tall_walls returns
    True when called with a wall that is taller than the window on that wall.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_taller_than_window(room_validator._room.walls[0])
        is True
    )


def test_wall_taller_than_window_with_no_window(validated_room):
    """
    Tests if the method wall_taller_than_window returns True for a given
    valid wall that has no  windows.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_taller_than_window(room_validator._room.walls[3])
        is True
    )


def test_wall_taller_than_window_with_short_wall(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if WallNotTallerThanWindowError is raised when a wall with
    insufficient width is passed as input to the method
    wall_taller_than_window"""
    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)
    with pytest.raises(WallNotTallerThanWindowError):
        room_validator.wall_taller_than_window(room_validator._room.walls[0])


# ---------------- wall_wider_than_amount_doors_windows -----------------
def test_wall_wider_than_amount_doors_windows_with_wider_wall(validated_room):
    """
    Tests that the method wall_wider_than_amount_doors_windows returns
    True when called with a wall that is wider than the windows and doors
    on that wall.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_wider_than_amount_doors_windows(
            room_validator._room.walls[0]
        )
        is True
    )


def test_wall_wider_than_amount_doors_windows_with_no_window_or_wall(
    validated_room,
):
    """
    Tests if the method wall_wider_than_amount_doors_windows returns True for a given
    valid wall that has no doors or windows.
    """
    room_validator = RoomValidator(validated_room)
    assert (
        room_validator.wall_wider_than_amount_doors_windows(
            room_validator._room.walls[3]
        )
        is True
    )


def test_wall_wider_than_amount_doors_windows_with_narrow_wall(
    validated_room_inconsistent_dimensions_2,
):
    """
    Tests if WallNotWiderThanDoorWindowError is raised when a wall with
    insufficient width is passed as input to the method
    wall_wider_than_amount_doors_windows"""
    room_validator = RoomValidator(validated_room_inconsistent_dimensions_2)
    with pytest.raises(WallNotWiderThanDoorWindowError):
        room_validator.wall_wider_than_amount_doors_windows(
            room_validator._room.walls[0]
        )

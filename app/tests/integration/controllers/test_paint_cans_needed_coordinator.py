import pytest

from src.controllers.paint_cans_needed_coordinator import (
    PaintCansNeededCoordinator,
)
from src.services.exception import InvalidRoomDimensionError


def test_init_with_invalid_geometric_validator(paint_cans_validator_instance):
    """
    Test for initialization with an invalid geometric validator. Raises a
    TypeError exception with an error message if the geometric validator
    is not a subclass of GeometricValidatorInterface.
    """
    with pytest.raises(TypeError) as exc_info:
        PaintCansNeededCoordinator(paint_cans_validator_instance, None)
    assert str(exc_info.value) == (
        "The geometric_validator attribute must be an instance of"
        " subclass GeometricValidatorInterface."
    )


def test_init_with_invalid_paint_can_needed_calculator(
    room_validator_instance,
):
    """
    Test for initialization with an invalid paint can needed calculator.
    Raises a TypeError exception with an error message if the paint can
    needed calculator is not a subclass of PaintCansInterface.
    """
    with pytest.raises(TypeError) as exc_info:
        PaintCansNeededCoordinator(room_validator_instance, None)
    assert str(exc_info.value) == (
        "The paint_can_needed_calculator attribute must be an"
        " instance of subclass PaintCansInterface."
    )


def test_init_with_invalid_room_dimensions(
    invalid_room_validator_instance, invalid_paint_cans_validator_instance
):
    """
    Test for initialization with invalid room dimensions. Raises an
    InvalidRoomDimensionError exception if the room dimensions fail
     validation.
    """
    with pytest.raises(InvalidRoomDimensionError):
        PaintCansNeededCoordinator(
            invalid_room_validator_instance,
            invalid_paint_cans_validator_instance,
        ).validate_geometric_object()


def test_init_with_valid_room_dimensions(
    room_validator_instance,
    paint_cans_validator_instance,
    expected_return_calculate_paint_cans_needed,
):
    """
    Test for initialization with valid room dimensions. Calculates the
    required number of paint cans using the given room validator and
    paint can needed calculator, and asserts that the result matches
    the expected result.
    """
    coordinator = PaintCansNeededCoordinator(
        room_validator_instance, paint_cans_validator_instance
    )
    assert (
        coordinator.get_paint_cans_needed()
        == expected_return_calculate_paint_cans_needed
    )

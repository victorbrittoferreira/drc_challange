import pytest
from pydantic import ValidationError

from src.controllers.main_controller import PaintCansController
from src.controllers.paint_cans_needed_coordinator import (
    PaintCansNeededCoordinator,
)
from src.schemas.request.room import Room
from src.schemas.response.paint_cans_needed import PaintCansNeeded


def test_validate_response_with_valid_data(
    valid_room,
    room_validator_instance,
    paint_cans_validator_instance,
    expected_return_calculate_paint_cans_needed,
):
    """
    Test if the function returns a PaintCansNeeded object with validated
    data when given valid input data.
    """
    valid_instances = PaintCansNeededCoordinator(
        room_validator_instance, paint_cans_validator_instance
    )
    result = PaintCansController(Room(**valid_room))
    assert result._validate_response(valid_instances) == PaintCansNeeded(
        paint_cans=expected_return_calculate_paint_cans_needed
    )


def test_calculate_paint_cans_needed_controller(
    valid_room, expected_return_calculate_paint_cans_needed
):
    expected_paint_cans = PaintCansNeeded(
        paint_cans=expected_return_calculate_paint_cans_needed
    )
    """
    Test if the function returns the expected number of paint cans needed
    to paint a valid room.
    """
    result = PaintCansController(Room(**valid_room))

    assert (
        result.calculate_paint_cans_needed_controller() == expected_paint_cans
    )


def test_calculate_paint_cans_needed_controller_invalid(
    invalid_room_dimensions,
):
    """
    Test if the function raises a ValidationError when given invalid room
    dimensions.
    """
    result = PaintCansController(Room(**invalid_room_dimensions))
    with pytest.raises(ValidationError):
        result.calculate_paint_cans_needed_controller()

import pytest

from src.services.paint_cans_needed_calculator import PaintCansCalculator

# --------------------------- constant attributes --------------------


def test_paint_coverage_per_m2():
    """Tests if the value of the constant attribute _PAINT_COVERAGE_PER_M2
    is 5.
    """
    assert PaintCansCalculator._PAINT_COVERAGE_PER_M2 == 5


def test_paint_can_sizes():
    """
    Tests if the value of the constant attribute _PAINT_CAN_SIZES_IN_LITERS
    is a tuple containing the values 0.5, 2.5, 3.6, and 18.
    """
    assert PaintCansCalculator._PAINT_CAN_SIZES_IN_LITERS == (
        0.5,
        2.5,
        3.6,
        18,
    )


# -------------------------------- init ---------------------------
def test_init_with_invalid_arguments():
    """
    Tests if an instance of PaintCansCalculator cannot be created with
     an invalid argument (in this case, a string).
    """
    with pytest.raises(TypeError):
        PaintCansCalculator("not a room")


def test_init_with_valid_arguments(validated_room):
    """
    Tests if an instance of PaintCansCalculator can be created with
     a valid argument (in this case, a Room object).
    """
    paint_cans_calculator = PaintCansCalculator(validated_room)
    assert paint_cans_calculator._room == validated_room


# ----------------------- @property_room_free_area --------------------


def test_room_free_area_no_doors_or_windows(validated_room):
    """
    Tests if the room_free_area property returns the expected value
    when there are no doors or windows in the room.
    """
    paint_cans_calculator = PaintCansCalculator(validated_room)
    expected_room_free_area = 125.84
    assert paint_cans_calculator.room_free_area == expected_room_free_area


# ---------------   calculate_paint_cans_needed    ------------------------


def test_calculate_paint_cans_needed(
    validated_room,
    expected_return_calculate_paint_cans_needed,
):
    """
    Tests if the calculate_paint_cans_needed method returns the expected
    value of paint cans needed to cover the room.
    """
    paint_cans_calculator = PaintCansCalculator(validated_room)
    assert (
        paint_cans_calculator.calculate_paint_cans_needed()
        == expected_return_calculate_paint_cans_needed
    )

import pytest

from src.schemas.response.paint_cans_needed import PaintCansNeeded


def test_paint_cans_needed_valid():
    """
    Tests if the values of the paint cans dict are valid, greater or
    equal zero
    """
    paint_cans_dict = {1.5: 2, 2.5: 1}
    paint_cans_needed = PaintCansNeeded(paint_cans=paint_cans_dict)
    assert paint_cans_needed.paint_cans == paint_cans_dict


def test_paint_cans_needed_negative_values():
    """
    Tests if the values of the paint cans dict are invalid, less than
     zero

    """
    paint_cans_dict = {1.5: 2, 2.5: -1}
    with pytest.raises(ValueError):
        PaintCansNeeded(paint_cans=paint_cans_dict)

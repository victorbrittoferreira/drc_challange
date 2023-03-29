from pytest import approx

from src.schemas.request.room import Room


# ------------------------ wall_area -------------------
def test_valid_walls_area(valid_room):
    """
    Test to verify if the walls total area  calculation is correct
    """
    validated_room = Room(**valid_room)
    walls_total_area = 140.0
    assert validated_room.walls_area == approx(walls_total_area)


# ------------------------ windows_area -------------------
def test_valid_windows_area(valid_room):
    """
    Test to verify if the windows total area  calculation is correct
    """
    validated_room = Room(**valid_room)
    windows_total_area = 9.6
    assert validated_room.windows_area == approx(windows_total_area)


# ------------------------ door_area -------------------
def test_valid_doors_area(valid_room):
    """
    Test to verify if the doors total area  calculation is correct
    """
    validated_room = Room(**valid_room)
    doors_total_area = 4.56
    assert validated_room.doors_area == approx(doors_total_area)

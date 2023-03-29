from pytest import raises

from src.schemas.door import Door


def test_create_door_with_non_numeric_width():
    """
    Test that creating a door with a non-numeric width raises
     a ValueError.
    """
    with raises(ValueError):
        Door("foo", 4.0)


def test_create_door_with_non_numeric_height():
    """
    Test that creating a door with a non-numeric height raises
     a ValueError.
    """
    with raises(ValueError):
        Door(3.0, "bar")


def test_create_door_with_zero_width():
    """
    Test that creating a door with a width of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Door(0.0, 4.0)


def test_create_door_with_zero_height():
    """
    Test that creating a door with a height of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Door(3.0, 0.0)


def test_door_area():
    """
    Test that creating of Door instance.
    """
    door = Door(3.0, 4.0)
    assert door.area == 12.0
    assert door.height == 4.0
    assert door.width == 3.0
    assert isinstance(door, Door)

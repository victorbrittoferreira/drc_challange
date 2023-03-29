from pytest import raises

from src.schemas.base_schema_geometric import Rectangle


def test_create_rectangle_with_non_numeric_width():
    """
    Test that creating a rectangle with a non-numeric width raises
     a ValueError.
    """
    with raises(ValueError):
        Rectangle("foo", 4.0)


def test_create_rectangle_with_non_numeric_height():
    """
    Test that creating a rectangle with a non-numeric height raises
     a ValueError.
    """
    with raises(ValueError):
        Rectangle(3.0, "bar")


def test_create_rectangle_with_zero_width():
    """
    Test that creating a rectangle with a width of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Rectangle(0.0, 4.0)


def test_create_rectangle_with_zero_height():
    """
    Test that creating a rectangle with a height of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Rectangle(3.0, 0.0)

from pytest import raises

from src.schemas.window import Window


def test_create_window_with_non_numeric_width():
    """
    Test that creating a window with a non-numeric width raises
     a ValueError.
    """
    with raises(ValueError):
        Window("foo", 4.0)


def test_create_window_with_non_numeric_height():
    """
    Test that creating a window with a non-numeric height raises
     a ValueError.
    """
    with raises(ValueError):
        Window(3.0, "bar")


def test_create_window_with_zero_width():
    """
    Test that creating a window with a width of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Window(0.0, 4.0)


def test_create_window_with_zero_height():
    """
    Test that creating a window with a height of zero raises
     a ValueError.
    """
    with raises(ValueError):
        Window(3.0, 0.0)


def test_window_area():
    """
    Test that creating of Window instance.
    """
    window = Window(3.0, 4.0)
    assert window.area == 12.0
    assert window.height == 4.0
    assert window.width == 3.0
    assert isinstance(window, Window)

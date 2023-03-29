import pytest

from src.services.interfaces.paint_cans_interface import PaintCansInterface


def test_subclasshook():
    """
    Tests whether a class that implements the validate_dimensions method is
    considered a subclass of PaintCansInterface using the
      issubclass function.
    """

    class ValidatingClass:
        def calculate_paint_cans_needed():
            pass

    assert issubclass(ValidatingClass, PaintCansInterface)


def test_subclasshook_fail():
    """
    Tests whether a class that does not implement the validate_dimensions
    method is not considered a subclass of PaintCansInterface
    using the issubclass function.
    """

    class InvalidClass:
        pass

    assert not issubclass(InvalidClass, PaintCansInterface)


def test_validate_dimensions():
    """
    Tests whether an instance of PaintCansInterface raises a
    TypeError when the abstract method validate_dimensions is called.
    """
    with pytest.raises(TypeError):
        PaintCansInterface().calculate_paint_cans_needed()


def test_str():
    """
    Tests whether the str function raises a TypeError when called on
    an instance of PaintCansInterface.
    """
    with pytest.raises(TypeError):
        str(PaintCansInterface())


def test_repr():
    """
    Tests whether the repr function raises a TypeError when called
    on an instance of PaintCansInterface.
    """
    with pytest.raises(TypeError):
        repr(PaintCansInterface())

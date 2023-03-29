import pytest

from src.services.interfaces.geometric_validator_interface import (
    GeometricValidatorInterface,
)


def test_subclasshook():
    """
    Tests whether a class that implements the validate_dimensions method is
    considered a subclass of GeometricValidatorInterface using the
      issubclass function.
    """

    class ValidatingClass:
        def validate_dimensions():
            pass

    assert issubclass(ValidatingClass, GeometricValidatorInterface)


def test_subclasshook_fail():
    """
    Tests whether a class that does not implement the validate_dimensions
    method is not considered a subclass of GeometricValidatorInterface
    using the issubclass function.
    """

    class InvalidClass:
        pass

    assert not issubclass(InvalidClass, GeometricValidatorInterface)


def test_validate_dimensions():
    """
    Tests whether an instance of GeometricValidatorInterface raises a
    TypeError when the abstract method validate_dimensions is called.
    """
    with pytest.raises(TypeError):
        GeometricValidatorInterface().validate_dimensions()


def test_str():
    """
    Tests whether the str function raises a TypeError when called on
    an instance of GeometricValidatorInterface.
    """
    with pytest.raises(TypeError):
        str(GeometricValidatorInterface())


def test_repr():
    """
    Tests whether the repr function raises a TypeError when called
    on an instance of GeometricValidatorInterface.
    """
    with pytest.raises(TypeError):
        repr(GeometricValidatorInterface())

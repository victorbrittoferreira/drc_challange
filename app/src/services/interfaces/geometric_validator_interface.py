from abc import ABCMeta, abstractmethod


class GeometricValidatorInterface(metaclass=ABCMeta):
    """
    Interface for validating geometric objects.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "validate_dimensions")
            and callable(subclass.validate_dimensions)
            or NotImplemented
        )

    @abstractmethod
    def validate_dimensions(self):
        """
        Validates if a given geometric object is within an acceptable geometric measurements

        Returns a string representation of the GeometricValidatorInterface.

        """
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the GeometricValidatorInterface.
        """
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the GeometricValidatorInterface.
        """
        raise NotImplementedError

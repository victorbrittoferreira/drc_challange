from abc import ABCMeta, abstractmethod


class PaintCansInterface(metaclass=ABCMeta):
    """
    Interface for paint cans calculators.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "calculate_paint_cans_needed")
            and callable(subclass.calculate_paint_cans_needed)
            or NotImplemented
        )

    @abstractmethod
    def calculate_paint_cans_needed(self):
        """
        Calculates how many paint cans are needed to cover given geometric object.

        Returns a string representation of the PaintCansInterface.

        """
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the PaintCansInterface.
        """
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the PaintCansInterface.
        """
        raise NotImplementedError

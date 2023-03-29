from typing import Type

from src.extensions.logger import log_exceptions
from src.schemas.response.paint_cans_needed import PaintCans
from src.services.exception import InvalidRoomDimensionError
from src.services.interfaces.geometric_validator_interface import (
    GeometricValidatorInterface,
)
from src.services.interfaces.paint_cans_interface import PaintCansInterface


class PaintCansNeededCoordinator:
    def __init__(
        self,
        geometric_validator: Type[GeometricValidatorInterface],
        paint_can_needed_calculator: Type[PaintCansInterface],
    ) -> None:
        """
        Initializes a `PaintCansNeededCoordinator` instance with a
        `geometric_validator` and a `paint_can_needed_calculator` to validate
        the room dimensions and calculate the paint cans needed,
        respectively.

        Args:
            - geometric_validator: A `GeometricValidatorInterface` instance to
              validate the room dimensions.
            - paint_can_needed_calculator: A `PaintCansInterface` instance to
              calculate the paint cans needed.

        Raises:
            - TypeError: If `geometric_validator` or
                `paint_can_needed_calculator` is not an instance of
                `GeometricValidatorInterface` or `PaintCansInterface`,
                respectively.
            - UnprocessedGeometricObject: If the room dimensions are invalid.
        """

        if not isinstance(geometric_validator, GeometricValidatorInterface):
            raise TypeError(
                "The geometric_validator attribute must be an instance of"
                " subclass GeometricValidatorInterface."
            )

        if not isinstance(paint_can_needed_calculator, PaintCansInterface):
            raise TypeError(
                "The paint_can_needed_calculator attribute must be an"
                " instance of subclass PaintCansInterface."
            )

        self._geometric_validator = geometric_validator
        self._paint_can_needed_calculator = paint_can_needed_calculator
        self._validated_dimensions: bool = None
        self.paint_can_needed = None

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"paint_cans_needed_coordinator": "validate_geometric_object"},
    )
    def validate_geometric_object(self) -> bool:
        """
        Validates the dimensions of a geometric object and stores the validated dimensions in the
        _validated_dimensions attribute.

        Returns:
            The validated dimensions of the geometric object.

        Raises:
            InvalidRoomDimensionError: If the dimensions of the geometric object fail validation.
        """
        try:
            self._validated_dimensions = (
                self._geometric_validator.validate_dimensions()
            )
        except InvalidRoomDimensionError:
            raise
        except Exception:
            raise
        return self._validated_dimensions

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"paint_cans_needed_coordinator": "get_paint_cans_needed"},
    )
    def get_paint_cans_needed(self) -> PaintCans:
        """
        Returns the calculated number of paint cans needed for each color.

        Returns:
            A dictionary with the number of paint cans needed for each color.

        """
        try:
            if self._validated_dimensions is None:
                self.validate_geometric_object()
            if self._validated_dimensions:
                self.paint_can_needed = (
                    self._paint_can_needed_calculator.calculate_paint_cans_needed()
                )
        except Exception:
            raise
        return self.paint_can_needed

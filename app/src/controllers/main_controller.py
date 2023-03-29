from pydantic import ValidationError

from src.controllers.paint_cans_needed_coordinator import (
    PaintCansNeededCoordinator,
)
from src.extensions.logger import log_exceptions
from src.schemas.request.room import Room
from src.schemas.response.paint_cans_needed import PaintCansNeeded
from src.schemas.response.unprocessable_geometric_object import (
    UnprocessedGeometricObject,
)
from src.services.exception import InvalidRoomDimensionError
from src.services.paint_cans_needed_calculator import PaintCansCalculator
from src.services.room_validator import RoomValidator


class PaintCansController:
    """
    A controller class that handles the logic for calculating the amount of paint cans needed to paint a room.

    Attributes:
        room: A Room object representing the room to be painted.

    Methods:
        validate_response(paint_can_service): Validates the response from the PaintCansNeededCoordinator object
        and returns the validated data in a PaintCansNeeded object.

        calculate_paint_cans_needed_controller(): Calculates the amount of paint cans needed to paint the room
        and returns a PaintCansNeeded object containing the number of paint cans needed for each color.

    Raises:
        ValidationError: If the input room object fails validation.
    """

    def __init__(self, room: Room):
        self.room = room

        if not isinstance(room, Room):
            raise TypeError(
                "The room argument must be an instance of the Room class."
            )

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={"paint_cans_controller": "_validate_response"},
    )
    def _validate_response(
        self, paint_can_service: PaintCansNeededCoordinator
    ) -> PaintCansNeeded | UnprocessedGeometricObject:
        """
        Validates the response from the PaintCansNeededCoordinator object and returns the validated data
        in a PaintCansNeeded object.

        Args:
            paint_can_service: A PaintCansNeededCoordinator object representing the service for calculating
            the amount of paint cans needed to paint the room.

        Returns:
            A PaintCansNeeded object containing the number of paint cans needed for each color.

        Raises:
            UnprocessedGeometricObject: If the input room object fails validation or if there is an error in
            the PaintCansNeededCoordinator object.
        """
        try:
            validated_geometric_object = (
                paint_can_service.validate_geometric_object()
            )
            if validated_geometric_object:
                validated_data = paint_can_service.get_paint_cans_needed()
                validated_data_response = PaintCansNeeded(
                    paint_cans=validated_data
                )
        except InvalidRoomDimensionError as error:
            return UnprocessedGeometricObject(errors=error.args[0])
        except Exception:
            raise

        return validated_data_response

    @log_exceptions(
        msg="exception_paint_cans_calculator_service",
        extra={
            "paint_cans_controller": "calculate_paint_cans_needed_controller"
        },
    )
    def calculate_paint_cans_needed_controller(self) -> PaintCansNeeded:
        """
        Calculates the amount of paint cans needed to paint the room and returns a PaintCansNeeded object
        containing the number of paint cans needed for each color.

        Returns:
            A PaintCansNeeded object containing the number of paint cans needed for each color.

        Raises:
            ValidationError: If the input room object fails validation.
        """
        try:
            room_validator = RoomValidator(self.room)
            paint_cans_calculator = PaintCansCalculator(self.room)

            paint_can_service = PaintCansNeededCoordinator(
                room_validator, paint_cans_calculator
            )
            validated_data_response = self._validate_response(
                paint_can_service
            )
        except ValidationError:
            raise
        except Exception:
            raise

        return validated_data_response

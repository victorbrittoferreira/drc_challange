from src.entities.paint_can import PaintCanToBuy
from src.entities.room import Room

PAINT_COVERAGE_PER_SQUARE_METERS = 5

STANDART_PAINT_CAN_SIZES_IN_LITERS = (0.5, 2.5, 3.6, 18)


def get_paint_can_buy_list(room: Room) -> PaintCanToBuy:
    square_meters_to_be_covered = room.walls_area - (
        room.windows_area + room.doors_area
    )
    paint_needed_in_liters = (
        square_meters_to_be_covered / PAINT_COVERAGE_PER_SQUARE_METERS
    )

    paint_can_buy_list = []

    for paint_can in STANDART_PAINT_CAN_SIZES_IN_LITERS[::-1]:
        quotient, remainder = divmod(paint_needed_in_liters, paint_can)
        if quotient > 0:
            [
                paint_can_buy_list.append(paint_can)
                for _ in range(int(quotient))
            ]
            paint_needed_in_liters = remainder

    if paint_needed_in_liters > 0:
        paint_can_buy_list.append(STANDART_PAINT_CAN_SIZES_IN_LITERS[0])
    validated_paint_can_list = PaintCanToBuy(paint_can_list=paint_can_buy_list)

    # return paint_can_buy_list
    return validated_paint_can_list

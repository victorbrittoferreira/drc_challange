from src.entities.door import DEFAULT_DOOR, Door
from src.entities.room import Room
from src.entities.wall import Wall
from src.entities.window import DEFAULT_WINDOW, Window


def verify_room_area(room: Room) -> bool:
    return (room.walls_area * 0.5) >= (room.windows_area + room.doors_area)


def verify_wall_area(wall: Wall) -> bool:
    return 1 <= wall.area <= 50


def verify_wall_with_door_height(wall: Wall, door: Door) -> bool:
    return wall.height >= (door.height + 0.3) if wall.doors else True


def check_if_the_wall_width_is_less_than_window_and_door(
    wall: Wall, window: Window, door: Door
) -> bool:
    if wall.doors is True:
        door_width = wall.doors * door.width
        return wall.width > door_width

    if wall.windows is True:
        window_width = wall.windows * window.width
        return wall.width > window_width

    return True


def check_if_the_wall_height_is_less_than_window_and_door(
    wall: Wall, window: Window, door: Door
) -> bool:
    if wall.doors is True:
        door_height = wall.doors * door.height
        return wall.height > door_height

    if wall.windows is True:
        window_height = wall.windows * window.height
        return wall.height > window_height

    return True


# TODO: PYDANTIC ValidationException


def validate_room_data(room: Room) -> bool:
    if not verify_room_area(room):
        return False

    for wall in room.walls:
        if not verify_wall_area(wall):
            return False
        if not verify_wall_with_door_height(wall, DEFAULT_DOOR):
            return False
        if not check_if_the_wall_width_is_less_than_window_and_door(
            wall, DEFAULT_WINDOW, DEFAULT_DOOR
        ):
            return False
        if not check_if_the_wall_height_is_less_than_window_and_door(
            wall, DEFAULT_WINDOW, DEFAULT_DOOR
        ):
            return False

    return True

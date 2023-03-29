import pytest
from fastapi.testclient import TestClient

from src.api import create_api
from src.schemas.request.room import Room
from src.services.paint_cans_needed_calculator import PaintCansCalculator
from src.services.room_validator import RoomValidator


# ----------------------- API ---------------------------
@pytest.fixture(scope="function")
def api():
    return create_api()


@pytest.fixture(scope="function")
def api_client(api):
    with TestClient(api) as api_client:
        yield api_client


# ------------------- TYPE TEST -----------------------------
basic_types = [
    2,
    1.2,
    "string",
    (),
    [],
    {},
    set([]),
    frozenset({}),
    lambda: "function",
    type("MyClass", (object,), {}),
    None,
    True,
]

# --------------------- E2E -------------------------------
# SUCESS SUBSESSION


@pytest.fixture(scope="function")
def valid_request_payload_walls_dimensions():
    return {
        "walls": [
            {"width": 7, "height": 5, "number_doors": 1, "number_windows": 2},
            {"width": 7, "height": 5, "number_doors": 2, "number_windows": 2},
            {"width": 7, "height": 5, "number_doors": 0, "number_windows": 0},
            {"width": 7, "height": 5, "number_doors": 0, "number_windows": 0},
        ]
    }


@pytest.fixture(scope="function")
def json_response_successful():
    return {"paint_cans": {"0.5": 3, "18.0": 1, "2.5": 1, "3.6": 1}}


# FAIL SUBSESSION
@pytest.fixture(scope="function")
def invalid_request_payload_walls_dimensions():
    return {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }


@pytest.fixture(scope="function")
def invalid_request_payload_walls_dimensions_2():
    return {
        "walls": [
            {
                "width": -1,
                "height": -0.1,
                "number_doors": "b",
                "number_windows": [],
            },
            {
                "width": "",
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }


@pytest.fixture(scope="function")
def invalid_request_payload_walls_dimensions_3():
    return {
        "walls": [
            {
                "width": -1,
                "height": -0.1,
                "number_doors": "b",
                "number_windows": [],
            },
            {
                "width": "",
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
        ]
    }


@pytest.fixture(scope="function")
def json_response_expected_fail_to_process_dimensions():
    return [
        {
            "loc": ["errors"],
            "msg": "Was/Were found inconsistent(cies) geometrics value(s) input.",
            "type": "value_error.geometric_inconsistencies_found",
            "ctx": {
                "walls": {
                    "Wall_1": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 7.84m2.",
                        "Wall is 2.10m shorter than the door.",
                        "Wall is 1.10m shorter than the window.",
                        "Wall is 5.50m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_2": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 1.52m2.",
                        "Wall is 2.10m shorter than the door.",
                        "Wall is 0.70m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_3": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 2.40m2.",
                        "Wall is 1.10m shorter than the window.",
                        "Wall is 1.90m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_4": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2."
                    ],
                }
            },
        }
    ]


@pytest.fixture(scope="function")
def json_response_expected_fail_to_process_dimensions2():
    return {
        "detail": [
            {
                "loc": ["body", "walls", 0, "width"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 0},
            },
            {
                "loc": ["body", "walls", 0, "height"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 0},
            },
            {
                "loc": ["body", "walls", 0, "number_doors"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            },
            {
                "loc": ["body", "walls", 0, "number_windows"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            },
            {
                "loc": ["body", "walls", 1, "width"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            },
        ]
    }


@pytest.fixture(scope="function")
def json_response_expected_fail_to_process_dimensions_3():
    return [
        {
            "loc": ["errors"],
            "msg": "Was/Were found inconsistent(cies) geometrics value(s) input.",
            "type": "value_error.geometric_inconsistencies_found",
            "ctx": {
                "walls": {
                    "Wall_1": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 6.08m2.",
                        "Wall is 2.10m shorter than the door.",
                        "Wall is 1.10m shorter than the window.",
                        "Wall is 5.50m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_2": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 1.52m2.",
                        "Wall is 2.10m shorter than the door.",
                        "Wall is 0.70m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_3": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                        "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 1.52m2.",
                        "Wall is 1.10m shorter than the window.",
                        "Wall is 1.90m narrower than the width of amount of window(s) + doors.",
                    ],
                    "Wall_4": [
                        "The wall area, 0.01m2, is out of range between 1m2 and 50m2."
                    ],
                }
            },
        }
    ]


@pytest.fixture(scope="function")
def json_response_expected_fail_to_process_dimensions3():
    return {
        "detail": [
            {
                "loc": ["body", "walls"],
                "msg": "wrong tuple length 3, expected 4",
                "type": "value_error.tuple.length",
                "ctx": {"actual_length": 3, "expected_length": 4},
            }
        ]
    }


# ---------------------- INTEGRATIONS ------------------------
@pytest.fixture(scope="function")
def room_validator_instance():
    valid_room = {
        "walls": [
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 1,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }
    room_validator = RoomValidator(Room(**valid_room))

    return room_validator


@pytest.fixture(scope="function")
def paint_cans_validator_instance():
    valid_room = {
        "walls": [
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 1,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }
    paint_cans_calculator = PaintCansCalculator(Room(**valid_room))
    return paint_cans_calculator


@pytest.fixture(scope="function")
def invalid_room_validator_instance():
    valid_room = {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }
    room_validator = RoomValidator(Room(**valid_room))

    return room_validator


@pytest.fixture(scope="function")
def invalid_paint_cans_validator_instance():
    valid_room = {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }
    paint_cans_calculator = PaintCansCalculator(Room(**valid_room))
    return paint_cans_calculator


# ------------------------- UNIT -----------------------------
# --------------- SCHEMAS ----------------


@pytest.fixture(scope="function")
def valid_room():
    return {
        "walls": [
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 1,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
            {
                "width": 7.0,
                "height": 5.0,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }


@pytest.fixture(scope="function")
def invalid_room_dimensions():
    return {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }


# --------------------- SERVICES -----------------------
# SUBSSESION --------- valid inputs


@pytest.fixture(scope="function")
def validated_room():
    valid_request_room_data = {
        "walls": [
            {"width": 7, "height": 5, "number_doors": 1, "number_windows": 2},
            {"width": 7, "height": 5, "number_doors": 2, "number_windows": 2},
            {"width": 7, "height": 5, "number_doors": 0, "number_windows": 0},
            {"width": 7, "height": 5, "number_doors": 0, "number_windows": 0},
        ]
    }
    validated_room_ = Room(**valid_request_room_data)
    return validated_room_


# SUBSSESION ---------  inconsistent_room_dimensions ------------


@pytest.fixture(scope="function")
def validated_room_inconsistent_dimensions():
    valid_request_room_data_inconsistent_dimensions = {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }

    valid_request_room_data_ = Room(
        **valid_request_room_data_inconsistent_dimensions
    )
    return valid_request_room_data_


@pytest.fixture(scope="function")
def validated_room_inconsistent_dimensions_2():
    valid_request_room_data_inconsistent_dimensions = {
        "walls": [
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 2,
                "number_windows": 2,
            },
            {
                "width": 10,
                "height": 10,
                "number_doors": 1,
                "number_windows": 0,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 1,
            },
            {
                "width": 0.1,
                "height": 0.1,
                "number_doors": 0,
                "number_windows": 0,
            },
        ]
    }

    valid_request_room_data_ = Room(
        **valid_request_room_data_inconsistent_dimensions
    )
    return valid_request_room_data_


# SUBSSESION ------------- expected output------------------------
@pytest.fixture(scope="function")
def expected_return_calculate_paint_cans_needed():
    return {18: 1, 3.6: 1, 2.5: 1, 0.5: 3}


# SUBSSESION ----------- unexpected output------------------------
@pytest.fixture(scope="function")
def expected_fail_to_process_dimensions():
    return {
        "Wall_1": [
            "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
            "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 7.84m2.",
            "Wall is 2.10m shorter than the door.",
            "Wall is 1.10m shorter than the window.",
            "Wall is 5.50m narrower than the width of amount of window(s) + doors.",
        ],
        "Wall_2": [
            "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
            "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 1.52m2.",
            "Wall is 2.10m shorter than the door.",
            "Wall is 0.70m narrower than the width of amount of window(s) + doors.",
        ],
        "Wall_3": [
            "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
            "The wall free area, 0.01m2, must be >= of the total area of windows + doors, 2.40m2.",
            "Wall is 1.10m shorter than the window.",
            "Wall is 1.90m narrower than the width of amount of window(s) + doors.",
        ],
        "Wall_4": [
            "The wall area, 0.01m2, is out of range between 1m2 and 50m2."
        ],
    }

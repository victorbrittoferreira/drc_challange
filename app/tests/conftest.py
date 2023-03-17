import pytest
from fastapi.testclient import TestClient
from src.api import create_api


@pytest.fixture(scope="function")
def api():
    return create_api()


@pytest.fixture(scope="function")
def api_client(api):
    with TestClient(api) as api_client:
        yield api_client


invalid_basic_types_list = [
    9999,
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

# --------------------- ENTITIES -----------------------------


@pytest.fixture(scope="function")
def correct_wall_size():
    return {"length": 1.2, "width": 1.3, "doors": 1, "windows": 1}

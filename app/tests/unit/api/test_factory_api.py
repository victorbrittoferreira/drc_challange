from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_create_api(api: FastAPI):
    """
    Tests if the create_api function returns an instance of FastAPI and includes the paint mall API router.
    """

    assert isinstance(api, FastAPI)
    version = "v1"
    api_base_route = f"/api/{version}"
    service = "/paint_mall"
    path_list = ["/paint_cans_needed"]

    assert f"{api_base_route}{service}{path_list[0]}" in [
        route.path for route in api.routes
    ]

    with TestClient(api) as client:
        response = client.post("/api/v1/paint_mall/paint_cans_needed")
        assert response.status_code == 422

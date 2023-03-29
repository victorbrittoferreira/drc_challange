def test_expected_sucess_response_paint_cans_calculator(
    api_client,
    valid_request_payload_walls_dimensions,
    json_response_successful,
):
    response = api_client.post(
        "/api/v1/paint_mall/paint_cans_needed",
        json=valid_request_payload_walls_dimensions,
    )

    assert response.status_code == 200
    assert response.json() == json_response_successful


def test_expected_unprocessable_entity_response_paint_cans_calculator(
    api_client,
    invalid_request_payload_walls_dimensions,
    json_response_expected_fail_to_process_dimensions,
):
    response = api_client.post(
        "/api/v1/paint_mall/paint_cans_needed",
        json=invalid_request_payload_walls_dimensions,
    )

    assert response.status_code == 422
    assert response.json() == json_response_expected_fail_to_process_dimensions


def test_expected_unprocessable_entity_response_paint_cans_calculator2(
    api_client,
    invalid_request_payload_walls_dimensions_2,
    json_response_expected_fail_to_process_dimensions2,
):
    response = api_client.post(
        "/api/v1/paint_mall/paint_cans_needed",
        json=invalid_request_payload_walls_dimensions_2,
    )

    assert response.status_code == 422
    assert (
        response.json() == json_response_expected_fail_to_process_dimensions2
    )


def test_expected_unprocessable_entity_response_paint_cans_calculator3(
    api_client,
    invalid_request_payload_walls_dimensions_3,
    json_response_expected_fail_to_process_dimensions3,
):
    response = api_client.post(
        "/api/v1/paint_mall/paint_cans_needed",
        json=invalid_request_payload_walls_dimensions_3,
    )

    assert response.status_code == 422
    assert (
        response.json() == json_response_expected_fail_to_process_dimensions3
    )

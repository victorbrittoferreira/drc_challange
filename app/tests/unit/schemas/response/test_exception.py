import pytest

from src.schemas.response.exception import UnprocessableGeometricObjectValue


def test_valid_unprocessed_geometric_object():
    """
    Test that an UnprocessableGeometricObjectValue exception is raised with
    the correct attributes when a dictionary of validation errors is passed
    to it.
    """
    errors_dict = {
        "wall_1": ["Missing height"],
        "wall_2": ["Missing dimensions"],
    }
    with pytest.raises(UnprocessableGeometricObjectValue) as error:
        raise UnprocessableGeometricObjectValue(walls=errors_dict)
    assert error.value.code == "geometric_inconsistencies_found"
    assert error.value.walls == errors_dict
    assert (
        error.value.msg_template
        == "Was/Were found inconsistent(cies) geometrics value(s) input."
    )

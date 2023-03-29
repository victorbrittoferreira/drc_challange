import pytest
from pydantic import ValidationError

from src.schemas.response.unprocessable_geometric_object import (
    UnprocessedGeometricObject,
)


def test_valid_unprocessed_geometric_object():
    """
    Test if the dict return is valid and raise a exception
    to be handle by fastapi
    """
    errors_dict = {
        "wall_1": ["Missing height"],
        "wall_2": ["Missing dimensions"],
    }
    with pytest.raises(ValidationError):
        UnprocessedGeometricObject(errors=errors_dict)

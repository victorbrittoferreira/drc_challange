from typing import Dict, List, NewType

from pydantic import BaseModel, validator

from .exception import UnprocessableGeometricObjectValue

Error = NewType("Error", List[str])
ErrorsDict = NewType("ErrorsDict", Dict[str, Error])


class UnprocessedGeometricObject(BaseModel):
    """
    A Pydantic model representing an unprocessed geometric object that has validation errors.

    Attributes:
    -----------
    errors : ErrorsDict
        A dictionary containing the validation errors for each component of the geometric object.

    Methods:
    --------
    validate_amount_paint_cans_needed(cls, errors)
        A validator function that raises an UnprocessableGeometricObjectValue error if the provided `errors`
        parameter is not a dictionary.
    """

    errors: ErrorsDict

    @validator("errors")
    def validate_amount_paint_cans_needed(cls, errors):
        if isinstance(errors, dict):
            raise UnprocessableGeometricObjectValue(walls=errors)

    class Config:
        extra = "forbid"
        frozen = True
        schema_extra = {
            "example": [
                {
                    "loc": ["errors"],
                    "msg": "Was/Were found inconsistent(cies) geometrics value(s) input.",
                    "type": "value_error.geometric_inconsistencies_found",
                    "ctx": {
                        "walls": {
                            "Wall_1": [
                                "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                                "Wall is 2.10m shorter than the door.",
                                "Wall is 5.50m narrower than the width of amount of window(s) + doors.",
                            ],
                            "Wall_2": [
                                "Wall is 2.10m shorter than the door.",
                                "Wall is 0.70m narrower than the width of amount of window(s) + doors.",
                            ],
                            "Wall_3": [
                                "The wall area, 0.01m2, is out of range between 1m2 and 50m2.",
                                "Wall is 1.90m narrower than the width of amount of window(s) + doors.",
                            ],
                            "Wall_4": [
                                "The wall area, 0.01m2, is out of range between 1m2 and 50m2."
                            ],
                        }
                    },
                }
            ]
        }

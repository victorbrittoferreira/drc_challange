from pydantic import PydanticValueError


class UnprocessableGeometricObjectValue(PydanticValueError):
    """Raises when Pydantic validation caught value unallowed or inconsistent."""

    code = "geometric_inconsistencies_found"
    msg_template = (
        "Was/Were found inconsistent(cies) geometrics value(s) input."
    )

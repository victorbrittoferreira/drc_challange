from pydantic import ValidationError
from pytest import approx, raises

from src.schemas.wall import Wall


# ------------------------ wall_area -----------------------------
def test_area():
    """
    Test to verify if the area calculation is correct
    """
    wall = Wall(width=5, height=2.5, number_doors=0, number_windows=0)
    assert wall.area == approx(12.5)


def test_negative_area_width():
    """
    Test to verify if an exception is raised when a negative width is passed
    """
    with raises(ValidationError):
        Wall(width=-5, height=1, number_doors=0, number_windows=0)


def test_negative_area_height():
    """
    Test to verify if an exception is raised when a negative height is passed
    """
    with raises(ValidationError):
        Wall(width=5, height=-1, number_doors=0, number_windows=0)


def test_no_width():
    """
    Test to verify if an exception is raised when the width is zero
    """
    with raises(ValidationError):
        Wall(width=0, height=1, number_doors=0, number_windows=0)


def test_no_height():
    """
    Test to verify if an exception is raised when the height is zero
    """
    with raises(ValidationError):
        Wall(width=1, height=0, number_doors=0, number_windows=0)


# ------------------------ windows_area -----------------------------


def test_windows_total_area():
    """
    Test to verify if the total windows area is correctly calculated
    """
    wall = Wall(width=5, height=2.5, number_doors=0, number_windows=2)
    assert wall.windows_area == approx(4.8)


def test_negative_windows():
    """
    Test to verify if an exception is raised when a negative number of windows is passed
    """
    with raises(ValidationError):
        Wall(width=5, height=2.5, number_doors=0, number_windows=-1)


def test_no_windows():
    """
    Test to verify if no exception is raised when zero windows are passed
    """
    wall = Wall(width=1, height=1, number_doors=0, number_windows=0)
    assert isinstance(wall, Wall)


# ------------------------ doors_area -----------------------------
def test_doors_total_area():
    """
    Test to verify if the total doors area is correctly calculated
    """
    wall = Wall(width=5, height=2.5, number_doors=2, number_windows=0)
    assert wall.doors_area == approx(3.04)


def test_negative_doors():
    """
    Test to verify if an exception is raised when a negative number of doors is passed
    """
    with raises(ValidationError):
        Wall(width=5, height=2.5, number_doors=-1, number_windows=0)


def test_no_doors():
    """
    Test to verify if no exception is raised when zero doors are passed
    """
    wall = Wall(width=1, height=1, number_doors=0, number_windows=0)
    assert isinstance(wall, Wall)

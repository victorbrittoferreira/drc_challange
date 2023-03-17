import copy

import pytest
from src.entities.wall import Wall


def test_valid_wall(correct_wall_size):
    wall_size = Wall(**correct_wall_size)

    assert (wall_size.length, wall_size.width) == (
        correct_wall_size["length"],
        correct_wall_size["width"],
    )


def test_invalid_size_gt_50m_wall(correct_wall_size):
    deepcopied_correct_wall_size = copy.deepcopy(correct_wall_size)
    deepcopied_correct_wall_size.update({"length": 50.1})
    with pytest.raises(ValueError):
        Wall(**deepcopied_correct_wall_size)


def test_invalid_size_lt_1m_wall(correct_wall_size):
    deepcopied_correct_wall_size = copy.deepcopy(correct_wall_size)
    deepcopied_correct_wall_size.update({"length": 0})
    with pytest.raises(ValueError):
        Wall(**deepcopied_correct_wall_size)

import pytest
from modules.day2 import position_product


def test_position_product():
    assert position_product(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150

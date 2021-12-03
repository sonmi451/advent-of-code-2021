import pytest
from day2 import crude_position_product, position_product


def test_crude_position_product():
    assert crude_position_product(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150

def test_position_product():
    assert position_product(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900

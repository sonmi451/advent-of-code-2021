import pytest
from modules.day1 import depth_measurement_increase, sum_depth_measurement_increase

# @pytest.mark.parametrize('input, result', testdata)
def test_depth_measurement_increase():
    assert depth_measurement_increase([199,200,208,210,200,207,240,269,260,263]) == 7

def test_sum_depth_measurement_increase():
    assert sum_depth_measurement_increase([199,200,208,210,200,207,240,269,260,263]) == 5

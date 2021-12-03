import pytest
from day3 import power_consumption, life_support_rating

def test_power_consumption():
    assert power_consumption(['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']) == 198

def test_life_support_rating():
    assert life_support_rating(['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']) == 230

from modules.day6 import exponential_fish


def test_one_fish_five_days():
    output = exponential_fish([3], 5)
    assert output == 2

def test_five_fish_eighteen_days():
    input = [3,4,3,1,2]
    output = exponential_fish(input, 18)
    assert output == 26


def test_five_fish_eighty_days():
    input = [3,4,3,1,2]
    output = exponential_fish(input, 80 )
    assert output == 5934

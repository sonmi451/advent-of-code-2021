from modules.day9 import find_low_points, calculate_risk


def test_find_low_points():
    input = [
        [int(x) for x in '2199943210'],
        [int(x) for x in '3987894921'],
        [int(x) for x in '9856789892'],
        [int(x) for x in '8767896789'],
        [int(x) for x in '9899965678']
    ]
    low_points = find_low_points(input)
    assert low_points == [1, 0, 5, 5]


def test_calculate_risk():
    risk = calculate_risk([1, 0, 5, 5])
    assert risk == 15

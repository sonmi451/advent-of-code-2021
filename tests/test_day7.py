from modules.day7 import align_crabs_linear, align_crabs, smallest_fuel_cost


def test_align_crabs_linear():
    input = [16,1,2,0,4,2,7,1,2,14]
    fuel_costs = align_crabs_linear(input, 16)
    fuel_cost = smallest_fuel_cost(fuel_costs)
    assert fuel_cost == 37

def test_align_crabs():
    input = [16,1,2,0,4,2,7,1,2,14]
    fuel_costs = align_crabs(input, 16)
    fuel_cost = smallest_fuel_cost(fuel_costs)
    assert fuel_cost == 168

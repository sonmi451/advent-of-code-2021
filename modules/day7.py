from math import factorial
from read_datafile import read_sequence

def get_crab_alignment():
    filepath = './data/day7.txt'
    crab_alignments = read_sequence(filepath)
    return crab_alignments


def furthest_crab(crabs):
    # find furthest away crab
    furthest_crab = 0
    for crab in crabs:
        if crab > furthest_crab:
            furthest_crab = crab
    return furthest_crab


def smallest_fuel_cost(fuel_costs):
    # Find smallest fuel cost
    smallest_cost = fuel_costs[0]
    for cost in fuel_costs:
        if cost < smallest_cost:
            smallest_cost = cost
            most_efficient_position = fuel_costs.index(cost)
    return fuel_costs[most_efficient_position]


def align_crabs_linear(crabs, furthest_crab):
    # find fuel costs of alignments
    fuel_costs = []
    for position in range(1, furthest_crab):
        movement = 0
        for crab in crabs:
            if crab > position:
                movement += (crab - position) % furthest_crab
            elif crab < position:
                movement += (position - crab) % furthest_crab
        fuel_costs.append(movement)
    return fuel_costs


def align_crabs(crabs, furthest_crab):
    # find fuel costs of alignments
    fuel_costs = []
    for position in range(1, furthest_crab):
        movement = 0
        all_crab_fuel = 0
        for crab in crabs:
            if crab > position:
                movement = (crab - position) % furthest_crab
            elif crab < position:
                movement = (position - crab) % furthest_crab

            one_crab_fuel = 0
            for step in range(1, movement+1):
                one_crab_fuel += step
            all_crab_fuel += one_crab_fuel

        fuel_costs.append(all_crab_fuel)
    return fuel_costs


crab_alignments = get_crab_alignment()
furthest_crab = furthest_crab(crab_alignments)
fuel_costs = align_crabs_linear(crab_alignments, furthest_crab)
# fuel_costs = align_crabs(crab_alignments, furthest_crab)
print(fuel_costs)
smallest_fuel_cost = smallest_fuel_cost(fuel_costs)
print(smallest_fuel_cost)

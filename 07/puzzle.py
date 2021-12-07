import math

def solve(data):

    fuel = []
    i = 0
    while i <= max(data):
        fuel.append(sum(calc_movement(crab_position, i) for crab_position in data))
        i += 1

    return min(fuel)

def calc_movement(crab_position, align_position):
    return abs(crab_position - align_position)

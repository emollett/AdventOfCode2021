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

def solve2(data):

    fuel = []
    i = 0
    while i <= max(data):
        fuel.append(sum(calc_movement2(crab_position, i) for crab_position in data))
        i += 1

    return min(fuel)

def calc_movement2(crab_position, align_position):
    return (1 + abs(crab_position - align_position)) * (abs(crab_position - align_position)/2)


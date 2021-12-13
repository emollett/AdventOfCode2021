from typing import Counter


def parse(data):
    input = []
    for line in data:
        coordinates = line.split(" -> ")
        x1 = int(coordinates[0].split(",")[0])
        y1 = int(coordinates[0].split(",")[1])
        x2 = int(coordinates[1].split(",")[0])
        y2 = int(coordinates[1].split(",")[1])
        input.append(((x1, y1), (x2, y2)))
    return input

def removeDiagonal(listOfVents):
    squareVents = []
    for vents in listOfVents:
        coord1, coord2 = vents
        if coord1[0]  == coord2[0] or coord1[1]  == coord2[1]:
            squareVents.append(vents)
    return squareVents

def expandCoordinates(listOfVents):
    expandedVents = []
    for vents in listOfVents:
        x1 = vents[0][0]
        y1 = vents[0][1]
        x2 = vents[1][0]
        y2 = vents[1][1]
        if x1 == x2:
            # tidy this up
            for i in range(y1, y2 + 1): expandedVents.append((x1, i))
            for i in range(y1, y2 - 1, -1): expandedVents.append((x1, i))
        elif y1 == y2:
            for i in range(x1, x2 + 1): expandedVents.append((i, y1))
            for i in range(x1, x2 - 1, -1): expandedVents.append((i, y1))
        elif y1 < y2 and x1 < x2:
            for i in range(y2 - y1 + 1): expandedVents.append((x1 + i, y1 + i))
        elif y1 < y2 and x1 > x2:
            for i in range(y2 - y1 + 1): expandedVents.append((x1 - i, y1 + i))
        elif y1 > y2 and x1 < x2:
            for i in range(y1 - y2 + 1): expandedVents.append((x1 + i, y1 - i))
        elif y1 > y2 and x1 > x2:
            for i in range(y1 - y2 + 1): expandedVents.append((x1 - i, y1 - i))
    return expandedVents

def solve(data):
    parsed_data = parse(data)
    removed_diagonals = removeDiagonal(parsed_data)
    lines = expandCoordinates(removed_diagonals)
    count = len([x for x in Counter(lines).values() if x>1])
    return count

def solve2(data):
    parsed_data = parse(data)
    lines = expandCoordinates(parsed_data)
    count = len([x for x in Counter(lines).values() if x>1])
    return count
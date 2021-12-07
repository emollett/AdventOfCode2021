def parse(data):
    input = []
    for line in data:
        coordinates = line.split(" -> ")
        x1 = int(coordinates[0].split(",")[0])
        y1 = int(coordinates[0].split(",")[1])
        x2 = int(coordinates[1].split(",")[0])
        y2 = int(coordinates[1].split(",")[1])
        input.append(([x1, y1], [x2, y2]))
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
            for i in range(y1, y2 + 1):
                expandedVents.append([x1, i])
            for i in range(y1, y2 - 1, -1):
                expandedVents.append([x1, i])
        else:
            for i in range(x1, x2 + 1):
                expandedVents.append([i, y1])
            for i in range(x1, x2 - 1, -1):
                expandedVents.append([i, y1])
    return expandedVents
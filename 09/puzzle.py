def findLows(heightmap):
    lows = []
    for y, line in enumerate(heightmap):
        for x, point in enumerate(line):
            # For points not at any edge
            if x != 0 and x != len(line) -1 and y != 0 and y != len(heightmap)-1:
                if point < line[x -1] and point < line[x +1] and point < heightmap[y-1][x] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # for things on the left hand side and not on the top or bottom edge
            elif x != len(line) -1 and y != 0 and y != len(heightmap)-1:
                if point < line[x +1] and point < heightmap[y-1][x] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # for things on the right hand side and not on the top or bottom edge
            elif x != 0 and y != 0 and y != len(heightmap)-1:
                if point < line[x -1] and point < heightmap[y-1][x] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # For points at the top but not on either side
            elif x != 0 and x != len(line) -1 and y != len(heightmap)-1:
                if point < line[x -1] and point < line[x +1] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # For points at the bottom but not at either side
            elif x != 0 and x != len(line) -1 and y != 0:
                if point < line[x -1] and point < line[x +1] and point < heightmap[y-1][x]:
                    lows.append([(x, y), point])

            # For point at top left corner
            elif x != len(line) -1 and y != len(heightmap)-1:
                if point < line[x +1] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # For point at top right corner
            elif x != 0 and y != len(heightmap)-1:
                if point < line[x -1] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

            # For point at bottom left corner
            elif x != len(line) -1 and y != 0 and y != len(heightmap)-1:
                if point < line[x +1] and point < heightmap[y-1][x]:
                    lows.append([(x, y), point])

            # For point at bottom right
            elif x != 0 and y != 0:
                if point < line[x -1] and point < heightmap[y-1][x]:
                    lows.append([(x, y), point])

    print(lows)
    return lows

def calculateRisk(lows):
    risk = 0
    for point in lows:
        risk += (int(point[1])+1)

    return risk
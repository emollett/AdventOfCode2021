def findLows(heightmap):
    lows = []
    for y, line in enumerate(heightmap):
        for x, point in enumerate(line):
            # For points not at any edge
            if x != 0 and x != len(line) -1 and y != 0 and y != len(heightmap)-1:
                if point < line[x -1] and point < line[x +1] and point < heightmap[y-1][x] and point < heightmap[y+1][x]:
                    lows.append([(x, y), point])

    return lows
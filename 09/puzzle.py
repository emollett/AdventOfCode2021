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

    return lows

def calculateRisk(lows):
    risk = 0
    for point in lows:
        risk += (int(point[1])+1)

    return risk

def findBasin(coordinate, heightmap):
    points_in_basin = []
    points_to_check = [coordinate]

    while len(points_to_check) > 0:
        x, y = points_to_check[0]

        # check to left
        if x != 0 and heightmap[y][x] < heightmap[y][x-1] and heightmap[y][x-1] != '9':
            points_to_check.append((x-1, y))

        # check to right
        if x != len(heightmap[y])-1 and heightmap[y][x] < heightmap[y][x+1] and heightmap[y][x+1] != '9':
            points_to_check.append((x+1, y))

        # check up
        if y != 0 and heightmap[y][x] < heightmap[y-1][x] and heightmap[y-1][x] != '9':
            points_to_check.append((x, y-1))

        # check down
        if y != len(heightmap)-1 and heightmap[y][x] < heightmap[y+1][x] and heightmap[y+1][x] != '9':
            points_to_check.append((x, y+1))

        points_in_basin.append((x, y))
        points_to_check.remove((x, y))

    return list(dict.fromkeys(points_in_basin))
        
def solve2(heightmap):
    lowPoints = findLows(heightmap)
    basin_sizes = []
    for coordinate in lowPoints:
        basin_sizes.append(len(findBasin(coordinate[0], heightmap)))
    biggest_basins = sorted(basin_sizes, reverse=True)
    return biggest_basins[0]*biggest_basins[1]*biggest_basins[2]


def parse(grid):
    parsed_data = []
    for y, line in enumerate(grid):
        for x, octopus in enumerate(line):
            parsed_data.append([(x, y), int(octopus)])
    return parsed_data

def oneStep(grid):
    right_bound = max(grid, key = lambda x: x[0][0])[0][0]
    bottom_bound = max(grid, key = lambda y: y[0][1])[0][1]
    flashed_octopuses = []

    # first we increase them all by 1
    for octopus in grid: octopus[1] +=1

    # then we look for any that are greater than 9 to start flashing, and keep doing this until no more are going to flash
    while any(octopus for octopus in grid if octopus[1] > 9):
        for index, octopus in enumerate(grid):
            if octopus[1] > 9:
                # reset this octopus to 0
                octopus[1] = 0

                # then increase all the neighbouring octopuses by 1
                x = octopus[0][0]
                y = octopus[0][1]
                neighbours = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
                in_bound_neighbours = [neighbour for neighbour in neighbours if neighbour[0] >= 0 and neighbour[0] <= right_bound and neighbour[1] >=0 and neighbour[1] <= bottom_bound]
                for octo in grid:
                    if octo[0] in in_bound_neighbours and octo[1] <= 9:
                        octo[1] += 1

                # then remove the flashed octopus from the grid for this step
                flashed_octopuses.append(grid.pop(index))
    synced = len(grid) == 0
    grid.extend(flashed_octopuses)
    return grid, synced

def countFlashes(grid, steps):
    flashes = 0
    for i in range(steps):
        oneStep(grid)
        flashes += len([octopus for octopus in grid if octopus[1] == 0])
    return flashes

def findSynchronisation(grid):
    synced = False
    i = 0
    while not synced:
        synced = oneStep(grid)[1]
        i += 1
    return i
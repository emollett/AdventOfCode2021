from operator import itemgetter

def parse(data):
    dots = []
    folds = []
    for line in data:
        if line == "":
            continue
        elif line.split()[0] == "fold":
            fold = line.split()[2].split("=")
            folds.append((fold[0], int(fold[1])))
        else:    
            coordinates = line.split(",")
            dots. append((int(coordinates[0]), int(coordinates[1])))
    return dots, folds

def oneFold(coordinates, fold):
    direction, size = fold

    if direction == 'y':
        new_coordinates = [(coordinate[0], size - (coordinate[1] - size)) for coordinate in coordinates if coordinate[1] > size]
        unchanged_coordinates = [coordinate for coordinate in coordinates if not coordinate[1] > size]
    if direction == 'x':
        new_coordinates = [(size - (coordinate[0] - size), coordinate[1]) for coordinate in coordinates if coordinate[0] > size]
        unchanged_coordinates = [coordinate for coordinate in coordinates if not coordinate[0] > size]

    new_coordinates.extend(unchanged_coordinates)
    folded_coordinates = list(dict.fromkeys(new_coordinates))

    return folded_coordinates

def severalFolds(data):
    dots, folds = parse(data)
    for fold in folds:
        dots = oneFold(dots, fold)
    return dots

def passwordPicture(data):
    dots = severalFolds(data)
    largest_x = max(dots, key=itemgetter(0))[0]
    largest_y = max(dots, key=itemgetter(1))[0]
    grid = []
    for i in range(largest_y + 1):
        grid.append(["  "] * (largest_x + 1))

    for dot in dots:
        grid[dot[1]][dot[0]] = '#'

    for line in grid:
        print(line)
    return -1

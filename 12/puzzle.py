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
    new_coordinates = []
    unchanged_coordinates = []
    if direction == 'y':
        for coordinate in coordinates:
            if coordinate[1] > size:
                new_coordinate = (coordinate[0], size - (coordinate[1] - size))
                new_coordinates.append(new_coordinate)
            else:
                unchanged_coordinates.append(coordinate)
    if direction == 'x':
        for coordinate in coordinates:
            if coordinate[0] > size:
                new_coordinate = (size - (coordinate[0] - size), coordinate[1])
                new_coordinates.append(new_coordinate)
            else:
                unchanged_coordinates.append(coordinate)
    new_coordinates.extend(unchanged_coordinates)
    folded_coordinates = list(dict.fromkeys(new_coordinates))
    return folded_coordinates

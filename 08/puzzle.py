def parse(data):
    notes = []
    for entry in data:
        unique_signal_pattern = entry.split(" | ")[0]
        output_value = entry.split(" | ")[1]
        parsed_entry = (unique_signal_pattern.split(" "), output_value.split(" "))
        notes.append(parsed_entry)
    return notes

def countUnique(data):
    uniqueCounter = 0
    for digit in data:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            uniqueCounter += 1
    return uniqueCounter

def solve1(notes):
    unique = 0
    for entry in notes:
        unique += countUnique(entry[1])
    return unique

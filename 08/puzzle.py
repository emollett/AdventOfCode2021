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

def identifyDigits(entry):
    input = entry[0]
    output = entry[1]
    
    one = any(len(digit) == 2 for digit in input)
    four = any(len(digit) == 3 for digit in input)
    seven = any(len(digit) == 4 for digit in input)
    eight = any(len(digit) == 7 for digit in input)

    for digit in input:
        if len(digit) == 4:
            if digit.split()

    # 3 has both the letters 1 does and length 4
    # 2 has 1 letter different from 3, which gives us e and f
    # 5 has 1 letter different from 3, which gives us b and c, shares all but 1 with 4

    #

    # a is the difference between 1 and 7 freq 8
    # b is the difference between 9 and 3 freq 6
    # c is the difference between 5 and 9 freq 8
    # d is the difference between 0 and 8 freq 7
    # e is the difference between 5 and 6 freq 4
    # f is the difference between ??????? freq 9
    # g is the difference between ??????? freq 7


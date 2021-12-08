def parse(raw_notes):
    notes = []
    for entry in raw_notes:
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
    
    one = [digit for digit in input if len(digit) == 2][0]
    four = [digit for digit in input if len(digit) == 4] [0]
    seven = [digit for digit in input if len(digit) == 3][0]
    eight = [digit for digit in input if len(digit) == 7][0]

    three = [digit for digit in input if len(digit) == 5 and one[0] in digit and one[1] in digit][0]

    six = [digit for digit in input if len(digit) == 6 and not (one[0]in digit and one[1] in digit)][0]
    nine = [digit for digit in input if len(digit) == 6 and all([letter in digit for letter in four])][0]
    zero = [digit for digit in input if len(digit) == 6 and digit != six and digit != nine][0]

    five = [digit for digit in input if len(digit) == 5 and all([letter in six for letter in digit])][0]
    two = [digit for digit in input if len(digit) == 5 and digit != three and digit != five][0]

    number_map = [zero, one, two, three, four, five, six, seven, eight, nine]

    return number_map

def decodeOutput(entry, numberMap):
    output = entry[1]

    decoded_output = ''

    for digit in output:
        matching_number = [number for number in numberMap if len(digit) == len (number) and all([letters in number for letters in digit])]
        indexOfNumber = numberMap.index(matching_number[0])
        decoded_output += str(indexOfNumber)

    return int(decoded_output)

def solve2(data):
    outputValues = 0
    for entry in data:
        number_map = identifyDigits(entry)
        decodedOutput = decodeOutput(entry, number_map)
        outputValues += decodedOutput
    return outputValues
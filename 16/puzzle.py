def parse(data):
    str = ""
    for character in data:
        str += "{0:04b}".format(int(character, 16))
    return str

def decodeHeader(data):
    return int(data[0:3], 2), int(data[3:6], 2), data[6:]

def decodeLiteral(data):
    end = False
    index = 0
    number = ""
    while not end:
        group = data[index:index+5]
        if int(group[0]) == 0: end = True
        number += group[1:5]
        index += 5
    print(data[index:])
    return int(number, 2), data[index:]

def decodeLengthID(data):
    if data[0] == '0': 
        lengthID = 'length'
        value = int(data[1:16], 2)
    else:
        lengthID = 'number'
        value = int(data[1:12], 2)

    return lengthID, value

def decodeOperator(versions, binary):
    # If it is a length operator, chop off the lengthID, and the 15 bits, then take a substring of length n, and look at that till it runs out

    # If it is a number operator, chop off the lengthID, and the 11 bits, then look through the remaining string for the next n sub packets.

    return versions, binary

def solve(data):
    binary = parse(data)
    versions = []
    while len(binary) > 0:
        version, id, binary = decodeHeader(binary)
        versions.append(version)
        if id == 4:
            number, binary = decodeLiteral(binary)
        else:
            versions, binary = decodeOperator(versions, binary)
    print(versions)
    return sum(versions)


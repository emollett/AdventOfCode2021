from operator import itemgetter
from typing import Counter

def parse(data):
    template = data[0]
    insertions = {}
    for line in data[2:]:
        insertion = line.split(" -> ")
        insertions[insertion[0]] = insertion[1]
    return template, insertions

def oneInsertion(template, insertionMap):
    pairs = [letter + template[i+1] for i, letter in enumerate(template[:-1])]
    insertions = [insertionMap[pair] for pair in pairs]
    inserted = "".join(i + j for i, j in zip(template, insertions)) + template[-1]
    return inserted

def multipleInsertions(data, rounds):
    template, insertionMap = data
    for _ in range(rounds):
        template = oneInsertion(template, insertionMap)
    return template

def solve(data, rounds):
    template = multipleInsertions(data, rounds)
    print(Counter(template).most_common(1)[0])
    print(Counter(template).most_common()[-1])
    score = Counter(template).most_common(1)[0][1] - Counter(template).most_common()[-1][1]
    return score

from collections import Counter
import string

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
    score = Counter(template).most_common(1)[0][1] - Counter(template).most_common()[-1][1]
    return score

def onePair(pair, insertionMap):
    insertion = insertionMap[pair]
    new_pairs = [pair[0]+insertion, insertion+pair[1]]
    return new_pairs

def createInitialFrequencies(insertionMap):
    pair_frequencies = {}
    for pair in insertionMap:
            pair_frequencies[pair] = 0
    return pair_frequencies

def updatePairFrequencies(pairs, pairFrequencies):
    pairFrequencies = pairFrequencies.fromkeys(pairFrequencies, 0)
    for pair in pairs:
        newPair, multiplier = pair
        pairFrequencies[newPair] += multiplier
    return pairFrequencies

def createNewPairs(pairFrequencies, insertionMap):
    pairsToUpdate = []
    for pair, frequency in pairFrequencies.items():
        if frequency > 0:
            insertion = insertionMap[pair]
            newPair1 = (pair[0]+insertion, frequency) 
            newPair2 = (insertion+pair[1], frequency)
            pairsToUpdate.extend([newPair1, newPair2])
    pairFrequencies = updatePairFrequencies(pairsToUpdate, pairFrequencies)
    return pairFrequencies

def solve2(data, rounds):
    template, insertionMap = data
    pairFrequencies = createInitialFrequencies(insertionMap)
    initial_pairs = [(letter + template[i+1], 1) for i, letter in enumerate(template[:-1])]
    pairFrequencies = updatePairFrequencies(initial_pairs, pairFrequencies)
    for _ in range(rounds):
        pairFrequencies = createNewPairs(pairFrequencies, insertionMap)
    score = scorePairs(pairFrequencies, template)
    return score

def scorePairs(pairFrequencies, template):
    elementFrequencies = dict.fromkeys(string.ascii_uppercase, 0)
    for pair, frequency in pairFrequencies.items():
        pair1 = pair[0]
        pair2 = pair[1]
        elementFrequencies[pair1] += frequency
        elementFrequencies[pair2] += frequency
    elementFrequencies[template[0]] += 1
    elementFrequencies[template[-1]] += 1
    elementFrequencies = {k: abs(v/2) for k, v in elementFrequencies.items()}
    score = max(elementFrequencies.values()) - min(filter(None, elementFrequencies.values()))
    return score


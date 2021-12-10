from typing import Counter

def processBrackets(line):
    opening_brackets = []
    for bracket in line:
        lookup = {")":"(", "]":"[", "}":"{", ">":"<"}
        if bracket in "([{<":
            opening_brackets.append(bracket)
        elif bracket in ")]}>" and opening_brackets[-1] == lookup[bracket]:
            opening_brackets.pop()
        else: return bracket
    return opening_brackets

def calculateAutocompleteScore(brackets):
    score = 0
    for bracket in reversed(brackets):
        lookup = {"(":1, "[":2, "{":3, "<":4}
        score = score * 5
        score += lookup[bracket]
    return score

def solve1(data):
    brackets = []
    for line in data:
        brackets.append(processBrackets(line))
    brackets = [x for x in brackets if not isinstance(x, list)]
    bracket_count = Counter(brackets)
    return bracket_count[')']*3 + bracket_count[']']*57 + bracket_count['}']*1197 + bracket_count['>']*25137

def solve2(data):
    scores = []
    for line in data:
        brackets = processBrackets(line)
        if isinstance(brackets, list):
            score = calculateAutocompleteScore(brackets)
            scores.append(score)
    scores.sort()
    middle_score = scores[len(scores)//2]
    return middle_score
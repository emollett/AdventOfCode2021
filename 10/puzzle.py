from typing import Counter

def findCorruptingBracket(line):
    opening_brackets = []
    for index, bracket in enumerate(line):
        if bracket == '[' or bracket == '{' or bracket == '(' or bracket == '<':
            opening_brackets.append(bracket)
        elif bracket == ']' and opening_brackets[-1] == '[':
            opening_brackets.pop()
        elif bracket == '}' and opening_brackets[-1] == '{':
            opening_brackets.pop()
        elif bracket == ')' and opening_brackets[-1] == '(':
            opening_brackets.pop()
        elif bracket == '>' and opening_brackets[-1] == '<':
            opening_brackets.pop()
        else: return bracket
    return 1

def solve1(data):
    brackets = []
    for line in data:
        brackets.append(findCorruptingBracket(line))
    bracket_count = Counter(brackets)

#     ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
    return bracket_count[')']*3 + bracket_count[']']*57 + bracket_count['}']*1197 + bracket_count['>']*25137

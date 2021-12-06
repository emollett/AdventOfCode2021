from collections import Counter

def solve(data, totalDays): 
    fish_per_offset = Counter(sorted(data))

    days = []
    i = 0
    while i < 9:
        days.append(fish_per_offset[i])
        i += 1

    while totalDays > 0:
        fish_to_add = days.pop(0)
        days.append(fish_to_add)
        days[6] += fish_to_add
        totalDays -= 1

    totalFish = sum(days)

    return totalFish

def parse(lines):  
    data = []  
    for line in lines:  
        data.append(int(line))  
    return data

def solve(data):  
    increased = 0
    previous_number = data[0]
    for number in data[1:len(data)]:
        if number > previous_number -1:
            increased = increased+1
        previous_number = number
    return increased

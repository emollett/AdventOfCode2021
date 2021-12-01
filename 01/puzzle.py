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

def solve2(data):  
    increased = 0
    previous_window = data[0] + data[1] + data[2]
    for index, number in enumerate(data[2:len(data)-2]):
        current_window = data[index+2] + data[index+3] + data[index+4]
        if current_window > previous_window:
            increased = increased+1
        previous_window = current_window
    return increased

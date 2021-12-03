Def Parse(lines)

Data = []  

For line in lines
   Data.append(line.split()) 

list(zip(*original[::-1]))
(Try without -1 bit)

Return data

Def solve(data)

Gamma = “”
Epsilon = “”

For datum in data
   Frequency = sum(datum)
   If frequency > len(datum)/2
      Gamma = gamma + “1”
      Epsilon = epsilon + 0
   Else 
      Gamma = gamma + 0
      Epsilon = epsilon + 1
   (May need reversing)

Return int(gamma,2) * int(epsilon,2)

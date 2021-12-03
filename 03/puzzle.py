from collections import Counter

def parse(lines):
   input = [] 
   for line in lines:
      input.append(list(line.strip()))
   
   rotated_input = list(zip(*input))

   data = []
   for line in rotated_input:
      data.append("".join(line))

   return data

def solve(data):

   gamma = ''
   epsilon = ''

   for line in data:
      res = Counter(line)
      if res["1"] > len(line)/2:
         gamma = gamma + '1'
         epsilon = epsilon + '0'
      else:
         gamma = gamma + '0'
         epsilon = epsilon + '1'

   return int(gamma,2) * int(epsilon,2)

from collections import Counter
from typing import ItemsView

def basicParse(input):
   output = [] 
   for line in input:
      output.append(list(line.strip()))
   return output

def rotateInput(input):
   rotated_input = list(zip(*input))
   data = []
   for line in rotated_input:
      data.append("".join(line))

   return data

def solve(data):
   rotatedData = rotateInput(data)
   gamma = ''
   epsilon = ''

   for line in rotatedData:
      res = Counter(line)
      if res["1"] > len(line)/2:
         gamma = gamma + '1'
         epsilon = epsilon + '0'
      else:
         gamma = gamma + '0'
         epsilon = epsilon + '1'

   return int(gamma,2) * int(epsilon,2)

def calculateOxygenRating(input):
   originalInput = basicParse(input)
   rotatedInput = rotateInput(originalInput)

   indexOfBit = 0

   while len(originalInput) > 1:
      res = Counter(rotatedInput[indexOfBit])
      if res["1"] >= len(originalInput)/2:
         originalInput = [i for i in originalInput if i[indexOfBit] == '1']
         rotatedInput = rotateInput(originalInput)
      else:
         originalInput = [i for i in originalInput if i[indexOfBit] == '0']
         rotatedInput = rotateInput(originalInput)
      indexOfBit += 1

   return int("".join(originalInput[0]),2)

def calculateCO2Rating(input):
   originalInput = basicParse(input)
   rotatedInput = rotateInput(originalInput)

   indexOfBit = 0

   while len(originalInput) > 1:
      res = Counter(rotatedInput[indexOfBit])
      if res["1"] >= len(originalInput)/2:
         originalInput = [i for i in originalInput if i[indexOfBit] == '0']
         rotatedInput = rotateInput(originalInput)
      else:
         originalInput = [i for i in originalInput if i[indexOfBit] == '1']
         rotatedInput = rotateInput(originalInput)
      indexOfBit += 1

   return int("".join(originalInput[0]),2)

def solve2(data):
   return calculateCO2Rating(data) * calculateOxygenRating(data)

from collections import Counter
from typing import ItemsView

def rotateInput(input):
   rotated_input = list(zip(*input))
   print(rotated_input)
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

def calculateOxygenRating(rotatedData, originalData):
   indexOfBit = 0

   while len(originalData) > 1:
      res = Counter(rotatedData[indexOfBit])
      if res["1"] >= res["0"]:
         originalData = [i for i in originalData if i[indexOfBit] == '1']
         rotatedData = rotateInput(originalData)
      else:
         originalData = [i for i in originalData if i[indexOfBit] == '0']
         rotatedData = rotateInput(originalData)
      indexOfBit += 1

   return int("".join(originalData[0]),2)

def calculateCO2Rating(rotatedData, originalData):
   indexOfBit = 0

   while len(originalData) > 1:
      res = Counter(rotatedData[indexOfBit])
      if res["0"] <= res["1"]:
         originalData = [i for i in originalData if i[indexOfBit] == '0']
         rotatedData = rotateInput(originalData)
      else:
         originalData = [i for i in originalData if i[indexOfBit] == '1']
         rotatedData = rotateInput(originalData)
      indexOfBit += 1

   return int("".join(originalData[0]),2)

def solve2(data):
   rotatedData = rotateInput(data)
   originalData = rotateInput(rotatedData)
   return calculateCO2Rating(rotatedData, originalData) * calculateOxygenRating(rotatedData, originalData)

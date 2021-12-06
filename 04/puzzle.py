from collections import Counter
from os import linesep
from typing import ItemsView

def parseDrawnNumbers(input):
   data = list(map(int, input[0].split(",")))
   return data

def parseBoards(input):
   del input[0]
   data = []
   board = []
   for line in input:
      if not line.isspace():
         stripped_line = line.strip()
         board.append(list(map(int, stripped_line.split())))
         print(board)
      else:
         data.append(board)
         board.clear()
   data.append(board)
   return data

def rotateInput(input):
   rotated_input = list(zip(*input))
   data = []
   for line in rotated_input:
      data.append("".join(line))
   return data
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
      if line != "":
         board.append(list((map(int, line.split()))))
      else:
         rotated_board = rotateInput(board[:])
         board.extend(rotated_board)
         if len(board)>0: data.append(board[:])
         board.clear()
   data.append(board[:])
   print(data)
   return data

def rotateInput(input):
   rotated_input = list(zip(*input))
   data = []
   for line in rotated_input:
      data.append("".join(line))
   return data
def parse(lines):
   instructions = []

   for line in lines:
      instructions.append([line.split()[0], int(line.split()[1])]) 

   return instructions

def solve(instructions):
   horizontal = 0
   vertical = 0

   for instruction in instructions:
      if instruction[0] == 'forward':
        horizontal += instruction[1]
      if instruction[0] == 'up':
         vertical -= instruction[1]
      if instruction[0] == 'down':
         vertical += instruction[1]

   return horizontal * vertical

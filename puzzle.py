def parse(lines)

   Class instruction:
      def __init__(self, direction, value):  
         self.direction = directions
         self.value = value

   instructions = []  

   for line in lines
      instructions.append(instruction(line.split()[0], int(line.split()[0])) ) 

   return instructions

def solve(instructions)
   horizontal = 0
   vertical = 0

   for instruction in instructions:
      if instruction.direction == 'right'
        horizontal += instruction.value
      if instruction.direction == 'left'
         horizontal -= instruction.value
      if instruction.direction == 'up'
         vertical += instruction.value
      if instruction.direction == 'down'
         vertical -= instruction.value

   return horizontal * vertical

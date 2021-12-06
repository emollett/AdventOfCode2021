import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_rotation(self):
        input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        data = puzzle.rotateInput(input)
        self.assertEqual(['011110011100', '010001010101', '111111110000', '011101100011', '000111100100'], data)

    def test_basic_solve(self):
        data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        self.assertEqual(198, puzzle.solve(data))

    def test_puzzle_answer_part1(self): 
        input = open("03/input.txt", "r")
        answer = puzzle.solve(input)  
        input.close()
        self.assertEqual(4138664, answer)

    def test_solve2_oxygen(self):
        rotatedInput = ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
        originalInput = puzzle.rotateInput(rotatedInput)
        self.assertEqual(23, puzzle.calculateOxygenRating(rotatedInput, originalInput))

    def test_solve2_co2(self):
        rotatedInput = ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
        originalInput = puzzle.rotateInput(rotatedInput)
        self.assertEqual(10, puzzle.calculateCO2Rating(rotatedInput, originalInput))

    def test_solve2_full(self):
        input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        self.assertEqual(230, puzzle.solve2(input))

    def test_puzzle_answer_part2(self): 
        input = open("03/input.txt", "r")
        answer = puzzle.solve2(input)  
        input.close()
        self.assertEqual(4273224, answer)

if __name__ == '__main__':  
    unittest.main()
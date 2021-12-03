import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.basicParse('''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines())
        self.assertEqual([['0', '0', '1', '0', '0'], ['1', '1', '1', '1', '0'], ['1', '0', '1', '1', '0'], ['1', '0', '1', '1', '1'], ['1', '0', '1', '0', '1'], ['0', '1', '1', '1', '1'], ['0', '0', '1', '1', '1'], ['1', '1', '1', '0', '0'], ['1', '0', '0', '0', '0'], ['1', '1', '0', '0', '1'], ['0', '0', '0', '1', '0'], ['0', '1', '0', '1', '0']], data)  

    def test_rotation(self):
        input = puzzle.basicParse('''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines())
        data = puzzle.rotateInput(input)
        self.assertEqual(['011110011100', '010001010101', '111111110000', '011101100011', '000111100100'], data)

    def test_basic_solve(self):
        data = puzzle.basicParse('''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines())
        self.assertEqual(198, puzzle.solve(data))

    def test_puzzle_answer_part1(self): 
        input = open("03/input.txt", "r")
        answer = puzzle.solve(input)  
        input.close()
        self.assertEqual(4138664, answer)

    def test_solve2_oxygen(self):
        input = '''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines()
        self.assertEqual(23, puzzle.calculateOxygenRating(input))

    def test_solve2_co2(self):
        input = '''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines()
        self.assertEqual(10, puzzle.calculateCO2Rating(input))

    def test_solve2_full(self):
        input = '''00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010'''.splitlines()
        self.assertEqual(230, puzzle.solve2(input))

    # def test_puzzle_answer_part1(self): 
    #     input = open("03/input.txt", "r")
    #     answer = puzzle.solve2(input)  
    #     input.close()
    #     self.assertEqual(0, answer)

if __name__ == '__main__':  
    unittest.main()
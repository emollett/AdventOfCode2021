import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.parse('''00100
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
        self.assertEqual(['011110011100', '010001010101', '111111110000', '011101100011', '000111100100'], data)

    def test_basic_solve(self):
        data = ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
        self.assertEqual(198, puzzle.solve(data))

    def test_puzzle_answer_part1(self): 
        input = open("03/input.txt", "r")
        data = puzzle.parse(input.readlines()) 
        answer = puzzle.solve(data)  
        input.close()
        self.assertEqual(4138664, answer)

if __name__ == '__main__':  
    unittest.main()
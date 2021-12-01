import unittest  
import puzzle

class TestBasic(unittest.TestCase):  
    def test_basic_solve(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(7, puzzle.solve(data))

    def test_basic_parse(self):
        data = puzzle.parse('''1  
        3  
        2'''.split())  
        self.assertEqual([1, 3, 2], data)

    def test_puzzle_answer_part1(self): 
        input = open("01\input.txt", "r")
        data = puzzle.parse(input.readlines()) 
        answer = puzzle.solve(data)  
        input.close()
        self.assertEqual(1228, answer)

if __name__ == '__main__':  
    unittest.main()
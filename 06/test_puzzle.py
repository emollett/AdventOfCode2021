import unittest  
import puzzle

class TestBasic(unittest.TestCase):  
    def test_basic_solve(self):
        data = [3,4,3,1,2]
        self.assertEqual(26, puzzle.solve(data, 18))
        self.assertEqual(5934, puzzle.solve(data, 80))

    def test_puzzle_answer_part1(self): 
        input = open("06/input.txt", "r")
        data = list(map(int, input.readline().split(",")))
        answer = puzzle.solve(data, 80)  
        input.close()
        self.assertEqual(360268, answer)

    def test_puzzle_answer_part1(self): 
        input = open("06/input.txt", "r")
        data = list(map(int, input.readline().split(",")))
        answer = puzzle.solve(data, 256)  
        input.close()
        self.assertEqual(1632146183902, answer)

if __name__ == '__main__':  
    unittest.main()
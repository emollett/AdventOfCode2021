import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_solve(self):
        data = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(37, puzzle.solve(data))

    def test_puzzle_answer_part1(self): 
        input = open("07/input.txt", "r")
        data = list(map(int, input.readline().split(",")))
        answer = puzzle.solve(data)  
        input.close()
        self.assertEqual(342534, answer)   

if __name__ == '__main__':  
    unittest.main()
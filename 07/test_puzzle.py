import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_solve(self):
        data = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(37, puzzle.solve(data, '1'))

    def test_puzzle_answer_part1(self): 
        input = open("07/input.txt", "r")
        data = list(map(int, input.readline().split(",")))
        answer = puzzle.solve(data, '1')  
        input.close()
        self.assertEqual(342534, answer) 

    def test_calc_crab_movement_2(self):
        self.assertEqual(10, puzzle.calc_movement2(1, 5))

    def test_basic_solve2(self):
        data = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(168, puzzle.solve(data, '2'))

    def test_puzzle_answer_part2(self): 
        input = open("07/input.txt", "r")
        data = list(map(int, input.readline().split(",")))
        answer = puzzle.solve(data, '2')  
        input.close()
        self.assertEqual(94004208, answer)   

if __name__ == '__main__':  
    unittest.main()
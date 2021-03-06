import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_find_horizontal_low_points(self):
        data = puzzle.findLows('''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines())
        self.assertEqual([[(1, 0), '1'], [(9, 0), '0'], [(2, 2), '5'], [(6, 4), '5']] ,data)

    def test_calculate_risk_level(self):
        data = [[(1, 0), '1'], [(9, 0), '0'], [(2, 2), '5'], [(6, 4), '5']]
        self.assertEqual(15, puzzle.calculateRisk(data))

    def test_puzzle_answer_part1(self): 
        input = open("09/input.txt", "r")
        data = input.read().splitlines()
        lows = puzzle.findLows(data)
        answer = puzzle.calculateRisk(lows)  
        input.close()
        self.assertEqual(516, answer) 

    def test_find_basin(self):
        data = puzzle.findBasin((2, 2) , '''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines())
        self.assertEqual(14 ,len(data))

    def test_basic_solve_2(self):
        data = puzzle.solve2('''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines())
        self.assertEqual(1134 ,data)   

    def test_puzzle_answer_part2(self): 
        input = open("09/input.txt", "r")
        data = input.read().splitlines()
        answer = puzzle.solve2(data)  
        input.close()
        self.assertEqual(1023660, answer)      

if __name__ == '__main__':  
    unittest.main()
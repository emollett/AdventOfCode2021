import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.parse('''forward 5
        down 5
        forward 8'''.splitlines())
        self.assertEqual([["forward", 5], ["down", 5], ["forward", 8]], data)

    def test_basic_solve(self):
        data = [["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]
        self.assertEqual(150, puzzle.solve(data))

    def test_puzzle_answer_part1(self): 
        input = open("02/input.txt", "r")
        data = puzzle.parse(input.readlines()) 
        answer = puzzle.solve(data)  
        input.close()
        self.assertEqual(0, answer)

if __name__ == '__main__':  
    unittest.main()
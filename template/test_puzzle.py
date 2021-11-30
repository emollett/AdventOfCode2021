import unittest  
import puzzle

class TestBasic(unittest.TestCase):  
    def test_pass(self):  
        data = puzzle.parse(open("template\input.txt", "r").readlines())  
        answer = puzzle.solve(data)  
        self.assertEqual(0, answer)

if __name__ == '__main__':  
    unittest.main()
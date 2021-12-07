import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_solve(self):
        data = ['16,1,2,0,4,2,7,1,2,14']
        self.assertEqual(4, puzzle.solve(data))

if __name__ == '__main__':  
    unittest.main()
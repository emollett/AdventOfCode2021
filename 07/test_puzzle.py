import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.parse('''forward 5
        down 5
        forward 8'''.splitlines())
        self.assertEqual([["forward", 5], ["down", 5], ["forward", 8]], data)

if __name__ == '__main__':  
    unittest.main()
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.parse('''0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2'''.splitlines())
        self.assertEqual([([0, 9], [5, 9]), ([8, 0], [0, 8]), ([9, 4], [3, 4]), ([2, 2], [2, 1]), ([7, 0], [7, 4]), ([6, 4], [2, 0]), ([0, 9], [2, 9]), ([3, 4], [1, 4]), ([0, 0], [8, 8]), ([5, 5], [8, 2])], data)

    def test_remove_diagonals(self):
        data = [([0, 9], [5, 9]), ([8, 0], [0, 8]), ([9, 4], [3, 4]), ([2, 2], [2, 1]), ([7, 0], [7, 4]), ([6, 4], [2, 0]), ([0, 9], [2, 9]), ([3, 4], [1, 4]), ([0, 0], [8, 8]), ([5, 5], [8, 2])]
        self.assertEqual([([0, 9], [5, 9]), ([9, 4], [3, 4]), ([2, 2], [2, 1]), ([7, 0], [7, 4]), ([0, 9], [2, 9]), ([3, 4], [1, 4])], puzzle.removeDiagonal(data))

    def test_expand_vents(self):
        data = [([0, 9], [5, 9]), ([9, 4], [3, 4])]
        self.assertEqual([[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [9, 4], [8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [3, 4]], puzzle.expandCoordinates(data))

if __name__ == '__main__':  
    unittest.main()
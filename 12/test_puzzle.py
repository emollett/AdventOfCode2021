from datetime import date
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_dots_parse(self):
        data = puzzle.parse('''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''.splitlines())
        self.assertEqual([(6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11), (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4), (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0)], data[0])

    def test_folds_parse(self):
        data = puzzle.parse('''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=55'''.splitlines())
        self.assertEqual([('y', 7), ('x', 55)], data[1])

    def test_one_fold(self):
        start_coordinates = [(6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11), (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4), (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0)]
        answer = puzzle.oneFold(start_coordinates, ('y', 7))
        self.assertEqual(17, len(answer))

    def test_x_fold(self):
        start_coordinates = [(6, 4), (0, 0), (9, 4), (4, 3), (6, 2), (0, 1), (10, 2), (1, 4), (2, 0), (8, 4), (0, 3), (10, 4), (6, 0), (4, 1), (3, 4), (3, 0), (9, 0)]
        answer = puzzle.oneFold(start_coordinates, ('x', 5))
        self.assertEqual(16, len(answer))

    def test_puzzle_answer_part1(self): 
        input = open("12/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.oneFold(data[0], data[1][0])
        input.close()
        self.assertEqual(724, len(answer))  

    def test_multiple_folds(self):
        data = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''.splitlines()
        self.assertEqual(16, len(puzzle.severalFolds(data)))

    def test_multiple_folds(self):
        data = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''.splitlines()
        answer= puzzle.passwordPicture(data)

    def test_puzzle_answer_part2(self): 
        input = open("12/input.txt", "r")
        data = input.read().splitlines()
        answer = puzzle.passwordPicture(data)
        input.close()

if __name__ == '__main__':  
    unittest.main()
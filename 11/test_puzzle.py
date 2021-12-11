from datetime import date
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = puzzle.parse('''11111
19991
19191
19991
11111'''.splitlines())
        self.assertEqual([[(0, 0), 1], [(1, 0), 1], [(2, 0), 1], [(3, 0), 1], [(4, 0), 1], [(0, 1), 1], [(1, 1), 9], [(2, 1), 9], [(3, 1), 9], [(4, 1), 1], [(0, 2), 1], [(1, 2), 9], [(2, 2), 1], [(3, 2), 9], [(4, 2), 1], [(0, 3), 1], [(1, 3), 9], [(2, 3), 9], [(3, 3), 9], [(4, 3), 1], [(0, 4), 1], [(1, 4), 1], [(2, 4), 1], [(3, 4), 1], [(4, 4), 1]], data)

    def test_one_step(self):
        data = puzzle.oneStep([[(0, 0), 1], [(1, 0), 1], [(2, 0), 1], [(3, 0), 1], [(4, 0), 1], [(0, 1), 1], [(1, 1), 9], [(2, 1), 9], [(3, 1), 9], [(4, 1), 1], [(0, 2), 1], [(1, 2), 9], [(2, 2), 1], [(3, 2), 9], [(4, 2), 1], [(0, 3), 1], [(1, 3), 9], [(2, 3), 9], [(3, 3), 9], [(4, 3), 1], [(0, 4), 1], [(1, 4), 1], [(2, 4), 1], [(3, 4), 1], [(4, 4), 1]])
        self.assertEqual([[(0, 0), 3], [(1, 0), 4], [(2, 0), 5], [(3, 0), 4], [(4, 0), 3], [(0, 1), 4], [(4, 1), 4], [(0, 2), 5], [(4, 2), 5], [(0, 3), 4], [(4, 3), 4], [(0, 4), 3], [(1, 4), 4], [(2, 4), 5], [(3, 4), 4], [(4, 4), 3], [(1, 1), 0], [(3, 1), 0], [(1, 2), 0], [(3, 2), 0], [(1, 3), 0], [(3, 3), 0], [(2, 1), 0], [(2, 3), 0], [(2, 2), 0]], data[0])

    def test_count_flashes(self):
        data = [[(0, 0), 1], [(1, 0), 1], [(2, 0), 1], [(3, 0), 1], [(4, 0), 1], [(0, 1), 1], [(1, 1), 9], [(2, 1), 9], [(3, 1), 9], [(4, 1), 1], [(0, 2), 1], [(1, 2), 9], [(2, 2), 1], [(3, 2), 9], [(4, 2), 1], [(0, 3), 1], [(1, 3), 9], [(2, 3), 9], [(3, 3), 9], [(4, 3), 1], [(0, 4), 1], [(1, 4), 1], [(2, 4), 1], [(3, 4), 1], [(4, 4), 1]]
        steps = 2
        self.assertEqual(9, puzzle.countFlashes(data, steps))
    
    def test_basic_solve(self):
        data = puzzle.parse('''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''.splitlines())
        self.assertEqual(35, puzzle.countFlashes(data, 2))

    def test_basic_solve_bigger_steps(self):
        data = puzzle.parse('''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''.splitlines())
        self.assertEqual(1656, puzzle.countFlashes(data, 100))

    def test_puzzle_answer_part1(self): 
        input = open("11/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.countFlashes(data, 100)
        input.close()
        self.assertEqual(1637, answer)  

    def test_basic_find_synchronisation(self):
        data = puzzle.parse('''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''.splitlines())
        self.assertEqual(195, puzzle.findSynchronisation(data))

    def test_puzzle_answer_part2(self): 
        input = open("11/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.findSynchronisation(data)
        input.close()
        self.assertEqual(0, answer)  

if __name__ == '__main__':  
    unittest.main()
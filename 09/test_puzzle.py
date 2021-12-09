import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_find_horizontal_low_points(self):
        data = puzzle.findLows('''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines())
        self.assertEqual([(1, 0), (9, 0), (0, 1), (3, 1), (6, 1), (9, 1), (2, 2), (7, 2), (9, 2), (2, 3), (6, 3), (1, 4), (6, 4)] ,data)

    # def test_solve_part_1(self):
    #     data= puzzle.parse('''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    #     edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    #     fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    #     fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    #     aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    #     fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    #     dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    #     bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    #     egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    #     gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.splitlines())
    #     self.assertEqual(26, puzzle.solve1(data))

    # def test_puzzle_answer_part1(self): 
    #     input = open("08/input.txt", "r")
    #     data = puzzle.parse(input.read().splitlines())
    #     answer = puzzle.solve1(data)  
    #     input.close()
    #     self.assertEqual(330, answer) 

if __name__ == '__main__':  
    unittest.main()
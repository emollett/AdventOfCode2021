import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_basic_parse(self):
        data = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
        self.assertEqual([(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'], ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])], puzzle.parse(data))

    def test_count_unique(self):
        data = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        self.assertEqual(4, puzzle.countUnique(data))

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

    def test_puzzle_answer_part1(self): 
        input = open("08/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.solve1(data)  
        input.close()
        self.assertEqual(330, answer) 

    # def test_calc_crab_movement_2(self):
    #     self.assertEqual(10, puzzle.calc_movement2(1, 5))

    # def test_basic_solve2(self):
    #     data = [16,1,2,0,4,2,7,1,2,14]
    #     self.assertEqual(168, puzzle.solve(data, '2'))

    # def test_puzzle_answer_part2(self): 
    #     input = open("07/input.txt", "r")
    #     data = list(map(int, input.readline().split(",")))
    #     answer = puzzle.solve(data, '2')  
    #     input.close()
    #     self.assertEqual(94004208, answer)   

if __name__ == '__main__':  
    unittest.main()
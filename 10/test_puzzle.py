from datetime import date
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_find_corrupting_character(self):
        data = '{([(<{}[<>[]}>{[]{[(<()>'
        self.assertEqual('}', puzzle.processBrackets(data))

    def test_basic_solve(self):
        data = puzzle.solve1('''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.splitlines())
        self.assertEqual(26397, data)

    def test_puzzle_answer_part1(self): 
        input = open("10/input.txt", "r")
        data = input.read().splitlines()
        answer = puzzle.solve1(data)  
        input.close()
        self.assertEqual(278475, answer)   

    def test_find_unclosed_brackets(self):
        data = '[({(<(())[]>[[{[]{<()<>>'
        self.assertEqual(['[', '(', '{', '(', '[', '[', '{', '{'], puzzle.processBrackets(data))  

    def test_calculate_autocomplete_score(self):
        data = ['[', '(', '{', '(', '[', '[', '{', '{']
        self.assertEqual(288957, puzzle.calculateAutocompleteScore(data))

    def test_basic_solve2(self):
        data = puzzle.solve2('''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.splitlines())
        self.assertEqual(288957, data) 

    def test_puzzle_answer_part2(self): 
        input = open("10/input.txt", "r")
        data = input.read().splitlines()
        answer = puzzle.solve2(data)  
        input.close()
        self.assertEqual(3015539998, answer)  

if __name__ == '__main__':  
    unittest.main()
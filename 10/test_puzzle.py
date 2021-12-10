import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_find_corrupting_character(self):
        data = '{([(<{}[<>[]}>{[]{[(<()>'
        self.assertEqual('}', puzzle.findCorruptingBracket(data))

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

if __name__ == '__main__':  
    unittest.main()
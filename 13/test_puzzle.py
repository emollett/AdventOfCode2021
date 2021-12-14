from datetime import date
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_template_parse(self):
        data = puzzle.parse('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines())
        self.assertEqual('NNCB', data[0])

    def test_insertions_parse(self):
        data = puzzle.parse('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines())
        self.assertEqual({'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}, data[1])

    def test_one_insertion(self):
        data = puzzle.parse('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines())
        answer = puzzle.oneInsertion(data[0], data[1])
        self.assertEqual('NCNBCHB', answer)

    def test_multiple_insertions(self):
        data = puzzle.parse('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines())
        answer = puzzle.multipleInsertions(data, 4)
        self.assertEqual('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB', answer)

    def test_solce1(self):
        data = puzzle.parse('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines())
        answer = puzzle.solve(data, 10)
        self.assertEqual(1588, answer)

    def test_puzzle_answer_part1(self): 
        input = open("13/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.solve(data, 10)
        input.close()
        self.assertEqual(2509, answer)  

    # def test_puzzle_answer_part1(self): 
    #     input = open("13/input.txt", "r")
    #     data = puzzle.parse(input.read().splitlines())
    #     answer = puzzle.solve(data, 40)
    #     input.close()
    #     self.assertEqual(0, answer)  


if __name__ == '__main__':  
    unittest.main()
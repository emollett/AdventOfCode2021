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

    def test_solve1(self):
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
        input = open("14/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.solve(data, 10)
        input.close()
        self.assertEqual(2509, answer)  
    
    def test_one_pair(self):
        pair = 'NN'
        insertion_map = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
        answer = puzzle.onePair(pair, insertion_map)
        self.assertEqual(['NC', 'CN'], answer)

    def test_create_initial_frequencies(self):
        insertion_map = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
        answer = puzzle.createInitialFrequencies(insertion_map)
        self.assertEqual({'CH': 0, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 0, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 0, 'NB': 0, 'BN': 0, 'BB': 0, 'BC': 0, 'CC': 0, 'CN': 0}, answer)

    def test_update_frequencies(self):
        pairs = [('NC', 2), ('CN', 2)]
        frequencyMap = {'CH': 0, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 0, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 0, 'NB': 0, 'BN': 0, 'BB': 0, 'BC': 0, 'CC': 0, 'CN': 0}
        answer = puzzle.updatePairFrequencies(pairs, frequencyMap)
        self.assertEqual({'CH': 0, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 0, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 2, 'NB': 0, 'BN': 0, 'BB': 0, 'BC': 0, 'CC': 0, 'CN': 2}, answer)

    def test_create_new_pairs(self):
        frequencyMap = {'CH': 0, 'HH': 0, 'CB': 1, 'NH': 0, 'HB': 0, 'HC': 0, 'HN': 0, 'NN': 1, 'BH': 0, 'NC': 1, 'NB': 0, 'BN': 0, 'BB': 0, 'BC': 0, 'CC': 0, 'CN': 0}
        insertion_map = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
        elementFrequencies = {'A': 0, 'B': 1, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 2, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        answer = puzzle.createNewPairs(frequencyMap, insertion_map)
        self.assertEqual({'CH': 1, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 1, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 1, 'NB': 1, 'BN': 0, 'BB': 0, 'BC': 1, 'CC': 0, 'CN': 1}, answer)

    def test_solve2(self):
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
        answer = puzzle.solve2(data, 2)
        self.assertEqual(5, answer)  

    def test_solve2_more(self):
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
        answer = puzzle.solve2(data, 3)
        self.assertEqual(7, answer) 

    def test_solve2_bigger(self):
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
        answer = puzzle.solve2(data, 10)
        self.assertEqual(1588, answer)   

    def test_puzzle_answer_part1_with_solve2(self): 
        input = open("14/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.solve2(data, 10)
        input.close()
        self.assertEqual(2509, answer)       

    def test_puzzle_answer_part1(self): 
        input = open("14/input.txt", "r")
        data = puzzle.parse(input.read().splitlines())
        answer = puzzle.solve2(data, 40)
        input.close()
        self.assertEqual(2827627697643, answer)  


if __name__ == '__main__':  
    unittest.main()
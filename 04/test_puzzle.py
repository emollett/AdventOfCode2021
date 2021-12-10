import unittest  
import puzzle

class TestBasic(unittest.TestCase): 
    
    def test_parse_drawn_numbers(self):
        data = puzzle.parseDrawnNumbers('''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7'''.splitlines())        
        self.assertEqual([7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], data)

    def test_parse_boards(self):
        data = puzzle.parseBoards('''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7'''.splitlines())        
        self.assertEqual([[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]], data)

    def test_rotation(self):
        input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        data = puzzle.rotateInput(input)
        self.assertEqual(['011110011100', '010001010101', '111111110000', '011101100011', '000111100100'], data)

    # def test_basic_solve(self):
    #     data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    #     self.assertEqual(198, puzzle.solve(data))

    # def test_puzzle_answer_part1(self): 
    #     input = open("03/input.txt", "r")
    #     answer = puzzle.solve(input)  
    #     input.close()
    #     self.assertEqual(4138664, answer)

    # def test_solve2_oxygen(self):
    #     rotatedInput = ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
    #     originalInput = puzzle.rotateInput(rotatedInput)
    #     self.assertEqual(23, puzzle.calculateOxygenRating(rotatedInput, originalInput))

    # def test_solve2_co2(self):
    #     rotatedInput = ['011110011100', '010001010101', '111111110000', '011101100011', '000111100100']
    #     originalInput = puzzle.rotateInput(rotatedInput)
    #     self.assertEqual(10, puzzle.calculateCO2Rating(rotatedInput, originalInput))

    # def test_solve2_full(self):
    #     input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    #     self.assertEqual(230, puzzle.solve2(input))

    # def test_puzzle_answer_part2(self): 
    #     input = open("03/input.txt", "r")
    #     answer = puzzle.solve2(input)  
    #     input.close()
    #     self.assertEqual(4273224, answer)

if __name__ == '__main__':  
    unittest.main()
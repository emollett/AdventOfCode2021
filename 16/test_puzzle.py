from datetime import date
import unittest  
import puzzle

class TestBasic(unittest.TestCase):  

    def test_template_parse(self):
        data = puzzle.parse('38006F45291200')
        self.assertEqual('00111000000000000110111101000101001010010001001000000000', data)

    def test_decode_header(self):
        binary = '110100101111111000101000'
        self.assertEqual((6, 4, '101111111000101000'), puzzle.decodeHeader(binary))

    def test_decode_literal_value_packet(self):
        binary = '101111111000101000'
        self.assertEqual((2021, '000'), puzzle.decodeLiteral(binary))

    def test_decode_length_id(self):
        binary = '00000000000110111101000101001010010001001000000000'
        self.assertEqual(('length', 27), puzzle.decodeLengthID(binary))

    def test_decode_length_id_2(self):
        binary = '10000000001101010000001100100000100011000001100000'
        self.assertEqual(('number', 3), puzzle.decodeLengthID(binary))

    def test_solve(self):
        hex = '8A004A801A8002F478'
        self.assertEqual(16, puzzle.solve(hex))


    # def test_puzzle_answer_part1(self): 
    #     input = open("14/input.txt", "r")
    #     data = puzzle.parse(input.read().splitlines())
    #     answer = puzzle.solve(data, 10)
    #     input.close()
    #     self.assertEqual(2509, answer)  

if __name__ == '__main__':  
    unittest.main()
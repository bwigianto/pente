import unittest

from pente import *

class PenteTest(unittest.TestCase):

    def test_add_stone_on_empty_board(self):
        start = [[0,0],[0,0]]
        expected = [[0,0],[1,0]]
        self.assertEqual(expected, add_stone(start, 1, (1, 0)))

    def test_add_stone_removes_oppopnent_stones(self):
        start = [[1,2,2,0]]
        expected = [[1,0,0,1]]
        self.assertEqual(expected, add_stone(start, 1, (0, 3)))

    def test_nonzero_is_invalid_move(self):
        start = [[1,0],[0,0]]
        self.assertFalse(valid_move(start, (0, 0)))

    def test_zero_is_valid_move(self):
        start = [[1,0],[0,0]]
        self.assertTrue(valid_move(start, (0, 1)))

    def test_five_in_a_row_false(self):
        start = [[1, 0, 0, 0, 0]]
        self.assertFalse(five(start))

    def test_five_in_a_row_true(self):
        start = [[1, 1, 1, 1, 1]]
        self.assertTrue(five(start))
if __name__ == '__main__':
    unittest.main()

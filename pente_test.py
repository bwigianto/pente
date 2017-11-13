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
        self.assertFalse(is_valid(start, (0, 0)))

    def test_zero_is_valid_move(self):
        start = [[1,0],[0,0]]
        self.assertTrue(is_valid(start, (0, 1)))

if __name__ == '__main__':
    unittest.main()

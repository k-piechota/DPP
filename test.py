import unittest
from unittest.mock import patch
import game.Board
import xmlrunner


class TestBoard(unittest.TestCase):
    def test_correct_move(self):
        with patch.object(game.Board.Board, '_create_board', return_value=[[1]]):
            self.assertEqual(game.Board.Board(1, 1, 'house.png').is_painted(0, 0), True)

    def test_invalid_move(self):
        with patch.object(game.Board.Board, '_create_board', return_value=[[0]]):
            self.assertEqual(game.Board.Board(1, 1, 'house.png').is_painted(0, 0), False)

    def test_invalid_filename_raises_BoardException(self):
        with self.assertRaisesRegex(game.Board.BoardException, "Invalid filename"):
            game.Board.Board(1, 1, 'invalid_filename.png')


if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()

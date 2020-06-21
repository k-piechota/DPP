import unittest
from unittest.mock import patch
import game.Board
import testlink


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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    out = unittest.TextTestRunner(verbosity=2).run(suite)
    print(out)
    if out.errors or out.failures:
        result = "f"
    else:
        result = "p"

    url = 'http://127.0.0.1/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
    key = '5ac847a7aec8bbf12e62842a6aa8cbb6'

    tls = testlink.TestlinkAPIClient(url, key)
    tls.reportTCResult(4, 8, 'Sample build', result, str(out))

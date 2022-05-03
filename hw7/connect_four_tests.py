"""
Hyojin Kwak
CS 5001
HW7 Unittest.Testcase for each method in ConnectFour class.
2022/4/19
"""


from connect_four import ConnectFour
import unittest


class ConnectFourTest(unittest.TestCase):
    def test_init(self):
        # testing constructor and its objects
        game = ConnectFour()
        self.assertEqual(game.board[0][0], ' ')
        self.assertEqual(game.col, 7)
        self.assertEqual(game.row, 6)
        self.assertEqual(game.piece, '')
        self.assertEqual(game.turn_queue, ['X'])
        self.assertEqual(game.tracking_piece, [])

    def test_str_(self):
        # testing the string method
        game = ConnectFour()
        self.assertTrue(game.__str__())

    def test_add_piece_invalid(self):
        # testing if it correcrly raises the error with invalid column
        try:
            game = ConnectFour()
            self.assertTrue(game.add_piece(-1))
        except ValueError:
            print('value error correctly raised')

    def test_add_piece_invalid1(self):
        # testing add piece method with too big input (invalid)
        try:
            game = ConnectFour()
            self.assertTrue(game.add_piece(7))
        except ValueError:
            print('value error correctly raised')

    def test_add_piece_board_change(self):
        game = ConnectFour()
        game.add_piece(0)
        self.assertEqual(game.board[-1], ['X', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_is_column_full(self):
        # testing if the method returns true when the col. is full
        game = ConnectFour()
        game.board[0][0] = 'X'
        game.board[1][0] = 'X'
        game.board[2][0] = 'X'
        game.board[3][0] = 'X'
        game.board[4][0] = 'X'
        game.board[5][0] = 'X'
        self.assertEqual(game.is_column_full(0), True)

    def test_player_turn(self):
        # the first returned piece should be X
        game = ConnectFour()
        self.assertEqual(game.player_turn(), 'X')

    def test_board_full(self):
        # the board should not be full in the beginning
        game = ConnectFour()
        self.assertEqual(game.is_board_full(), False)

    def test_is_gameover(self):
        # when the board is full game should be over
        game = ConnectFour()
        for row in range(len(game.board)):
            for col in range(len(game.board[0])):
                game.board[row][col] = 'X'
        self.assertEqual(game.is_game_over(), True)

    def test_get_winner_full_board(self):
        # when the board is full, (tie), winner is None
        game = ConnectFour()
        for row in range(len(game.board)):
            for col in range(len(game.board[0])):
                game.board[row][col] = 'X'
        self.assertEqual(game.get_winner(), None)

    def test_get_winner_at_start(self):
        # when the game starts there is no winner yet
        game = ConnectFour()
        self.assertEqual(len(game.tracking_piece), 0)
        self.assertEqual(game.get_winner(), None)

    def test_get_winner_vertical(self):
        # winner is X in this vertical test case
        game = ConnectFour()
        game.board[0][0] = 'X'
        game.board[1][0] = 'X'
        game.board[2][0] = 'X'
        game.board[3][0] = 'X'
        game.tracking_piece = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertEqual(game.get_winner(), 'X')

    def test_get_winner_horizontal(self):
        # winner is O in this horizontal test case
        game = ConnectFour()
        game.board[0][0] = 'O'
        game.board[0][1] = 'O'
        game.board[0][2] = 'O'
        game.board[0][3] = 'O'
        game.tracking_piece = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.assertEqual(game.get_winner(), 'O')

    def test_get_winner_diagonal(self):
        # winner is O in this diagonal test case
        game = ConnectFour()
        game.board[0][0] = 'O'
        game.board[1][1] = 'O'
        game.board[2][2] = 'O'
        game.board[3][3] = 'O'
        game.tracking_piece = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(game.get_winner(), 'O')

    def test_undo(self):
        # when there is no more to undo a piece, error should be raised
        try:
            game = ConnectFour()
            self.assertTrue(game.undo())
        except ValueError:
            print('value error raised correctly')


def main():
    # verbosity = 3 for more detail in test result
    unittest.main(verbosity=3)


if __name__ == '__main__':
    main()

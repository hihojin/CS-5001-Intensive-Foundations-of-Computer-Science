"""
Hyojin Kwak
CS 5001
HW7 CONNECT FOUR COMMAND LINE GAME
2022/4/19
"""


class ConnectFour:
    """connect four board game"""
    def __init__(self):
        """constructor
        param: None
        return objects"""
        self.row = 6
        self.col = 7
        self.board = [[' '] * self.col for col in range(self.row)]
        # depends on whose turn it is.
        # when player turn is determined. will be set to X or O
        self.piece = ''
        self.turn_queue = ['X']
        # tracking stack.
        self.tracking_piece = []

    def __str__(self):
        """returns string representation of game board"""
        output_board = ''
        for row in range(len(self.board)):
            line = ''
            for col in range(len(self.board[0])):
                line += '|' + self.board[row][col]
            line += '|' + '\n' + ('-' * (self.col * 2 + 1))
            output_board += line + '\n'
        return output_board

    def add_piece(self, column):
        """param: column: int, column to place the piece
        # if the column is invalid (bigger, smaller than board size)
        # or if the column is full, or game already is over,
        # we can't add a piece; raise a valueError.
        # otherwise place piece in the lowest empty row of the given column.
        # returns None"""

        # column 0 ~ 6 is valid
        if column < 0:
            raise ValueError('column is too small')
        # self.col == 7
        if column > (self.col - 1):
            raise ValueError('column is too big')
        if self.is_column_full(column):
            raise ValueError('column is full')
        if self.is_game_over():
            raise ValueError('game is over')

        piece = self.player_turn()
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = piece
                self.tracking_piece.append((row, column))
                return

    def is_column_full(self, column):
        """
        param: int, column
        returns: Boolean True if column is full.
        # when board[row==0][given column by user] is not empty(' ')
        # it means the column is all occupied. because the lowest[row] of
        # the column gets filled and the upper indexes get filled later.
        """
        if self.board[0][column] == 'X' or self.board[0][column] == 'O':
            return True
        return False

    def player_turn(self):
        """
        using queue to determine player's turn
        Param: None
        Return: self.piece (X, O)
        """
        player_piece = self.turn_queue.pop(0)
        if player_piece == 'X':
            self.turn_queue.append('O')
            self.piece = 'X'
            return self.piece
        else:
            self.turn_queue.append('X')
            self.piece = 'O'
            return self.piece

    def is_board_full(self):
        """
        param: None
        return: Boolean True is the board is full
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == ' ':
                    return False
        return True

    def is_game_over(self):
        """
        checking the game over conditions here.
        Param: None
        Return: Boolean
        """
        # when the board is full or when there is a winner
        if self.is_board_full():
            return True
        # if no winner yet and the game board is not full, should playing
        elif self.get_winner() is None and not self.is_board_full():
            return False
        elif self.get_winner() is not None:
            return True

    def get_winner(self):
        """
        # each time a piece gets added to board[row][col]
        # we check in 8 directions and check if in any direction
        # 4 of the same pieces are aligned (either X or O), including
        # the current piece. return X or O (as a winner).
        # else: game is not over and there is no winners yet (still playing)
        # or the game board is full(tie) - game over
        param: None
        return: None, X, O (winners) string or Nonetype
        """
        if self.is_board_full():
            return None
        # at first before any piece was added
        # should continue game: not is_ case
        if len(self.tracking_piece) == 0:
            return None

        # right, down, left, up, NE, SE, SW, NW
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                      (-1, 1), (1, 1), (1, -1), (-1, -1)]
        for i in range(8):
            current = self.tracking_piece[-1]  # (row, col)
            for repeat in range(3):
                is_winner = False
                next_row = directions[i][0] + current[0]
                next_col = directions[i][1] + current[1]
                valid_row = 0 <= next_row < len(self.board)
                valid_col = 0 <= next_col < len(self.board[0])
                if valid_row and valid_col:
                    piece = self.board[current[0]][current[1]]
                    if piece == self.board[next_row][next_col]:
                        # if it is the same piece in neighbor, we want to
                        # check if its two other neighbors are the same
                        # in the same direction we found the same piece
                        current = (next_row, next_col)
                        is_winner = True
                    else:
                        is_winner = False
                        break
                else:
                    break
            if is_winner:
                return self.board[current[0]][current[1]]  # returns X or O
        # there is no winner yet and game board not full -- continue playing
        return None

    def undo(self):
        """
        undo the latest piece off from the board using
        the stack list implementation
        param: None
        return: None
        """
        if len(self.tracking_piece) <= 0:
            raise ValueError('no more piece to undo')
        recent_piece = self.tracking_piece.pop()
        self.board[recent_piece[0]][recent_piece[1]] = ' '

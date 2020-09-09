from math import sqrt


class Board:

    ERROR = -1

    def __init__(self, size=(9, 9)):
        self.height, self.width = size
        self.board = self.__init_board()
        self.mini_box_height = int(sqrt(self.height))
        self.mini_box_width = int(sqrt(self.width))
        self.valid_nums = [num for num in range(self.mini_box_width * self.mini_box_height)]

    def __str__(self):
        output = ''
        for row in range(self.height):
            if row % self.mini_box_height == 0 and row > 0:
                output += ' - ' * (self.width - 2) + '\n'
            for col in range(self.width):
                if col % self.mini_box_width == 0 and col > 0:
                    output += '| '
                output += str(self.board[row][col])
                output += ' '
            output += '\n'
        return output

    def is_legal(self, row, col, num):
        """
        Given the cell coordinates and attempted number, returns whether or not
        the number can legally be placed there. Does not account for if the desired cell is already accupied
        :param row: The row
        :param col: The column
        :param num: The number
        :return: True iff legal placement
        """
        # Check the rest of the row
        for other_col_coordinate in range(self.width):
            if self.board[row][other_col_coordinate] == num:
                return False

        # Check the rest of the column
        for other_row_coordinate in range(self.height):
            if self.board[other_row_coordinate][col] == num:
                return False

        # Check the mini box that the cell resides in
        col_shift = col // self.mini_box_width
        row_shift = row // self.mini_box_height

        for _row in range(self.mini_box_height):
            for _col in range(self.mini_box_width):
                if self.board[row_shift * self.mini_box_height + _row][col_shift * self.mini_box_width + _col] == num:
                    return False

        return True

    def apply_move(self, row, col, num):
        """
        Attempts to apply the given number to the given cell.
        Returns True iff successful
        :param row: The row
        :param col: The column
        :param num: The number
        :return: True iff successful
        """
        if 0 <= row < self.height and 0 <= col < self.width and num in self.valid_nums:
            self.board[row][col] = num
            return True
        return False

    def find_empty_cell(self):
        """Returns an empty cell in the board. If none exist, return (Board.ERROR, Board.ERROR)"""
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 0:
                    return row, col
        return Board.ERROR, Board.ERROR

    def __init_board(self):
        """Initializes a board"""
        board = []
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                new_row.append(0)
            board.append(new_row)
        return board

    def set_board(self, board):
        """Sets the board to the given board (a 2D array). Does not check for validity
        and does not update other internal variables connected to the board.
        Useful only for setting the board before the game begins"""
        self.board = board


if __name__ == '__main__':
    game = Board()
    test_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    game.set_board(test_board)
    print(game)
    print(game.is_legal(0, 0, 2))
    print(game.is_legal(6, 1, 8))
    print(game.is_legal(1, 1, 6))
    print(game.is_legal(0, 6, 8))

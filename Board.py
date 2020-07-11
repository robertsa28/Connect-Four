# Board.py, by Barb Wahl (11-18-18)
# Modified by:
#     STUDENT NAME: Alex Roberts
#     DATE: December 6th, 2018

# The Connect Four board is represented by a list of seven columns,
# where each column is a list with entries from {'.', 'X', 'O'}.
# An entry equal to 'X' represents a checker belonging to player 1, and
# an entry equal to 'O' represents a checker belonging to player 2. An
# entry equal to '.' is an open spot on the board.

# If C is a column in the board, then C[0] represents the checker at the
# TOP of the column, C[1] is the next checker DOWN, and so on. An "empty"
# column looks like ['.', '.', '.', '.', '.', '.'] and is filled from
# right to left ("bottom" to "top") by replacing '.' with 'X' or 'O'
# as checkers are dropped into that column.

# A player wins by getting four of their checkers adjacent on the board,
# either vertically, horizontally, or diagonally (left-to-right or right-
# to-left). If the board becomes full without a winner, the game ends
# due to deadlock.

from copy import copy

class Board:
    # Class Constants
    NUM_ROWS = 6
    NUM_COLS = 7
    MAX_MOVES = 42

    ###
    # __init__
    # The Board "constructor" method.
    # Initializes a new Board object to create an empty board for game play.
    ###
    def __init__(self):
        blank_col = ['.', '.', '.', '.', '.', '.']
        self.cols = []
        for c in range(Board.NUM_COLS):
            self.cols.append(copy(blank_col))  # copy to prevent aliasing

    ###
    # __str__
    # The "to string" method for the Board class.
    # Activated when a Board object is printed; returns the string
    # representation of a Board.
    ###
    def __str__(self):
        border = '=' * 29 + "\n"
        acc = "\n  0   1   2   3   4   5   6   \n"    # column indexs
        acc += border                     # top border
        for row in range(Board.NUM_ROWS):
            acc += self.row_to_string(row) + "\n"
        acc += border

        return acc

    ###
    # fill
    # For testing; fills a Board with the characters from a provided string.
    # The first column is filled, then the second, and so on.
    # parameters:  s, a string of length 42 or more
    ###
    def fill(self, s):
        # use chars in s to fill columns of Board
        for c in range(Board.NUM_COLS):
            # stop minus start equals number of rows in board, which
            # is the length of one column
            start = Board.NUM_ROWS * c
            stop = Board.NUM_ROWS * (c + 1)
            self.cols[c] = list(s[start : stop])

    ###
    # row_to_string
    # Helper for the __str__ method, returns the string for printing
    # a single row of the board.
    ###
    def row_to_string(self, row):
        acc = '|'
        for col in range(Board.NUM_COLS):
            acc = acc + ' ' + self.cols[col][row] + ' |'

        return acc

    ###
    # take_turn
    # prompts a player to choose a column number (an integer in the range
    # 0 through 6)
    # parameters: player_num, an integer, either 1 or 2
    # return: the tuple (col, row) indicating where the checker was placed;
    #         the column index `col` is determined by prompting the player to
    #         enter a valid column number
    # note:   A valid column cannot be completely full of checkers.
    ###
    def take_turn(self, player_num):
        # TO BE IMPLEMENTED
        if player_num == 1:
        	ch = "X"
        else:
        	ch = "O"
        print("Player", player_num)
        player_input = int(input("Please input a valid column number: "))
        if self.is_valid_move(player_input):
        	return self.place_checker_in_column(ch, player_input)
        else:
        	print("The column you entered is not valid! Please try again.")
        	return self.take_turn(player_num)

    ###
    # is_valid_move
    # helper for take_turn; checks that a given column index is a valid move
    # return: True if col is in range(Board.NUM_COLS) and that column of the
    #         board is not completely full of checkers.
    ###
    def is_valid_move(self, col):
        # TO BE IMPLEMENTED
        if col in range(Board.NUM_COLS) and "." in self.cols[col]:
        	return True
        return False

    ###
    # place_checker_in_column
    # updates the board by adding a specific checker to a given column
    # parameters: `ch`, a character representing the checker ('X' or 'O')
    #             `col`, an integer in range(Board.NUM_COLS)
    # return: the tuple (col, row) indicating where the checker was placed
    # note:   The LAST occurrence of '.' in the specified column is replaced
    #         by the value of `ch`.
    ###
    def place_checker_in_column(self, ch, col):
        # TO BE IMPLEMENTED
        for row in range(len(self.cols[col]) - 1, -1, -1):
        	if self.cols[col][row] == ".":
        		self.cols[col][row] = ch
        		return (col, row)

    ###
    # has_winner
    # verifies whether the checker that was just played at a specific position
    # on the board has created a winning condition
    # paramters: `col`, an integer in range(Board.NUM_COLS)
    #            `row`, an integer in range(Board.NUM_ROWS)
    # return: True if there is a winner in the row indexed by `row`, the column
    #         indexed by `col`, or one of the two diagonals through (col, row);
    #         otherwise, False.
    ###
    def has_winner(self, col, row):
        # check column `col`
        if self.has_winning_substring(self.get_col(col)):
            return True

        # check row `row`
        if self.has_winning_substring(self.get_row(row)):
            return True

        # check LR_diag through (col, row)
        if self.has_winning_substring(self.get_LR_diag(col, row)):
            return True

        # check RL_diag through (col, row)
        if self.has_winning_substring(self.get_RL_diag(col, row)):
            return True

        # no winner
        return False

    ###
    # has_winning_substring
    # helper for has_winner, takes a string of characters and searches
    #     for a winning substring
    # parameters: `s`, a string
    # return: True if `s` has substring "XXXX" or "OOOO"; otherwise, False
    ###
    def has_winning_substring(self, s):
        # TO BE IMPLEMENTED
        if len(s) < 4:
        	return False
        else:
        	for i in range(0, len(s) - 3):
        		if s[i:i + 4] == "XXXX" or s[i:i + 4] == "0000":
        			return True
        return False

    ###
    # get_row
    # helper for has_winner, returns a string representation of a given row
    # parameters: `row`, an integer in range(Board.NUM_ROWS)
    # return: a string accumulated by concatenating the characters in the row
    #         indexed by `row`
    ###
        # TO BE IMPLEMENTED
    def get_row(self, row):
    	r = ""
    	for i in self.cols:
        	r = r + i[row]
    	return r

    ###
    # get_col
    # helper for has_winner, returns a string representation of a given column
    # parameters: `col`, an integer in range(Board.NUM_COLS)
    # return: a string accumulated by concatenating the characters in the
    #         column indexed by `col`
    ###
    def get_col(self, col):
        # TO BE IMPLEMENTED
        c = ""
        for i in self.cols[col]:
        	c += str(i)
        return c

    ###
    # get_LR_diag
    # helper for has_winner, returns a string representation of a given
    #     left-to-right diagonal
    # parameters: `col`, an integer in range(Board.NUM_COLS)
    #             `row`, an integer in range(Board.NUM_ROWS)
    # return: a string accumulated by concatenating the characters in the
    #         left-to-right diagonal which passes through board location
    #         (col, row)
    ###
    def get_LR_diag(self, col, row):
        cols = []
        rows = []
        # move left and up to find the first position in the diagonal
        while col > 0 and row > 0:
            col -= 1
            row -= 1
        # move right and down to accumulate the characters along the diagonal
        while col < Board.NUM_COLS and row < Board.NUM_ROWS:
            cols.append(col)
            rows.append(row)
            col += 1
            row += 1

        return self.get_string_from(cols, rows)

    ###
    # get_RL_diag
    # helper for has_winner, returns a string representation of a given
    #     right-to-left diagonal
    # parameters: `col`, an integer in range(Board.NUM_COLS)
    #             `row`, an integer in range(Board.NUM_ROWS)
    # return: a string accumulated by concatenating the characters in the
    #         right-to-left diagonal which passes through board location
    #         (`col`, `row`)
    ###
    def get_RL_diag(self, col, row):
        cols = []
        rows = []
        # move right and up to find the first position in the diagonal
        while col < Board.NUM_COLS - 1 and row > 0:
            col += 1
            row -= 1
        # move left and down to accumulate the characters along the diagonal
        while col >= 0 and row < Board.NUM_ROWS:
            cols.append(col)
            rows.append(row)
            col -= 1
            row += 1

        return self.get_string_from(cols, rows)

    ###
    # get_string_from
    # helper for get_LR_diag and get_RL_diag, takes parallel lists of
    #     column and row indices and returns the corresponding string
    #     of characters from those positions on the board
    # parameters: C, a list of column indices
    #             R, a list of row indices where len(R) = len(C)
    # return: the string of characters from locations (C[0], R[0]),
    #         (C[1], R[1]), (C[2], R[2]), etc.
    ###
    def get_string_from(self, C, R):
        acc = ""
        for i in range(len(C)):
            acc += self.cols[C[i]][R[i]]
        return acc

# Testing function for Board class
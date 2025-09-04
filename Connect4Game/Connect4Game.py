from abc import (ABC, abstractmethod)


class Connect4GameStrategy(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def strategy(self, game_safety_copy):
        ...


class Connect4Game:
    """
    Class has functions to validate moves, make a move, and check for winning players.
    The class also stores the board variable, current player, and winner.
    """
    def __init__(self):
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
        self.winner = None

    def is_valid_move(self, column):
        """
        Checks the column to see if it is a number between 0 and 7 and if the column has available spaces.
        A boolean is returned.
        """
        if not (0 <= column < 7):
            return False
        return self.board[0][column] == 0

    def make_move(self, column):
        """
        The column in which the player would like to play their moved is passed in.
        The move is validated, if validated, the move is stored in the game board.
        Checks if there is a winner and sets the winning player.
        In no winner, update player to next player
        No value is returned.
        """
        # if either the move is not validated or there is a winner, the move is not stored
        if not self.is_valid_move(column) or self.winner is not None:
            return

        # loops through each move in a column, starting with 5 and ending in 0
        for row in range(5, -1, -1):
            # if value in the board is 0, the move is available
            if self.board[row][column] == 0:
                # set the board value to the current player
                self.board[row][column] = self.current_player
                # checks if there is now a winner
                if self.check_winner(row, column):
                    # if winner, set winning player to current player
                    self.winner = self.current_player
                else:
                    # since the player is either 1 or 2, subtract the current player from 3 so the next player is up
                    self.current_player = 3 - self.current_player
                return

    def check_winner(self, row, col):
        """
        Using in the last played move, by passing in the row and col, checks if there is now a winner.
        A boolean is returned
        """
        # for each of the winning directions, same row, same column, same diagonal down-right, same diagonal up-right
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        results = [self.check_line(row, col, dr, dc) for dr, dc in directions]
        # returns true or false if there is a winning combination
        return any(results)

    def check_line(self, row, col, dr, dc):
        """
        For a winning direction, checks if at least 4 values are the same in a row for the current player.
        A boolean is returned.
        """
        count = 0
        row = row - dr * 3
        col = col - dc * 3
        # for the 7 available spots in a line
        for _ in range(7):
            # checks if the value is stored the same and the value in spot before it, and it's for the current player.
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                # adds to the number of same values in a line
                count += 1
                # if the count reaches 4, we have a winner, return True
                if count == 4:
                    return True
            # resets the count to 0 as the values in the line are not consistently the same
            else:
                count = 0
            row += dr
            col += dc

        return False

"""
Connect4Game and strategy functions.

This module defines:
    - Connect4GameStrategy: a base class to play connect four game with AI strategy.
    - Connect4Game: the game engine with move validation and winner detection.

Assumptions:
    - Connect4Game Board size: 6 rows × 7 columns.
    - Column indices: integers in [0..6] (inclusive).
    - Players are 1 and 2 ids
    - Winner is set with the winning player id
    - A move is valid if the column is within the 7 columns and the column has available spaces out of 6
"""

from abc import (ABC, abstractmethod)


class Connect4GameStrategy(ABC):
    """Base class for Connect4Game strategies.

    Subclasses must implement a strategy function, passing is a safe copy of the game board.
    """

    def __init__(self):
        """Initialize an instance of Connect4GameStrategy."""
        ...

    @abstractmethod
    def strategy(self, game_safety_copy):
        """Implement the strategy for an instance of Connect4GameStrategy."""
        ...


class Connect4Game:
    """Connect4Game engine.

    Responsibilities:
        - Validate each move to ensure within the 7 available columns and there is available spaces in the column
        - Save a move in the game board
        - Check for a winning player

    Attributes:
        board: 6×7 grid. 0 values for available moves, 1 or 2 for players move
        current_player: The player to move next (1 or 2).
        winner: None until a player wins, the player id (1 or 2) is set as winner
    """

    def __init__(self):
        """Initialize an instance of Connect4GameStrategy."""
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
        self.winner = None

    def is_valid_move(self, column):
        """Return whether the specified column is a valid move.

        Args:
            column (int): Column index 0-6.

        Returns:
            bool: True if column is within the 7 column range and the column is not (6 is the max)
            False otherwise.
        """
        if not (0 <= column < 7):
            return False
        return self.board[0][column] == 0

    def make_move(self, column):
        """Save the current players move in the specified column.

        This method:
            - Validates the move (within column range, and available space in column)
            - Saves the move in the first available space in the specified columns
            - Checks if the move resulted in a win and if so, updates the winner to the current player
            - If no winner, the play moves on to next player, current player is swapped.

        Args:
            column (int): column index to save the current players move

        Returns:
            None
        """
        # Return if either the move is not validated or there is a winner.
        if not self.is_valid_move(column) or self.winner is not None:
            return

        # Check the columns for the first available spot closest the bottom, starting with 5 and ending in 0
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                # Check if there is now a winner, if so update winning player
                if self.check_winner(row, column):
                    self.winner = self.current_player
                else:
                    # Set next player, 1 or 2 (using 3 minus current player to get opposite player).
                    self.current_player = 3 - self.current_player
                return

    def check_winner(self, row, col):
        """Determine if the last move at (row, col) produced a win.

        Args:
            row (int): Row index of the last move, number 0-5.
            col (int): Column index of the last move, number 0-6

        Returns:
            bool: True if there are 4 values stored in a line in any 4 directions:
            same row, same column, same diagonal down-right, same diagonal up-right
        """
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        results = [self.check_line(row, col, dr, dc) for dr, dc in directions]
        return any(results)

    def check_line(self, row, col, dr, dc):
        """For a specific move (row and column combination), check for 4 consecutive current player moves in specified direction.

        Args:
            row (int): Row index of the last move, number 0-5.
            col (int): Column index of the last move, number 0-6
            dr (int): Row step per cell (e.g., 0, 1, or -1).
            dc (int): Column step per cell (e.g., 1 or 0).

        Returns:
            bool: True if at least four consecutive spaces is the current player in the specified direction;
            False otherwise.

        """
        count = 0
        row = row - dr * 3
        col = col - dc * 3
        for _ in range(7):
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            row += dr
            col += dc

        return False

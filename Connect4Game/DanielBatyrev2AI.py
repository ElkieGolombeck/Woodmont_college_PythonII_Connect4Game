"""
Connect4Game Strategy for Player 2.

This module defines:
    - RandomStrategy2: class for player with the first available move selection for available moves
"""

import Connect4Game as Game
import random


class RandomStrategy2(Game.Connect4GameStrategy):
    """Random AI Strategy for a Connect4Game.

    Responsibilities:
        - Get Random AI Strategy move for Connect4Game board.

    Attributes:
        name: player's name

    Note:
        Inherits the Connect4GameStrategy class to validate the move strategy
    """

    def __init__(self, name="Daniel Batyrev 2"):
        """Initialize an instance of RandomStrategy2."""
        self.name = name

    @classmethod
    def strategy(cls, game_safety_copy):
        """
        Get first move from a list of all valid and available moves.

        Args:
            game_safety_copy: copy of the current board with all attributes.

        Returns:
            int: first column picked from all valid moves
        """
        valid_moves = list()
        # Loop through 7, as the game board has 7 columns.
        for col in range(7):
            # Validate whether a move in that column is valid, and append to list of valid moves.
            if game_safety_copy.is_valid_move(col):
                valid_moves.append(col)
        # Return the first column on the list.
        return min(valid_moves)

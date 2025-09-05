"""
Connect4Game Strategy for Player1.

This module defines:
    - RandomStrategy: class for player with random choice selection for available moves
"""

import Connect4Game as Game
import random


class RandomStrategy(Game.Connect4GameStrategy):
    """Random AI Strategy for a Connect4Game.

    Responsibilities:
        - Get Random AI Strategy move for Connect4Game board.

    Attributes:
        name: player's name

    Note:
        Inherits the Connect4GameStrategy class to validate the move strategy
    """

    def __init__(self, name="Daniel Batyrev"):
        """Initialize an instance of RandomStrategy."""
        self.name = name

    @classmethod
    def strategy(cls, game_safety_copy):
        """
        Randomly get a move from a list of all valid and available moves.

        Args:
            game_safety_copy: copy of the current board with all attributes.

        Returns:
            int: random choice column picked from all valid moves
        """
        valid_moves = list()
        # Loop through 7, as the game board has 7 columns.
        for col in range(7):
            # Validate whether a move in that column is valid, and append to list of valid moves.
            if game_safety_copy.is_valid_move(col):
                valid_moves.append(col)
        # Return a random choice column
        return random.choice(valid_moves)

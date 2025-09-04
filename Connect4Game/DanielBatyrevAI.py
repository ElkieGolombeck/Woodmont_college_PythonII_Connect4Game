import Connect4Game as Game
import random


class RandomStrategy(Game.Connect4GameStrategy):
    """
    Inherits the Connect4GameStrategy so all functions are available.
    Adds a strategy function which selects a random choice column for players next move
    """
    def __init__(self, name="Daniel Batyrev"):
        self.name = name

    @classmethod
    def strategy(cls, game_safety_copy):
        """
        A copy of the current board is passed in to ensure no unwanted changes are made.
        A random choice column is picked from all valid moves
        """
        valid_moves = list()
        # loop through 7, as the game board has 7 columns
        for col in range(7):
            # validate whether a move in that column is valid
            if game_safety_copy.is_valid_move(col):
                # if so, append it to a list of valid moves
                valid_moves.append(col)
        # a random choice column is returned
        return random.choice(valid_moves)

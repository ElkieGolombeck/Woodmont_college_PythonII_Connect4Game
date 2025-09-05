"""
Connect4Game using AI Strategy to play against 2 competing players 10,000 games.

Score of each game is saved and displayed a bar chart with the players results.

Assumptions
- Connect4Game Board size: 6 rows × 7 columns.
- Players are 1 and 2
- Winner is set with the winning player id
- A move is valid if the column is within the 7 columns and the column has available spaces out of 6
"""

import Connect4Game
import DanielBatyrevAI as DanielAI
import DanielBatyrev2AI as Daniel2AI
import copy
import func_timeout
import matplotlib.pyplot as plt

# Competitors: index 0 is Player 1, index 1 is Player 2.
# Assumption: Connect4 has 7 columns, strategies must return an int 0 to 6.
competitor_list = [DanielAI.RandomStrategy(),Daniel2AI.RandomStrategy2()]

MAX_WAIT_TIME = 1
winners = list()
random_choice = DanielAI.RandomStrategy()

# Play 10,000 games.
for game_nr in range(10000):
    # Human-friendly game number: range starts at 0, so print, index + 1.
    print(game_nr + 1)
    # Track ties, set to false at the beginning of the game, will update to true if no available moves.
    tie = False
    # Start a new game. Assumption: game board is a 6 by 7 board, current player is 1, and no winner initially.
    game = Connect4Game.Connect4Game()
    # Play the game until a winner is set.
    while game.winner is None:
        # Copy game to ensure that the original game board is not modified in other functions.
        game_safety_copy = copy.deepcopy(game)
        # Player's Strategy can take a maximum of 1 second
        try:
            move = func_timeout.func_timeout(
                MAX_WAIT_TIME, competitor_list[game.current_player - 1].strategy, [game_safety_copy])
        except func_timeout.FunctionTimedOut:
            # Random choice strategy is played if the strategy function times out.
            print(f'time out limit exceeded: {competitor_list[game.current_player - 1].name} performs random move')
            move = random_choice.strategy(game_safety_copy)
        game.make_move(move)
        # Set the tie variable to true if there are no more available moves.
        if 0 == sum(map(game.is_valid_move, range(7))):
            tie = True
            break
    if tie:
        winners.append("tie")
    else:
        # Append winning player id to winners list.
        winners.append(competitor_list[game.current_player - 1].name)
    # Reverse the competing players strategy functions
    competitor_list.reverse()

dictionary = {}
# Create a dictionary with each player and it's total number of wins.
for item in winners:
    dictionary[item] = dictionary.get(item, 0) + 1

print(dictionary)

# Create a bar chart displaying the total wins for each player
plt.figure(figsize=(8, 6))
plt.bar(dictionary.keys(), dictionary.values(), color=['blue', 'green', 'red'])
plt.title("Connect 4 Results Analysis", fontsize=16)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Number of Wins", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
for i, value in enumerate(dictionary.values()):
    plt.text(i, value + 5, str(value), ha='center', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
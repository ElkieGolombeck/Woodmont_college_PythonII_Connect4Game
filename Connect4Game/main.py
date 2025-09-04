import Connect4Game
import DanielBatyrevAI as DanielAI
import DanielBatyrev2AI as Daniel2AI
import copy
import func_timeout
import matplotlib.pyplot as plt

competitor_list = [DanielAI.RandomStrategy(),Daniel2AI.RandomStrategy2()]

MAX_WAIT_TIME = 1
winners = list()
random_choice = DanielAI.RandomStrategy()

# 10,000 games will be played
for game_nr in range(10000):
    # The game starts by printing the number game being played
    # Looping through a range will start with 0. We are adding 1 to each game so the starting number is 1.
    print(game_nr + 1)
    # tie variable is declared and set to false at the beginning of the game
    tie = False
    # initialize a new object of the Connect4Game class
    game = Connect4Game.Connect4Game()
    # the game will continue the play until a winner is set
    while game.winner is None:
        # to ensure that the original game board is not touched until the move is played, we continue with a copy
        game_safety_copy = copy.deepcopy(game)
        # to ensure that the game won't time out, each move is maxed at 1 second
        # the strategy function is called to get the current player next move
        # Each competing player has a different strategy function that is called to determine it's next move
        try:
            move = func_timeout.func_timeout(
                MAX_WAIT_TIME, competitor_list[game.current_player - 1].strategy, [game_safety_copy])
        except func_timeout.FunctionTimedOut:
            # if the strategy function does time out, the random choice strategy is played.
            print(f'time out limit exceeded: {competitor_list[game.current_player - 1].name} performs random move')
            move = random_choice.strategy(game_safety_copy)
        # once the next move is decided on, make the move
        game.make_move(move)
        # if there are no more available moves, set the tie to true and break out of loop
        if 0 == sum(map(game.is_valid_move, range(7))):
            tie = True
            break
    if tie:
        # if there is a tie, append tie to the list of winners.
        winners.append("tie")
    else:
        # if we are out of the loop, and there's no tie, there is a winner. Append the winning player to the winners list
        winners.append(competitor_list[game.current_player - 1].name)
    # reverse the competing players strategy functions
    competitor_list.reverse()

dictionary = {}
# from the list of winners, store in dict, the number of wins for each winner
for item in winners:
    dictionary[item] = dictionary.get(item, 0) + 1

print(dictionary)

# create a plot chart
plt.figure(figsize=(8, 6))
# set bar chart values. The x axis is the dictionary keys (winner name) and the y axis is the number of wins.
plt.bar(dictionary.keys(), dictionary.values(), color=['blue', 'green', 'red'])
# set the title and labels
plt.title("Connect 4 Results Analysis", fontsize=16)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Number of Wins", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
for i, value in enumerate(dictionary.values()):
    plt.text(i, value + 5, str(value), ha='center', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
# display the chart
plt.show()
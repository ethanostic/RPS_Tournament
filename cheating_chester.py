# Cheats, but does not always win. Gets the opponent's play, but cannot guess random numbers.

from rock_paper_scissors import bot_1_name, bot_2_name, player_1_return_plays, player_1_answer, player_2_return_plays, player_2_answer

import importlib

def generate_choice(plays, answer):
    if bot_1_name == "cheating_chester":
        bot = importlib.import_module(bot_2_name)
        opponents_choice = bot.generate_choice(player_2_return_plays, player_2_answer)
    else:
        bot = importlib.import_module(bot_1_name)
        opponents_choice = bot.generate_choice(player_1_return_plays, player_1_answer)

    if opponents_choice == "ROCK":
        choice = "PAPER"
    elif opponents_choice == "PAPER":
        choice = "SCISSORS"
    elif opponents_choice == "SCISSORS":
        choice = "ROCK"

    return choice
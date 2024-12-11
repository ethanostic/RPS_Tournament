import random

# Returns the oponents previous play
def generate_choice(plays, answer):
    if plays:
        last_round = list(plays.values())[-1]
        friendly_bot_choice = last_round[1]
        choice = friendly_bot_choice
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    return choice

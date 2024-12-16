import random

# Returns the oponents previous play
def generate_choice(plays, answer):
    if plays:
        last_round = list(plays.values())[-1]
        opponents_choice = last_round[1]
        choice = opponents_choice
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    return choice

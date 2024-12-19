# Always plays the same play the whole round.

import random
def generate_choice(plays, answer):
    if plays:
        # Repeats first play for the whole round
        last_round = list(plays.values())[-1]
        choice = last_round[0]
    else:
        # Starts with random play
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    return choice
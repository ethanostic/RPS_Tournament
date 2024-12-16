# Finds the play played the most and exploits it. Recognized one play patterns only. Doe not account for the relationship between opponent and friendly plays.

import random
from collections import Counter

def generate_choice(plays, answer):

    # If there are no plays see else:
    if plays:

        # Get all opponent's plays and append to patterns
        patterns = []
        for i in range(len(plays)):
            last_round = list(plays.values())[i]
            opponents_previous_choice = last_round[1]
            patterns.append(opponents_previous_choice)

        # Get the play that is played the most
        play_counts = Counter(patterns)
        most_common_play, count = play_counts.most_common(1)[0]

        # Exploit the most played play
        if most_common_play == "ROCK":
            choice = "PAPER"
        elif most_common_play == "PAPER":
            choice = "SCISSORS"
        elif most_common_play == "SCISSORS":
            choice = "ROCK"

    # Return random otherwise
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    return choice

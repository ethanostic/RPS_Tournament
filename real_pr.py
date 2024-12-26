# Given plays from current_round and opponent's play from next current_round, finds pattern and exploits

import random
from collections import Counter

def generate_choice(plays, answer):

    # If there are no plays see else:
    if plays:

        # Get all opponent's plays and append to patterns
        patterns = []
        for i in range(len(plays)):

            # Get last round plays from opponent and this bot
            last_round = list(plays.values())[i - 1]
            previous_bot_choice = last_round[0]
            previous_opponents_choice = last_round[1]

            # Get current round opponent's play
            current_round = list(plays.values())[i]
            opponents_choice = current_round[1]


            # Make a pattern list and append it to patterns
            pattern = [previous_bot_choice, previous_opponents_choice, opponents_choice]
            patterns.append(pattern)

        # Get the play that is played the most
        play_counts = Counter(patterns)
        most_common_play = play_counts.most_common(1)[0]


        # Exploit the most played play
        if most_common_play[2] == "ROCK":
            choice = "PAPER"
        elif most_common_play[2] == "PAPER":
            choice = "SCISSORS"
        elif most_common_play[2] == "SCISSORS":
            choice = "ROCK"

    # Return random otherwise
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    return choice
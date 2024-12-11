# Choses the choice that beats the choice that has been played the least by the other player.

import random

def generate_choice(plays, answer):
    if plays:
        opponents_plays = [value[-1] for value in plays.values()]

        rocks = 0
        papers = 0
        scissors = 0

        for play in opponents_plays:
            if play == "ROCK":
                rocks += 1
            elif play == "PAPER":
                papers += 1
            elif play == "SCISSORS":
                scissors += 1

            lowest = min(rocks, papers, scissors)

            if lowest == rocks:
                choice = "PAPER"
            elif lowest == papers:
                choice = "SCISSORS"
            elif lowest == scissors:
                choice = "ROCK"
                
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])

    return choice
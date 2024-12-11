# Finds opponent's choice and plays against it. Wins only if it is called second.
# Doesn't work

import rock_paper_scissors

def generate_choice(plays, answer):

    opponents_choice = rock_paper_scissors.bot_1_choice

    if opponents_choice == "ROCK":
        choice = "PAPER"
    elif opponents_choice == "PAPER":
        choice = "SCISSORS"
    elif opponents_choice == "SCISSORS":
        choice = "ROCK"

    return choice
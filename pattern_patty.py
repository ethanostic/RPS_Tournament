# Repeats the rock, paper, scissors pattern over and over again
def generate_choice(plays, answer):
    if plays:
        last_round = list(plays.values())[-1]
        friendly_bot_choice = last_round[0]
        if friendly_bot_choice == "ROCK":
            choice = "PAPER"
        elif friendly_bot_choice == "PAPER":
            choice = "SCISSORS"
        elif friendly_bot_choice == "SCISSORS":
            choice = "ROCK"
        
    else:
        choice = "ROCK"

    return choice
import random
# If the bot wins, it choses the play after its previous play.
# If it loses, it choses the play before its previous play.
def generate_choice(plays, answer):
    if plays:
        last_round = list(plays.values())[-1]
        friendly_bot_choice = last_round[0]
        
        if answer == "WIN":
            if friendly_bot_choice == "ROCK":
                choice = "PAPER"
            elif friendly_bot_choice == "PAPER":
                choice = "SCISSORS"
            else:
                choice = "ROCK"
        else:
            if friendly_bot_choice == "ROCK":
                choice = "SCISSORS"
            elif friendly_bot_choice == "PAPER":
                choice = "ROCK"
            else:
                choice = "PAPER"
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    
    return choice

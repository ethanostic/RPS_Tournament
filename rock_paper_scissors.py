import importlib
import time

bot_1_name = input("Bot 1 file name (without .py): ")
bot_2_name = input("Bot 2 file name (without .py): ")

bot_1 = importlib.import_module(bot_1_name)
bot_2 = importlib.import_module(bot_2_name)

# Ensure 'generate_choice' is a function in both bot modules
if not callable(getattr(bot_1, 'generate_choice', None)) or not callable(getattr(bot_2, 'generate_choice', None)):
    print("Both bots must have a 'generate_choice' function!")
    exit()

player_1_return_plays = {}
player_2_return_plays = {}

player_1_score = 0
player_2_score = 0

def play(bot_1_name, bot_1_choice, bot_2_name, bot_2_choice):
    global player_1_score, player_2_score
    valid_choices = ["ROCK", "PAPER", "SCISSORS"]
    bot_1_choice = bot_1_choice.upper()
    bot_2_choice = bot_2_choice.upper()

    # Validate both players' choices
    print(f"Round {round_number}")
    if bot_1_choice not in valid_choices:
        print(f"Invalid input from {bot_1_name}. Choices must be ROCK, PAPER, or SCISSORS.")
    if bot_2_choice not in valid_choices:
        print(f"Invalid input from {bot_2_name}. Choices must be ROCK, PAPER, or SCISSORS.")
    
    if bot_1_choice == bot_2_choice:
        print(f"TIE!")
        print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")
        return False  # Return False to indicate no winner, round_number doesn't increment
    else:
        # Determine the winner
        if (bot_1_choice == "ROCK" and bot_2_choice == "SCISSORS") or \
           (bot_1_choice == "PAPER" and bot_2_choice == "ROCK") or \
           (bot_1_choice == "SCISSORS" and bot_2_choice == "PAPER"):
            # Bot 1 wins
            print(f"{bot_1_name} wins!")
            win = 1
            player_1_score += 1
            print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")
        else:
            # Bot 2 wins
            print(f"{bot_2_name} wins!")
            win = 2
            player_2_score += 1
            print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")

    return_information(bot_1_choice, bot_2_choice, round_number, win)
    return True  # Return True to indicate a winner, round_number will increment

def return_information(bot_1_choice, bot_2_choice, round_number, win):
    global player_1_answer, player_2_answer
    player_1_return_plays[round_number] = [bot_1_choice, bot_2_choice]
    player_2_return_plays[round_number] = [bot_2_choice, bot_1_choice]
    
    if win == 1:
        player_1_answer = "WIN"
    else:
        player_1_answer = "LOSE"
    if win == 2:
        player_2_answer = "WIN"
    else:
        player_2_answer = "LOSE"

player_1_answer = None
player_2_answer = None

round_number = 1
max_rounds = 100

while round_number <= max_rounds:
    bot_1_choice = bot_1.generate_choice(player_1_return_plays, player_1_answer)
    bot_2_choice = bot_2.generate_choice(player_2_return_plays, player_2_answer)

    # If the play function returns False, round_number will increment
    if play(bot_1_name, bot_1_choice, bot_2_name, bot_2_choice):
        round_number += 1  # Increment the round number only when there is a winner for that round
    time.sleep(0.1)
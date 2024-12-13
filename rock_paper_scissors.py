import importlib
import time

def main_rps(bot_1_name, bot_2_name, max_rounds):

    bot_1 = importlib.import_module(bot_1_name)
    bot_2 = importlib.import_module(bot_2_name)

    # Ensure 'generate_choice' is a function in both bot modules
    if not callable(getattr(bot_1, 'generate_choice', None)) or not callable(getattr(bot_2, 'generate_choice', None)):
        print("Both bots must have a 'generate_choice' function.")
        exit()

    global player_1_score, player_2_score, tied_rounds, tie_breaker_turn

    player_1_return_plays = {}
    player_2_return_plays = {}

    player_1_score = 0
    player_2_score = 0

    tied_rounds = 0

    player_1_answer = None
    player_2_answer = None

    round_number = 1

    tie_breaker_turn = 1
    def play(bot_1_name, bot_1_choice, bot_2_name, bot_2_choice):
        global player_1_score, player_2_score, tied_rounds, tie_breaker_turn
        valid_choices = ["ROCK", "PAPER", "SCISSORS"]
        bot_1_choice = bot_1_choice.upper()
        bot_2_choice = bot_2_choice.upper()

        print(f"Round {round_number}")

        # Validate both players' choices
        if bot_1_choice not in valid_choices:
            print(f"Invalid input from {bot_1_name}. Choices must be ROCK, PAPER, or SCISSORS.")
            exit()
        if bot_2_choice not in valid_choices:
            print(f"Invalid input from {bot_2_name}. Choices must be ROCK, PAPER, or SCISSORS.")
            exit()

        if bot_1_choice == bot_2_choice:
            tied_rounds += 1
            print("TIE!")
            print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")
            
            # End the ties after three consecutive attempts
            if tied_rounds == 3:
                tie_breaker_turn = 2 if tie_breaker_turn == 1 else 1 
                
                if tie_breaker_turn == 1:
                    print(f"TIE-BREAKER!\n{bot_1_name} wins!")
                    player_1_score += 1
                    win = 1
                else:
                    print(f"TIE-BREAKER!\n{bot_2_name} wins!")
                    player_2_score += 1
                    win = 2

                print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")
                tied_rounds = 0  # Reset tie counter
                return_information(bot_1_choice, bot_2_choice, round_number, win)
                return True

            return False  # No tie_breaker_turn, round_number doesn't increment

        else:

            # Determine the tie_breaker_turn
            if (bot_1_choice == "ROCK" and bot_2_choice == "SCISSORS") or \
            (bot_1_choice == "PAPER" and bot_2_choice == "ROCK") or \
            (bot_1_choice == "SCISSORS" and bot_2_choice == "PAPER"):
                print(f"{bot_1_name} wins!")
                player_1_score += 1
                win = 1
            else:
                print(f"{bot_2_name} wins!")
                player_2_score += 1
                win = 2

            print(f"{bot_1_name}: {player_1_score}\n{bot_2_name}: {player_2_score}\n")
            return_information(bot_1_choice, bot_2_choice, round_number, win)
            return True

    def return_information(bot_1_choice, bot_2_choice, round_number, win):
        global player_1_answer, player_2_answer
        player_1_return_plays[round_number] = [bot_1_choice, bot_2_choice]
        player_2_return_plays[round_number] = [bot_2_choice, bot_1_choice]
        
        if win == 1:
            player_1_answer = "WIN"
            player_2_answer = "LOSE"
        else:
            player_1_answer = "LOSE"
            player_2_answer = "WIN"

    while round_number <= max_rounds:
        bot_1_choice = bot_1.generate_choice(player_1_return_plays, player_1_answer)
        bot_2_choice = bot_2.generate_choice(player_2_return_plays, player_2_answer)

        # If the play function returns True, round_number will increment
        if play(bot_1_name, bot_1_choice, bot_2_name, bot_2_choice):
            round_number += 1

    return player_1_score, player_2_score
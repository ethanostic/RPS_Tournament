import random
from collections import defaultdict, Counter

def generate_choice(plays,answer):
    # If there are at least two rounds of plays
    if len(plays) >= 2:
        # Initialize pattern tracker
        patterns = defaultdict(list)

        # Populate patterns from plays history
        play_list = list(plays.values())
        for i in range(1, len(play_list)):  # Start from the second round
            previous_bot_choice, previous_opponent_choice = play_list[i - 1]
            current_opponent_choice = play_list[i][1]

            pattern_key = (previous_bot_choice, previous_opponent_choice)
            patterns[pattern_key].append(current_opponent_choice)

        # Get last round's plays
        last_round_bot, last_round_opponent = play_list[-1]

        # Determine the matching pattern
        pattern_key = (last_round_bot, last_round_opponent)
        if pattern_key in patterns:
            # Find the most common opponent play
            most_common = Counter(patterns[pattern_key]).most_common(1)
            if most_common:
                predicted_opponent_move = most_common[0][0]

                # Exploit the opponent's predicted move
                if predicted_opponent_move == "ROCK":
                    return "PAPER"
                elif predicted_opponent_move == "PAPER":
                    return "SCISSORS"
                elif predicted_opponent_move == "SCISSORS":
                    return "ROCK"

        # Fallback to random if no pattern is found
        return random.choice(["ROCK", "PAPER", "SCISSORS"])

    # Random choice for the first round or insufficient data
    return random.choice(["ROCK", "PAPER", "SCISSORS"])

# ChatGPT made this bot. I asked him for pattern recognition

import random

def generate_choice(plays, answer):
    if plays:  
        # Store the history of the opponent's moves
        history = [move[1] for move in list(plays.values())]  # List of opponent moves
        
        # Check patterns of varying lengths (2, 3, and 4 moves)
        max_pattern_length = 4
        patterns = {}

        # Loop through history and track patterns of different lengths
        for length in range(2, max_pattern_length + 1):
            for i in range(len(history) - length):
                pattern = tuple(history[i:i + length])  # Get the pattern of 'length' moves
                if pattern not in patterns:
                    patterns[pattern] = 0
                patterns[pattern] += 1
        
        # Identify the most frequent pattern
        most_frequent_pattern = max(patterns, key=patterns.get, default=None)
        
        # Predict the next move based on the most frequent pattern
        if most_frequent_pattern:
            last_move_of_pattern = most_frequent_pattern[-1]  # The last move in the pattern
            
            if last_move_of_pattern == 'ROCK':
                choice = 'PAPER'
            elif last_move_of_pattern == 'PAPER':
                choice = 'SCISSORS'
            else:
                choice = 'ROCK'
        else:
            # If no clear pattern is detected, choose randomly or default
            choice = 'ROCK'
    else:
        choice = random.choice(["ROCK", "PAPER", "SCISSORS"])

    return choice

import os
from rock_paper_scissors import main_rps

# List all the files in the working directory
current_directory = os.getcwd()
file_names = []
for entry in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, entry)):
        file_names.append(entry)

# Remove specific files from the list
file_names.remove("create_tournament_rounds.py")
file_names.remove("rock_paper_scissors.py")
file_names.remove("template.py")
file_names.remove("README.md")
file_names.remove("testfile.py")

# Remove .py extension from filenames
file_names_without_py = []
for file in file_names:
    if file.endswith(".py"):
        file = file.removesuffix(".py")
    file_names_without_py.append(file)

file_names = file_names_without_py

# Generate all possible pairs ensureing that the key:value pairs are in alphabetical order
file_pairs_made = []

for filekey in file_names:
    for filevalue in file_names:
        if filekey > filevalue:
            file_pairs_made.append({filevalue: filekey})
        else:
            file_pairs_made.append({filekey: filevalue})

# Remove duplicate pairs
unique_pairs = set()
final_pairs = []

for pair in file_pairs_made:
    pair_tuple = tuple(pair.items())
    if pair_tuple not in unique_pairs:
        final_pairs.append(pair)
        unique_pairs.add(pair_tuple)

final_pairs_sorted = sorted(final_pairs, key=lambda x: list(x.keys())[0])

# Loop through each pair and run the rps with the filenames
scores = {}
for pair in final_pairs_sorted:
    for file1, file2 in pair.items():
        player_1_score, player_2_score = main_rps(file1, file2, 100)
        scores[file1, file2] = [player_1_score, player_2_score]

# Initialize a dictionary to store total scores and count of games for each player
total_scores = {}
game_counts = {}

# Calculate the total scores and the number of games for each player
for (file1, file2), score in scores.items():
    # Update total score and game count for player 1 (file1)
    if file1 not in total_scores:
        total_scores[file1] = 0
        game_counts[file1] = 0
    total_scores[file1] += score[0]
    game_counts[file1] += 1
    
    # Update total score and game count for player 2 (file2)
    if file2 not in total_scores:
        total_scores[file2] = 0
        game_counts[file2] = 0
    total_scores[file2] += score[1]
    game_counts[file2] += 1

# Calculate and store the average score for each player
average_scores = {}
for player in total_scores:
    average_scores[player] = round(total_scores[player] / game_counts[player], 1)

# Sort the players by average score in descending order
sorted_average_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

# Print the sorted average scores
print("Average scores (sorted from highest to lowest):")
for player, avg_score in sorted_average_scores:
    print(f"{player}: {avg_score}")
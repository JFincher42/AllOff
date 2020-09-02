import json


with open("data_file.json", "r") as read_file:
    puzzles = json.load(read_file)

print(puzzles)

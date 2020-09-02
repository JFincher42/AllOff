import json

puzzles = dict()
puzzle = dict()

puzzle["solution"] = [(0, 0), (2, 0), (4, 0), (0, 4), (2, 4), (4, 4)]
puzzle["level"] = 1
puzzles[0] = puzzle

puzzle = dict()
puzzle["solution"] = [(0, 0), (2, 0), (4, 0), (0, 4), (2, 4), (4, 4), (2, 2)]
puzzle["level"] = 1
puzzles[1] = puzzle


with open("data_file.json", "w") as write_file:
    json.dump(puzzles, write_file)


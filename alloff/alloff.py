"""
AllOff - A Python version of the handheld game `Lights Out`

"""

import PySimpleGUI as sg
import ui
import json


def load_puzzles(puzzle_file):
    # Open the file with pointers to our puzzle files
    with open("puzzle-files.json", "r") as puzzle_filenames:
        puzzle_files = json.load(puzzle_filenames)

    # Get the location of our puzzle files
    with open(puzzle_files[puzzle_file], "r") as puzzle_input:
        puzzle_datafiles = json.load(puzzle_input)

    # Open and read each file into our puzzle dictionary
    # TODO: Make this an object instead?


def setup_game_board(puzzle_file, level, puzzle):
    # Init all the lights off
    board = [[False for col in range(5)] for row in range(5)]

    # TODO: Get the puzzle requested
    return board


def game_over(board):
    for col in range(5):
        for row in range(5):
            if board[row][col]:
                return False

    return True


def update_board(board, row, col):

    board[col][row] = not board[col][row]
    if col > 0:
        board[col - 1][row] = not board[col - 1][row]
    if col < 4:
        board[col + 1][row] = not board[col + 1][row]
    if row > 0:
        board[col][row - 1] = not board[col][row - 1]
    if row < 4:
        board[col][row + 1] = not board[col][row + 1]


def update_display(board, window):
    # Update the display
    for col in range(5):
        for row in range(5):
            if board[col][row]:
                window[f"-BUTTON-{row}-{col}-"].update(
                    image_filename=ui.button_lit_image_path
                )
            else:
                window[f"-BUTTON-{row}-{col}-"].update(
                    image_filename=ui.button_grey_image_path
                )


if __name__ == "__main__":
    window = sg.Window("All Off!", ui.layout, finalize=True)

    # Read the local configuration file
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Load all current puzzles
    puzzles = load_puzzles(config["current_puzzle_file"])

    # Setup game board
    board = setup_game_board(
        config["current_level"], config["current_puzzle"],
    )

    # Show the initial setup
    update_display(board, window)

    while not game_over(board):

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            running = False

        elif event == "-RESET-":
            print("RESET")
            board = setup_game_board()
            window["-RESET-"].update(disabled=True)

        elif "-BUTTON-" in event:
            # Button press
            row, col = int(event[8]), int(event[10])
            update_board(board, row, col)
            window["-RESET-"].update(disabled=False)
            print(f"[{row},{col}]")

        update_display(board, window)

    input()

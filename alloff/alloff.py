"""
AllOff - A Python version of the handheld game `Lights Out`

"""

import PySimpleGUI as sg
import ui


def setup_game_board():
    # Init everything off
    board = [[False for col in range(5)] for row in range(5)]

    # Get the new setup
    update_board(board, 0, 0)
    update_board(board, 0, 2)
    update_board(board, 0, 4)
    update_board(board, 4, 0)
    update_board(board, 4, 2)
    update_board(board, 4, 4)

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

    # Setup game board
    board = setup_game_board()

    # Show the initial setup
    update_display(board, window)

    while not game_over(board):

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            running = False

        elif "-BUTTON-" in event:
            # Button press
            row, col = int(event[8]), int(event[10])
            update_board(board, row, col)

        update_display(board, window)

    input()

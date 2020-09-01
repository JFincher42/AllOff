"""
AllOff - A Python version of the handheld game `Lights Out`

"""

import PySimpleGUI as sg
import ui

window = sg.Window("All Off!", ui.layout)
running = True

# Game board
board = [[False for col in range(5)] for row in range(5)]
while running:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        running = False

    elif "-BUTTON-" in event:
        # Button press
        row, col = int(event[8]), int(event[10])
        board[col][row] = not board[col][row]

        if board[col][row]:
            window[event].update(image_filename=ui.button_lit_image_path)
        else:
            window[event].update(image_filename=ui.button_grey_image_path)

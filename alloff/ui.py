"""
UI for AllOff
"""

import PySimpleGUI as sg
from pathlib import Path

# Where are our images?
current_folder = Path("alloff")
button_grey_image_path = current_folder / "images" / "button_gray.png"
button_lit_image_path = current_folder / "images" / "button_lit.png"

# The button layout

buttons = [
    [
        sg.Button(
            image_filename=button_grey_image_path, key=f"-BUTTON-{row}-{col}-"
        )
        for col in range(5)
    ]
    for row in range(5)
]


# Score, level, reset row
bottom_row = [
    sg.Text("Level: ", size=(10, 1), key="-LEVEL-"),
    sg.ProgressBar(
        max_value=6, orientation="horizontal", size=(10, 16), key="-PROGRESS-"
    ),
    sg.Button(button_text="Reset", disabled=True, key="-RESET-"),
]

# Master Layout
layout = buttons + [bottom_row]

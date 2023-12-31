
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documents\Code\Python\Consulting Math\build\assets\frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#171C29")


canvas = Canvas(
    window,
    bg = "#171C29",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    107.0,
    407.0,
    anchor="nw",
    text="TOTAL MARKET SHARE",
    fill="#FFFFFF",
    font=("Gotham Bold", 65 * -1)
)

canvas.create_text(
    107.0,
    501.0,
    anchor="nw",
    text="How many questions would you like to answer?",
    fill="#FFFFFF",
    font=("Gotham Book", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    274.5,
    587.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=107.0,
    y=557.0,
    width=335.0,
    height=58.0
)
window.resizable(False, False)
window.mainloop()

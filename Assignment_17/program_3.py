# Create a frame using tkinter with any label text and two buttons.One to exit and other to
# change the label to some other text.

from tkinter import *

import sys

root = Tk()

frame = Frame()

frame.pack()

lbl = Label(frame, text = 'Test')

lbl.pack(side=TOP)

def display():
    global lbl

    lbl.config(text = "Text Change")

button_1 = Button(frame, text="Change Text", command=display)

button_1.pack(side=LEFT, expand=YES, fill=Y)

button_2 = Button(frame, text="Quit", command=sys.exit)

button_2.pack(side = RIGHT, expand=YES, fill=Y)

button_2.mainloop()

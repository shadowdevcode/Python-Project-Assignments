#  Write a python program to in the same interface as above and create a action when the button is click it will
#  display some text.

from tkinter import *

def functodisplay():

    print("Message Displayed")

widget = Button(None, text="CLICK TO DISPLAY", command = functodisplay)

widget.pack(side = BOTTOM, expand = YES, fill=Y)

widget.mainloop()

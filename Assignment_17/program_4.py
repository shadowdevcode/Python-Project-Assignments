# Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *

root = Tk()
root.title("Display Name App")

label_display = Label(root, text = 'Welcome to display name application').pack()

label_display_name = Label(root, text = 'Enter your name: ').pack()

name = StringVar()

entry_box = Entry(root, textvariable = name).pack()

def do_it():
    print("Hello ", str(name.get()))

work = Button(root, text = 'Display', command = do_it).pack()

root.mainloop()
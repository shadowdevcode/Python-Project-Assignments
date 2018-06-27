#  Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):


        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="Exit", command=root.destroy)

        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("Welcome to hello world!")

root = tk.Tk()

app = Application(master=root)

app.mainloop()

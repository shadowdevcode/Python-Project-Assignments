# Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and
# create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *

root = Frame()      # This will create a parent containment
root.pack()         # Packing the content in the interface

dictionary_list = {"Name-1": 1110, "Name-2": 2120, "Name-3": 3242, "Name-4": 5783}  # Dictionary created

label1 = Label(root, text="Name")
label1.pack(side = "top")
label2 = Label(root, text="Mobile Number")
label2.pack(side = "top")


def scroll_list(event):             # Performing some action so function declared.

    label_act = list_box.get(ACTIVE)
    print(label_act)
    name = dictionary_list.get(label_act)
    mobile_number = dictionary_list.get(label_act)

    global widget1, widget2

    label1.config(text = name)

    label2.config(text = mobile_number)


list_box = Listbox(root)            # ListBox is created

scroll_bar1 = Scrollbar(root)
scroll_bar1.config(command = list_box.yview)
list_box.config(yscrollcommand = scroll_bar1.set)
scroll_bar1.pack(side = RIGHT, fill = Y)
list_box.pack(side = LEFT, expand = YES, fill = BOTH)


list_box.bind('<Double-1>', scroll_list)

for i, j in dictionary_list.items():
     list_box.insert('end', i, j)       # Displayed both Name and mobile number

root.mainloop()


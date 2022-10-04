import tkinter
from tkinter.constants import W
from tkinter.ttk import Radiobutton, Label, Button


def select():
    monitor.config(text="{}".format(option.get()))


def reset():
    option.set(None)
    monitor.config(text="")


root = tkinter.Tk()
label_title = tkinter.Label(root, text="Select your favorite Mexican Food!!!")
label_title.pack()
option = tkinter.StringVar()
option.set(None)

Radiobutton(root, text="Taco", variable=option,
            value='Taco', command=select).pack(anchor=W)
Radiobutton(root, text="Burrito", variable=option,
            value='Burrito', command=select).pack(anchor=W)
Radiobutton(root, text="Quesadilla", variable=option,
            value='Quesadilla', command=select).pack(anchor=W)
Radiobutton(root, text="Enchilada", variable=option,
            value='Enchilada', command=select).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reset", command=reset).pack()

root.mainloop()

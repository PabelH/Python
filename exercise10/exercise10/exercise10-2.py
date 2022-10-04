import tkinter
from tkinter import ttk, Tk

window: Tk = tkinter.Tk()

label_title = tkinter.Label(window, text="What countries have you visited?")
label_title.pack()

c1 = tkinter.StringVar()
c2 = tkinter.StringVar()
c3 = tkinter.StringVar()
c4 = tkinter.StringVar()


ttk.Checkbutton(window, text="Argentina", variable=c1, width=20).pack()
ttk.Checkbutton(window, text="Spain", variable=c2, width=20).pack()
ttk.Checkbutton(window, text="Mexico", variable=c3, width=20).pack()
ttk.Checkbutton(window, text="USA", variable=c4, width=20).pack()

window.mainloop()

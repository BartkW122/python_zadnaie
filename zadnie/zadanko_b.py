from funkcje import *
from tkinter import *


root = Tk()
root.title("GRA")
root.geometry("300x300")

menubar = Menu(root)
graj = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Graj", menu=graj)
graj.add_command(label="Nowa gra",command=lambda: nowa_gra(root))
graj.add_command(label="Zapisz grę")
graj.add_command(label="Wczytaj grę")

# Use lambda to pass root as an argument to opcje2
menubar.add_command(label="Opcje", command=lambda: opcje2(root))

root.config(menu=menubar)
root.mainloop()

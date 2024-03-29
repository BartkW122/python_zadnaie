from funkcje import *
from tkinter import *

global w
global canvas
global w2
global event


root = Tk()
root.title("GRA")
root.geometry("300x300")

canvas = Canvas(root, width=300, height=300)
canvas.pack()
w2=IntVar(master=root)
menubar = Menu(root)
graj = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Graj", menu=graj)
graj.add_command(label="Nowa gra", command=lambda: nowa_gra(root,canvas))
graj.add_command(label="Zapisz grę",command=lambda: pole_na_zapisywanie_pliku(root))
graj.add_command(label="Wczytaj grę",command=lambda: pole_na_pliki(root))
graj.add_command(label="Wyjdź",command=root.destroy)


menubar.add_command(label="Opcje", command=lambda: opcje2(root,canvas))

root.config(menu=menubar)
root.mainloop()
from tkinter import *
from math import *


def opcje2(root):
    root2 = Toplevel(root)
    root2.title("Opcje")
    root2.geometry("300x300")
    kolor = Label(root2, text="kolory:")
    kolor.pack()

    w = IntVar(master=root2)
    kolor1 = Label(root2, text="zielony")
    kolor1.pack()
    kolor1 = Radiobutton(root2, variable=w, value=1)
    kolor1.pack()

    kolor2 = Label(root2, text="niebieski")
    kolor2.pack()
    kolor2 = Radiobutton(root2, variable=w, value=2)
    kolor2.pack()

    kolor3 = Label(root2, text="czerwony")
    kolor3.pack()
    kolor3 = Radiobutton(root2, variable=w, value=3)
    kolor3.pack()
    w2 = IntVar(master=root2)
    tryb = Label(root2, text="tryb gry:")
    tryb.pack()
    tryb1 = Label(root2, text="człowiek")
    tryb1.pack()
    tryb1 = Radiobutton(root2, variable=w2, value=4)
    tryb1.pack()

    tryb2 = Label(root2, text="Bot")
    tryb2.pack()
    tryb2 = Radiobutton(root2, variable=w2, value=5)
    tryb2.pack()

    btn = Button(root2, text="zapisz", command=lambda: zamiana_koloru(w))
    btn.pack()

    root2.mainloop()


def zamiana_koloru(w):
    w_get = w.get()
    if w_get == 1:
        canvas.configure(bg="green")
    if w_get == 2:
        canvas.configure(bg="blue")
    if w_get == 3:
        canvas.configure(bg="red")


def nowa_gra(root):
    global canvas

    canvas = Canvas(root, width=300, height=300)
    # canvas = Canvas(root, width=300, height=300)
    # Linie pionowe
    canvas.create_line(100, 0, 100, 300, width=2)
    canvas.create_line(200, 0, 200, 300, width=2)

    # Linie poziome
    canvas.create_line(0, 100, 300, 100, width=2)
    canvas.create_line(0, 200, 300, 200, width=2)

    canvas.bind("<Button-1>", dane)
    canvas.pack()


def dane(event):
    x = floor(event.x / 100)
    y = floor(event.y / 100)
    print(x, y)
    wynik = (100 * x) + 50
    print("srodek", wynik)
    canvas.create_line(wynik,100, 100, 100, fill="black")
    Canvas()

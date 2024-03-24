from tkinter import *
from math import *
import os
z = "x"
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
    global z
    global wynik
    global wynik2
    global  tab_dane
    tab_dane=[]
    x = floor(event.x / 100)
    y = floor(event.y / 100)
    #print(x, y)
    wynik = (100 * x) + 50
    wynik2 = (100 * y) + 50
    #print("srodek", wynik)
    #print("srodek2", wynik2)

    z = znak(wynik, wynik2, z)
    #print("Aktualny symbol:", z)
    #for i in range(len(tab_dane)):
    tab_dane.append(wynik)
    tab_dane.append(wynik2)
    print(tab_dane)


def znak(wynik, wynik2, znak):
    global canvas
    global x_z
    global o_z
    if znak == "x":
        x_z=canvas.create_line(wynik + 20, wynik2 - 20, wynik - 20, wynik2 + 20, fill="black", width=10),canvas.create_line(wynik - 20, wynik2 - 20, wynik + 20, wynik2 + 20, fill="black", width=10)
        return "o"
    else:
        o_z=canvas.create_oval(wynik - 20, wynik2 - 20, wynik + 20, wynik2 + 20, outline="black", width=10)
        return "x"

def zapisz_gre():
    global wynik
    global wynik2
    global z

    file = open('zapisana_gra.txt', 'a')
    file.write(str(wynik))
    file.write("\n")
    file.write(str(wynik2))
    file.write("\n")
    file.write(z)
    file.write("\n")
    file.close()


def wczytaj_gre():
    tab=[]
    f = open('zapisana_gra.txt', "r")
    for line in f:
        tab.append(line)
    print(tab)
    f.close()
    os.remove('zapisana_gra.txt')





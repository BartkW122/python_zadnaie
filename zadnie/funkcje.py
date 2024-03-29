from tkinter import *
from tkinter import messagebox
from math import *
import os
import json
import random

z = "x"
tab_dane2 = []
tab_dane = []
x_z = 0
o_z = 0
plansza = [['' for _ in range(3)] for _ in range(3)]


def opcje2(root, canvas):
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

    w2 = IntVar(master=root2)  # Define w2 here
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

    btn = Button(root2, text="zapisz", command=lambda: zapis(w,w2,canvas))
    btn.pack()


    root2.mainloop()



def wybor_gracz(w2):
    w2_get = w2.get()
    if w2_get == 5:
        messagebox.showinfo('grasz', 'grasz z Botem')
        return "bot"
    if w2_get == 4:
        messagebox.showinfo('grasz', 'grasz z człowiekiem')
        return "czlowiek"


def zamiana_koloru(w, canvas):
    w_get = w.get()
    if w_get == 1:
        canvas.configure(bg="green")
    if w_get == 2:
        canvas.configure(bg="blue")
    if w_get == 3:
        canvas.configure(bg="red")


def zapis(w, w2, canvas):
    zamiana_koloru(w, canvas)
    wybor_gracz(w2)


def komputer():
    global plansza
    global z
    global x
    global y
    dostepne_ruchy = [(x, y) for x in range(3) for y in range(3) if plansza[x][y] == '']
    print(random.choice(dostepne_ruchy))
    plansza[x][y] = "o"
    print(plansza)


def nowa_gra(root, canvas):
    global plansza
    global z
    global tab_dane
    global tab_dane2
    w2=IntVar(master=root)
    tab_dane = []
    tab_dane2 = []
    plansza = [['' for _ in range(3)] for _ in range(3)]
    canvas.delete("all")
    for linia in range(1, 3):
        canvas.create_line(linia * 100, 0, linia * 100, 300, fill="black", width=5)
        canvas.create_line(0, linia * 100, 300, linia * 100, fill="black", width=5)
    z = "x"
    canvas.bind("<Button-1>", lambda event, w2=w2: dane(event, canvas, w2))


def dane(event, canvas, w2):
    global z
    global wynik
    global wynik2
    global x
    global y

    x = floor(event.x / 100)
    y = floor(event.y / 100)
    wynik = (100 * x) + 50
    wynik2 = (100 * y) + 50

    z = ruch(wynik, wynik2, z, canvas, w2)


def sprawdz_czy_puste():
    global plansza
    global x
    global y
    global z
    if plansza[x][y] == '':
        plansza[x][y] = z
        return True
    else:
        return False


def wygrana():
    global plansza
    for i in range(3):
        if plansza[i][0] == plansza[i][1] == plansza[i][2] != '':
            return True
        if plansza[0][i] == plansza[1][i] == plansza[2][i] != '':
            return True
    if plansza[0][0] == plansza[1][1] == plansza[2][2] != '':
        return True
    if plansza[0][2] == plansza[1][1] == plansza[2][0] != '':
        return True
    return False


def remis():
    global plansza
    for row in plansza:
        for znak2 in row:
            if znak2 == '':
                return False
    return True


def zapisywanie_danych():
    global wynik
    global wynik2
    global tab_dane
    global tab_dane2
    tab_dane = [wynik, wynik2]

    tab_dane2.append(tab_dane)


def ruch(wynik, wynik2, znak, canvas, w2):
    global tab_dane2
    global x
    global y
    #wybor_gracz(w2)
    if wybor_gracz(w2)=="bot":
        komputer()

    if sprawdz_czy_puste():
        zapisywanie_danych()
        plansza[x][y] = znak
        if wygrana():
            messagebox.showinfo('Wygrana', f'Gracz {znak} wygrywa!')
        if remis():
            messagebox.showinfo('remis', 'remis')
        if znak == "x":
            canvas.create_line(wynik + 20, wynik2 - 20, wynik - 20, wynik2 + 20, fill="black", width=10)
            canvas.create_line(wynik - 20, wynik2 - 20, wynik + 20, wynik2 + 20, fill="black", width=10)
            return "o"
        else:
            canvas.create_oval(wynik - 20, wynik2 - 20, wynik + 20, wynik2 + 20, outline="black", width=10)
            return "x"
    else:
        messagebox.showinfo('miejsce', 'miejsce jest zajete')
        return znak






def pole_na_zapisywanie_pliku(root):
    global name
    root3 = Toplevel(root)
    root3.title("PLIKI_ZAPIS")
    root3.geometry("300x200")
    n=Label(root3,text="podaj nazwe pliku:")
    n.pack()
    name=Entry(root3)
    name.pack()
    btn=Button(root3,text="zapisz",command=zapisz_gre)
    btn.pack()
    btn2 = Button(root3, text="wyjdź", command=root3.destroy)
    btn2.pack()
    root3.mainloop()
def pole_na_pliki(root):
    global name
    root4 = Toplevel(root)
    root4.title("PLIKI(WYBÓR)")
    root4.geometry("300x200")
    n = Label(root4, text="podaj nazwe pliku:")
    n.pack()
    name = Entry(root4)
    name.pack()
    btn = Button(root4, text="wczytaj",command=wczytaj_gre)
    btn.pack()
    btn2 = Button(root4, text="wyjdź", command=root4.destroy)
    btn2.pack()
    root4.mainloop()
def zapisz_gre():
    global tab_dane2
    global name
    with open(f'{name.get()}', 'a') as file:
        json.dump(tab_dane2, file)
def wczytaj_gre():
    global name
    #print(name.get())
    with open(f'{name.get()}', 'r') as file:
        data = json.load(file)
        print(data)


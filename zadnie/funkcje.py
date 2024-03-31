from tkinter import *
from tkinter import messagebox
from math import *
import os
import json
import random

z = "x"
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

    btn = Button(root2, text="zapisz", command=lambda: zapis(w,w2,canvas))
    btn.pack()


    root2.mainloop()
    root2.destroy()



def wybor_gracz(w2,canvas,w):
    global z

    w2_get = w2.get()
    if w2_get == 4:
        messagebox.showinfo('grasz', 'grasz z człowiekiem')
        return "czlowiek"
    if w2_get == 5:
        messagebox.showinfo('grasz', 'grasz z Botem')
        komputer(canvas,w,w2)
        return "bot"






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
    wybor_gracz(w2,canvas,w)




def nowa_gra(root, canvas):
    global plansza
    global z
    w2 = IntVar(master=root)
    w=IntVar(master=root)
    plansza = [['' for _ in range(3)] for _ in range(3)]
    canvas.delete("all")
    for linia in range(1, 3):
        canvas.create_line(linia * 100, 0, linia * 100, 300, fill="black", width=5)
        canvas.create_line(0, linia * 100, 300, linia * 100, fill="black", width=5)
    z = "x"
    canvas.bind("<Button-1>", lambda event: dane(event, canvas, w2,w))


def dane(event, canvas, w2,w):
    global z
    global wynik
    global wynik2
    global x
    global y

    x = floor(event.x / 100)
    y = floor(event.y / 100)
    wynik = (100 * x) + 50
    wynik2 = (100 * y) + 50
    if wybor_gracz(w2,canvas,w)=='bot':
        if komputer(canvas,w2,w):
            if z=='o':
                return 'x'

    z = ruch(wynik, wynik2, z, canvas, w2)




def komputer(canvas,w,w2):
    global plansza
    global z
    x=0
    y=0

    dostepne_ruchy = [(x, y) for x in range(3) for y in range(3) if plansza[x][y] == '']
    if dostepne_ruchy:
        x,y=random.choice(dostepne_ruchy)
        print(x,y)
        plansza[x][y] = "o"
        print(plansza)

        canvas.delete("all")
        for linia_2 in range(1, 3):
            canvas.create_line(linia_2 * 100, 0, linia_2 * 100, 300, fill="black", width=5)
            canvas.create_line(0, linia_2 * 100, 300, linia_2 * 100, fill="black", width=5)
        if plansza[x][y] == "x":
            wynik_2 = y * 100 + 50
            wynik2_2 = x * 100 + 50
            canvas.create_line(wynik2_2 - 20, wynik_2 - 20, wynik2_2 + 20, wynik_2 + 20, fill="black", width=10)
            canvas.create_line(wynik2_2 - 20, wynik_2 + 20, wynik2_2 + 20, wynik_2 - 20, fill="black", width=10)
        if plansza[x][y] == "o":
            wynik_2 = y * 100 + 50
            wynik2_2 = x * 100 + 50
            canvas.create_oval(wynik2_2 - 20, wynik_2 - 20, wynik2_2 + 20, wynik_2 + 20, outline="black", width=10)


        canvas.bind("<Button-1>", lambda event: dane(event, canvas, w2,w))


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





def ruch(wynik, wynik2, znak, canvas, w2):
    global tab_dane2
    global tab_wynik
    global x
    global y


    if sprawdz_czy_puste()==True:

        if wygrana():
            canvas.unbind("<Button-1>")
            messagebox.showinfo('Wygrana', f'Gracz {znak} wygrywa!')


        if remis():
            canvas.unbind("<Button-1>")
            messagebox.showinfo('remis', 'remis')

        plansza[x][y] = znak
        print("ruch", plansza)

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

    root3.mainloop()
    root3.destroy()
def pole_na_pliki(root,canvas):
    global name
    global w3
    w2=IntVar(master=root)
    w=IntVar(master=root)
    pliki=[]
    root4 = Toplevel(root)
    root4.title("PLIKI(WYBÓR)")
    root4.geometry("300x300")
    w3 = StringVar(master=root4)
    folder_path = r"C:\Users\Ja\OneDrive\Pulpit\prywatny git\zadnie"#zmiana ścieżki na ścieżkę gdzie znajduje się folder
    rozszerzenie='.txt'
    contents = os.listdir(folder_path)
    p = Label(root4, text='dostępne pliki:')
    p.pack()
    for item in contents:
        if item.endswith(rozszerzenie):

            t=Label(root4, text=f'{item} ')
            t.pack()
            p2 = Radiobutton(root4,variable=w3,value=f'{item} ')
            p2.pack()


    btn = Button(root4, text="wczytaj",command=lambda: wczytaj_gre(canvas, w2,w))
    btn.pack()

    root4.mainloop()
    root4.destroy()

def zapisz_gre():
    global plansza
    global name
    messagebox.showinfo('zapis','Gra została zapisana')
    print(plansza)
    with open(f'{name.get()}.txt', 'a') as file:
        json.dump(plansza, file)


def wczytaj_gre(canvas, w2,w):
    global plansza
    global w3
    messagebox.showinfo('wczytywanie', 'gra została wczytana')
    with open(w3.get(), 'r') as file:
        data = json.load(file)
        plansza = data
    print(plansza)
    canvas.delete("all")
    for linia_2 in range(1, 3):
        canvas.create_line(linia_2 * 100, 0, linia_2 * 100, 300, fill="black", width=5)
        canvas.create_line(0, linia_2 * 100, 300, linia_2 * 100, fill="black", width=5)

    for x_2 in range(len(plansza)):
        for y_2 in range(len(plansza[x_2])):
            if plansza[x_2][y_2] == "x":
                wynik_2 = y_2 * 100 + 50
                wynik2_2= x_2 * 100 + 50
                canvas.create_line(wynik2_2 - 20, wynik_2 - 20, wynik2_2 + 20, wynik_2 + 20, fill="black", width=10)
                canvas.create_line(wynik2_2 - 20, wynik_2 + 20, wynik2_2 + 20, wynik_2 - 20, fill="black", width=10)
            elif plansza[x_2][y_2] == "o":
                wynik_2 = y_2 * 100 + 50
                wynik2_2 = x_2 * 100 + 50
                canvas.create_oval(wynik2_2 - 20, wynik_2 - 20, wynik2_2 + 20, wynik_2 + 20, outline="black", width=10)

    canvas.bind("<Button-1>", lambda event: dane(event, canvas, w2,w))


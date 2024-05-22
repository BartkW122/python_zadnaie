import time
from tkinter import *
from tkinter import messagebox

start_czasu = 0
<<<<<<< HEAD
czasy=[]
=======
>>>>>>> b6f7c4618e2b5e1ffe05beccc540db01fa4375c2
gracze_czasy = []
en = []  # lista graczy

def gracz():
    ilosc_g = int(ilosc_graczy.get())
    if ilosc_g>=2:
        for i in range(1, ilosc_g + 1):
            Label(okno, text=f"Podaj znak dla gracza {i}:").pack()
            e = Entry(okno)
            e.pack()
            en.append(e)
    else:
        messagebox.showinfo(message="musi być conajmniej 2 graczy by ropocząć gre!")

def zapisz_przyciski():
    for i in range(len(en)):
        messagebox.showinfo(message=f"Gracz {i+1} ma przycisk {en[i].get()}")
        okno.bind(en[i].get(), stop)
    ilosc_graczy.config(state="disabled")
    for entry in en:
        entry.config(state="disabled")

def zmien():
    ilosc_graczy.config(state="normal")
    for entry in en:
        entry.config(state="normal")

def start():
    global start_czasu
    messagebox.showinfo(message="po kliknięciu przyciksu z rozpocznie się  doliczanie czasu!")
    gracze_czasy.clear()
    for i in range(len(en)):
        okno.bind(en[i].get(), stop)
    start_czasu = time.time()
    czas()

def stop(event):
    global start_czasu
    if start_czasu != 0:
        zapisany_czas = round(time.time() - start_czasu, 2)
        for i in range(len(en)):
            if event.char == en[i].get():
<<<<<<< HEAD
                gracze_czasy.append((en[i].get(), round(10-zapisany_czas,2)))
                czasy.append((en[i].get(), round(zapisany_czas,2)))
=======
                gracze_czasy.append((en[i].get(), round(15-zapisany_czas,2)))
>>>>>>> b6f7c4618e2b5e1ffe05beccc540db01fa4375c2
                print(f"Gracz {i+1} z przyciskiem {en[i].get()} ma {zapisany_czas} sekund")
                okno.unbind(en[i].get())

def czas():
    global start_czasu
    if start_czasu != 0:
        zapisany_czas = round(time.time() - start_czasu, 2)
        print(zapisany_czas)
        if zapisany_czas < 15:
            okno.after(100, czas)
        else:
            messagebox.showinfo(message="Minęło 15 sekund!")
            wygrana()

def pokaz_zapisaany_czas():
    gracze_czasy.sort(reverse=True)
    print(gracze_czasy)
    wygrana()

def wygrana():
    gracze_czasy.sort(reverse=True)
    zwyciezca=gracze_czasy[0]
<<<<<<< HEAD
    messagebox.showinfo(message=f"gracz z przyciskiem ({zwyciezca[0]}) wygrał z czasem  {round(10-zwyciezca[1],2)}")

#def pokaz_czasy_graczy():
    #for i in range(len(czasy)):
    #messagebox.showinfo(message=)
=======
    messagebox.showinfo(message=f"gracz z przyciskiem ({zwyciezca[0]}) wygrał z czasem  {round(15-zwyciezca[1],2)}")

>>>>>>> b6f7c4618e2b5e1ffe05beccc540db01fa4375c2
okno = Tk()
okno.title("Gra w 10 sekund")
okno.geometry("800x800")

ilosc_graczy = Label(okno, text="Podaj ilość graczy:")
ilosc_graczy.pack()
ilosc_graczy = Entry(okno)
ilosc_graczy.pack()

stworz_graczy = Button(okno, text="Stwórz graczy", command=gracz)
stworz_graczy.pack()

start_button = Button(okno, text="Start", command=start)
start_button.pack()

<<<<<<< HEAD
#pokaz_czas = Button(okno, text="Pokaż czasy graczy", command=pokaz_czasy_graczy())
=======
#pokaz_czas = Button(okno, text="Pokaż czas", command=pokaz_zapisaany_czas)
>>>>>>> b6f7c4618e2b5e1ffe05beccc540db01fa4375c2
#pokaz_czas.pack()

zapisz = Button(okno, text="Zapisz przyciski", command=zapisz_przyciski)
zapisz.pack()

zmien = Button(okno, text="Zmień znak/ilosc graczy", command=zmien)
zmien.pack()

okno.mainloop()

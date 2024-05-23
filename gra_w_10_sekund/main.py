import time
from tkinter import *
from tkinter import messagebox

start_czasu = 0
czasy=[]
gracze_czasy = []
en = []  # lista graczy
znaki=[]

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
    znaki.clear()
    for i in range(len(en)):
        znaki.append(en[i].get())
    for i in range(len(en)):
        if len(znaki) == len(set(znaki)):
            messagebox.showinfo(message=f"Gracz {i+1} ma przycisk {en[i].get()}")
            okno.bind(en[i].get(), stop)
            ilosc_graczy.config(state="disabled")
            for entry in en:
                entry.config(state="disabled")
            start_button.config(state="normal")
        else:
            messagebox.showerror(message="przyciski nie mogą się powtażać")
def zmien():
    start_button.config(state="disabled")
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
                gracze_czasy.append((f"gracz {i + 1}", round(10 - zapisany_czas, 2)))
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

def wygrana():
    gracze_czasy.sort(key=lambda x:x[1])
    print(gracze_czasy)
    zwyciezca=gracze_czasy[0]
    messagebox.showinfo(message=f"{zwyciezca[0]}  wygrał z czasem  {round(10-zwyciezca[1],2)}")

def pokaz_czasy_graczy():
    for i in range(len(gracze_czasy)):
        messagebox.showinfo(message=f"{gracze_czasy[i]}")
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
start_button.config(state="disabled")
pokaz_czas = Button(okno, text="Pokaż czasy graczy", command=pokaz_czasy_graczy)
pokaz_czas.pack()

zapisz = Button(okno, text="Zapisz przyciski", command=zapisz_przyciski)
zapisz.pack()

zmien = Button(okno, text="Zmień znak/ilosc graczy", command=zmien)
zmien.pack()

okno.mainloop()

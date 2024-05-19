import time
from tkinter import *
from tkinter import messagebox

start_czasu = 0
stop_czasu = 0
tab_czas = []
en = []  # tabela graczy

def gracz():
    ilosc_g = ilosc_graczy.get()
    ilosc_g_2 = int(ilosc_g)
    for i in range(1, ilosc_g_2 + 1):
        Label(okno, text=f"Podaj znak dla gracza {i}:").pack()
        e = Entry(okno)
        e.pack()
        en.append(e)

def przycisk(event):
    for i in range(len(en)):
        messagebox.showinfo(message=f"Gracz {i+1} ma przycisk {en[i].get()}")
        okno.bind(en[i].get(), stop)
        en[i].config(state="disabled")
        ilosc_graczy.config(state="disabled")

def zmien():
    for i in range(len(en)):
        en[i].config(state="normal")
        ilosc_graczy.config(state="normal")

def start():
    global start_czasu
    tab_czas.clear()
    tab_czas.clear()
    for i in range(len(en)):
        okno.bind(en[i].get(), stop)
    start_czasu = time.time()
    czas()

def stop(event):
    global start_czasu, stop_czasu
    if start_czasu != 0:
        stop_czasu = time.time()
        zapisany_czas = stop_czasu - start_czasu
        print("Minęło:", round(zapisany_czas, 2), "sekund")
        for i in range(len(en)):
            if event.char == en[i].get():
                tab_czas.append((en[i].get(), round(zapisany_czas, 2)))
                print(f"Kliknięto gracz {i+1}")
                okno.unbind(en[i].get())

def czas():
    global start_czasu
    if start_czasu != 0:
        zapisany_czas = time.time() - start_czasu
        print("Pozostało:", round(zapisany_czas, 2), "sekund")
        if zapisany_czas < 15:
            okno.after(100, czas)
        else:
            messagebox.showinfo(message="Minęło 15 sekund!")

def pokaz_zapisaany_czas():
    print(tab_czas)
    wygrana()

def wygrana():
        #tab_czas.sort()
        #zwyciezca = tab_czas[0]
        #messagebox.showinfo(message=f"Zwycięzca to gracz z przyciskiem '{zwyciezca[0]}' z czasem {zwyciezca[1]} sekund")
        #print(f"Zwycięzca to gracz z przyciskiem '{zwyciezca[0]}' z czasem {zwyciezca[1]} sekund")
        #do zrobienia

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

pokaz_czas = Button(okno, text="Pokaż czas", command=pokaz_zapisaany_czas)
pokaz_czas.pack()

zapisz = Button(okno, text="Zapisz znak", command=lambda: przycisk(Event))
zapisz.pack()

zmien = Button(okno, text="Zmień znak/czas", command=zmien)
zmien.pack()

okno.mainloop()

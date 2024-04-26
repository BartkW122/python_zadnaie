import time
from tkinter import *

start_czasu = 0
stop_czasu = 0
tab_czas=[]

def klik(event):
    print("kliknięto")
def przycisk(event):
    gracz_1=g1.get()
    print(f"gracz 1 ma przycisk {gracz_1}")
    okno.bind(f"{gracz_1}", klik)
    g1.config(state= "disabled")
def zmien():
    g1.config(state="enable")
def start():
    global start_czasu
    start_czasu = time.time()
    czas()

def stop():
    global start_czasu, stop_czasu
    if start_czasu != 0:
        stop_czasu = time.time()
        zapisany_czas = stop_czasu - start_czasu
        print("Minęło:", round(zapisany_czas, 2), "sekund")
        tab_czas.append(round(zapisany_czas, 2))
        start_czasu = 0

def czas():
    global start_czasu
    if start_czasu != 0:
        zapisany_czas = time.time() - start_czasu
        print("Pozostało:", round(zapisany_czas, 2), "sekund")
        if zapisany_czas < 10:
            okno.after(100, czas)
        else:
            print("Minęło  10 sekund!")
def pokaz_zapisaany_czas():
    print("zapisany czas "+str(tab_czas))

okno = Tk()
okno.title("Gra w 10 sekund")
okno.geometry("300x300")
gracz1=Label(okno,text="podaj znak dla gracza 1:")
gracz1.pack()
g1=Entry(okno)
g1.pack()
zapisz=Button(okno,text="zapisz",command=lambda:przycisk(Event))
zapisz.pack()
#okno.bind("a", przycisk)
start_button = Button(okno, text="Start", command=start)
start_button.pack()

stop_button = Button(okno, text="Stop", command=stop)
stop_button.pack()

pokaz_czas = Button(okno, text="pokaz", command=pokaz_zapisaany_czas)
pokaz_czas.pack()

okno.mainloop()

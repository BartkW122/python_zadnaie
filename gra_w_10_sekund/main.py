import time
from tkinter import *

start_czasu = 0
stop_czasu = 0
czas_g1=0
czas_g2=0

def klik(event):
    print("kliknięto")
def przycisk(event):
    global gracz_1,gracz_2
    gracz_1=g1.get()
    gracz_2=g2.get()
    print(f"gracz 1 ma przycisk {gracz_1}")
    print(f"gracz 2 ma przycisk {gracz_2}")
    okno.bind(f"{gracz_1}", stop)
    okno.bind(f"{gracz_2}", stop)
    g1.config(state= "disabled")
    g2.config(state= "disabled")
def zmien():
    g1.config(state="normal")
    g2.config(state="normal")
def start():
    global start_czasu
    okno.bind(f"{gracz_1}", stop)
    okno.bind(f"{gracz_2}", stop)
    start_czasu = time.time()
    czas()

def stop(event):
    global start_czasu, stop_czasu,gracz_1,gracz_2,czas_g1,czas_g2
    if start_czasu != 0:
        stop_czasu = time.time()
        zapisany_czas = stop_czasu - start_czasu
        print("Minęło:", round(zapisany_czas, 2), "sekund")
        if event.char== gracz_1:
            czas_g1=round(zapisany_czas, 2)
            print("klikniento g1")
            okno.unbind(f"{gracz_1}")
        if event.char== gracz_2:
            czas_g2=round(zapisany_czas, 2)
            print("klikniento g2")
            g2.config(state="disabled")
            okno.unbind(f"{gracz_2}")
        
       

def czas():
    global start_czasu,czas_g1,czas_g2
    if start_czasu != 0:
        zapisany_czas = time.time() - start_czasu
        print("Pozostało:", round(zapisany_czas, 2), "sekund")
        if zapisany_czas < 15:
            okno.after(100, czas)
        else:
            print("Minęło  15 sekund!")
def pokaz_zapisaany_czas():
    print("zapisany czas_g1 "+str(czas_g1))
    print("zapisany czas_g2 "+str(czas_g2))
    wygrana()
    
def wygrana():
    if czas_g1>czas_g2:
        print("gracz 1 wygrał")
    if czas_g2>czas_g1:
        print("gracz 2 wygrał")
okno = Tk()
okno.title("Gra w 10 sekund")
okno.geometry("300x300")
gracz1=Label(okno,text="podaj znak dla gracza 1:")
gracz1.pack()
g1=Entry(okno)
g1.pack()

gracz2=Label(okno,text="podaj znak dla gracza 2:")
gracz2.pack()
g2=Entry(okno)
g2.pack()
zapisz=Button(okno,text="zapisz",command=lambda:przycisk(Event))
zapisz.pack()


zmien=Button(okno,text="zmien",command=zmien)
zmien.pack()

start_button = Button(okno, text="Start", command=start)
start_button.pack()

#stop_button = Button(okno, text="Stop", command=lambda:stop(Event))
#stop_button.pack()

pokaz_czas = Button(okno, text="pokaz", command=pokaz_zapisaany_czas)
pokaz_czas.pack()


okno.mainloop()

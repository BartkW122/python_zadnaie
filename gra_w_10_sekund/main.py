import time
from tkinter import *

start_czasu = 0
stop_czasu = 0

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
        start_czasu = 0

def czas():
    global start_czasu
    if start_czasu != 0:
        zapisany_czas = time.time() - start_czasu
        print("Pozostało:", round(zapisany_czas, 2), "sekund")
        if zapisany_czas < 10:
            okno.after(100, czas)
        else:
            print("Minęło dokładnie 10 sekund!")

okno = Tk()
okno.title("Gra w 10 sekund")
okno.geometry("300x300")

start_button = Button(okno, text="Start", command=start)
start_button.pack()

stop_button = Button(okno, text="Stop", command=stop)
stop_button.pack()

okno.mainloop()

#!/usr/bin python3

import tkinter as tk
from tkinter import messagebox
from random import randint

WINDOW_SIZE = 500
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
MIN_DISTANCE = 100

def movebtn(event=None):
    curr_x = x.get()
    curr_y = y.get()
    
    while True:
        new_x = randint(0, WINDOW_SIZE - BUTTON_WIDTH)
        new_y = randint(0, WINDOW_SIZE - BUTTON_HEIGHT)

        distance = ((new_x - x.get()) ** 2 + (new_y - y.get()) ** 2) ** 0.5
        
        if distance > MIN_DISTANCE:
            break

    btn.place(x = new_x, y = new_y)

window = tk.Tk()
window.geometry('500x500')
window.title('Move your button')

x = tk.IntVar()
y = tk.IntVar()
x.set(10)
y.set(10)

btn = tk.Button(window, text='Kliknij')
btn.place(x=x.get(), y=y.get())
btn.bind('<Enter>', movebtn)

window.mainloop()

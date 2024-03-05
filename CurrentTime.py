from tkinter import *
import time 

def clock_func():
    updated_clock = time.strftime('%H : %M : %S')
    visual_clock.config(text=updated_clock)
    window.after(1000, clock_func)


window = Tk()
window.geometry('200x200')
clock = time.strftime('%H : %M : %S')
visual_clock = Label(window, text =clock)
visual_clock.pack()

clock_func()


window.mainloop()
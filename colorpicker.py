from tkinter import *
from tkinter import colorchooser


window = Tk()
window.geometry('400x400')

def color_picker():
    color_code, color_name = colorchooser.askcolor(title='choose a color')
    label.config(text=f'Selected Color: {color_name}', background=f'{color_name}')



label = Label(window, text= f'Selected Color: None', font=('Arial', 15, 'normal'))
label.pack()

button = Button(window, text='Choose color', command=color_picker)
button.place(x=150, y=40)



window.mainloop()
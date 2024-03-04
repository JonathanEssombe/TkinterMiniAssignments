from tkinter import *

window = Tk()
window_icon = PhotoImage(file='dogman-lilpetey-grime-and-punishment.gif')
window.iconphoto(True, window_icon)
window.geometry('400x400')
window.title('Excersie 10')

window_label = Label(window, text='Custom Label',
                     font=('Ariel', 20, 'bold'),
                     foreground='green',
                     background='black')
window_label.pack()
window_button = Button(window,
                       text='press me',
                       foreground='blue',
                       font=('Helvetica', 20, 'Bold'),
                       background='gray')
window_button



window.mainloop()
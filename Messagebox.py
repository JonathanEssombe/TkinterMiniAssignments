from tkinter import *
from tkinter import messagebox

root = Tk()
root_icon = PhotoImage(file='dogman-lilpetey-grime-and-punishment.gif')
root.iconphoto(True, root_icon)
root.title('Learn to Code at Codemy.com')
root.geometry('400x400')

# showinfo, showwaring, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showinfo('This is my Popup!', 'Hello World!')
    Label(root, text=response).pack()
    # if response == "yes":
    #     Label(root, text='You Clicked Yes!').pack()
    # else:
    #     Label(root, text='You Clicked No!').pack()
root_button = Button(root, text='Popup', command=popup)
root_button.pack()

root.mainloop()
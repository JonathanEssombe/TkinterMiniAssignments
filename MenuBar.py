from tkinter import *

window = Tk()
window.title('Spyder (Python 3.6)')
#window_icon = PhotoImage(file='dogman-lilpetey-grime-and-punishment.gif')
# window.iconphoto(True, window_icon)
# window.geometry('400x400')



window_menu = Menu(window)
window.config(menu=window_menu)

file_menu = Menu(window_menu, tearoff=False)
window_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)

edit_menu = Menu(window_menu, tearoff=False)
window_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')

help_menu = Menu(window_menu, tearoff=False)
window_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About Spyder')


window.mainloop()
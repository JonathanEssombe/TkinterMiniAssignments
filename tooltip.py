from tkinter import *

window = Tk()
window.geometry('400x400')

def open_tool_tip(event):
    tool_tip.geometry(f'+{event.x + 25}+{event.y + 25}') 
    tool_tip.wm_overrideredirect(True) 
    tool_tip_label.pack()
    tool_tip.deiconify()

def close_tool_tip(event):
    tool_tip.withdraw()



my_button = Button(window, text='press me')
my_button.bind('<Enter>', open_tool_tip)
my_button.bind('<Leave>', close_tool_tip)
my_button.pack()

my_label = Label(window, text='this is a label')
my_label.bind('<Enter>', open_tool_tip)
my_label.bind('<Leave>', close_tool_tip)
my_label.pack()

tool_tip = Toplevel()
tool_tip.title('This is a tool tip')
tool_tip_label = Label(tool_tip, text='This is a tool tip', bg='light yellow')
tool_tip.withdraw()



window.mainloop()
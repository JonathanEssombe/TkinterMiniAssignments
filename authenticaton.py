from tkinter import *
from tkinter import messagebox



def login_function():

    global username_created
    username_input = username_entry.get()
    password_input = password_entry.get()
    if username_input == 'myname' and password_input == 'password':
        messagebox.showinfo(title='Login successful', message='Welcome Admin')
    else:
        messagebox.showerror(title='Login Unsuccessful', message='invalid username or password')



def create_function():
    username_created = username_entry.get()
    password_created = password_entry.get()


window = Tk()
window.title('Login')

username_label = Label(window, text='Username:')
username_label.grid(row=0, column=1)

username_entry = Entry(window)
username_entry.grid(row=1, column=0, columnspan=3)


password_label = Label(window, text='Password:')
password_label.grid(row=2, column=1)

password_entry = Entry(window, show='*')
password_entry.grid(row=3, column=0, columnspan=3)

login_button = Button(window, text='Login', command=login_function)
login_button.grid(row=4, column=1)




window.mainloop()



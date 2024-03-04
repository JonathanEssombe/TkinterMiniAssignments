from tkinter import *

windows = Tk()
windows.geometry('500x200')
windows.title('Temperature converter')

# celsius to fahrenheit
def fahrenheit_convertor():
    celsius_input = celsius_entry.get()
    try:
        celsius_entered = float(celsius_input)
    except ValueError:
        display_screen.config(text='Error')
    else:
        fahrenheit_expression = (9 / 5) * (celsius_entered) + 32
        fahrenheit_output = f'{celsius_entered:.2f}°C= {fahrenheit_expression:.2f}℉'
        display_screen.config(text=fahrenheit_output)


# fahrenheit to celsius
def celsius_convertor():
    farenheit_input = farenheit_entry.get()
    try:
        farenheit_entered = float(farenheit_input)
    except ValueError:
        display_screen.config(text='Error')
    else:
        celsius_expression = (5 / 9) * (farenheit_entered - 32)
        celsius_output = f'{farenheit_entered:.2f}℉ = {celsius_expression:.2f}°C'
        display_screen.config(text=celsius_output)


# first grid row

celsius_label = Label(windows, text='input celsius:')
celsius_label.grid(row=0, column=0, sticky=E)

celsius_entry = Entry(windows)
celsius_entry.grid(row=0, column=1)

fahrenheit_button = Button(windows,
                           text='convert to fahrenheit',
                           command=fahrenheit_convertor)

fahrenheit_button.grid(row=0, column=2)

# 2nd grid row

farenheit_label = Label(windows, text='input farenheit:')
farenheit_label.grid(row=1, column=0)

farenheit_entry = Entry(windows)
farenheit_entry.grid(row=1, column=1)

celsius_button = Button(windows,
                           text='convert to degrees',
                           command=celsius_convertor)

celsius_button.grid(row=1, column=2, ipadx=6)


# display screen 

display_screen = Label(windows, text='', borderwidth=True)
display_screen.grid(row=2, column=1)

windows.mainloop()

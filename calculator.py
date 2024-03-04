from tkinter import *

calculator = Tk()
calculator.title('calculator')
calculator.geometry('130x215')
expression = ''



calculator_screen = Label(calculator, text='0', font=25, relief='raised')
calculator_screen.grid(column=0, row=0, columnspan=3, ipady=5, sticky=SE)

def exceed_character_func():
    global expression
    if len(expression) >= 11:
        expression = expression[:-1]
        calculator_screen.config(text=expression)


def equals_func():
    global expression
    try:
        evaluate = eval(expression)
        calculator_screen.config(text=evaluate)
        expression = ''
    except Exception:
        calculator_screen.config(text='Error')
        expression = ''


def add_func():
    exceed_character_func()
    global expression
    expression += '+'
    calculator_screen.config(text=expression)


def subtract_func():
    exceed_character_func()
    global expression
    expression += '-'
    calculator_screen.config(text=expression)

def multiply_func():
    exceed_character_func()
    global expression
    expression += '*'
    calculator_screen.config(text=expression)

def divide_func():
    exceed_character_func()
    global expression
    expression += '/'
    calculator_screen.config(text=expression)

def clear_func():
    global expression
    expression = ''
    calculator_screen.config(text='0')

def delete_func():
    global expression
    expression = expression[:-1]
    if expression == '':
        calculator_screen.config(text='0')
    else:
        calculator_screen.config(text=expression)

def dot_func():
    exceed_character_func()
    global expression
    expression += '.'
    calculator_screen.config(text=expression)


def zero_func():
    exceed_character_func()
    global expression
    expression += '0'
    calculator_screen.config(text=expression)

def one_func():
    exceed_character_func()
    global expression
    expression += '1'
    calculator_screen.config(text=expression)

def two_func():
    exceed_character_func()
    global expression
    expression += '2'
    calculator_screen.config(text=expression)

def three_func():
    exceed_character_func()
    global expression
    expression += '3'
    calculator_screen.config(text=expression)

def four_func():
    exceed_character_func()
    global expression
    expression += '4'
    calculator_screen.config(text=expression)

def five_func():
    exceed_character_func()
    global expression
    expression += '5'
    calculator_screen.config(text=expression)

def six_func():
    exceed_character_func()
    global expression
    expression += '6'
    calculator_screen.config(text=expression)

def seven_func():
    exceed_character_func()
    global expression
    expression += '7'
    calculator_screen.config(text=expression)

def eight_func():
    exceed_character_func()
    global expression
    expression += '8'
    calculator_screen.config(text=expression)

def nine_func():
    exceed_character_func()
    global expression
    expression += '9'
    calculator_screen.config(text=expression)



add_button = Button(calculator, text='+', command=add_func)
add_button.grid(row=1, column=0)

subtract_button = Button(calculator, text='-', command=subtract_func)
subtract_button.grid(row=1, column=1, ipadx=3)

multiply_button = Button(calculator, text='*', command=multiply_func)
multiply_button.grid(row=2, column=1, ipadx=1)

divide_button =  Button(calculator, text='/', command=divide_func)
divide_button.grid(row=1, column=2)

clear_button = Button(calculator, text='C', command=clear_func)
clear_button.grid(row=2, column=2)

equals_button = Button(calculator, text='=', command=equals_func)
equals_button.grid(row=6, column=2)

delete_button = Button(calculator, text='del', command=delete_func)
delete_button.grid(row=2, column=0)



dot_button = Button(calculator, text='.', command=dot_func)
dot_button.grid(row=6, column=0)

zero_button = Button(calculator, text='0', command=zero_func)
zero_button.grid(row=6, column=1)

one_button = Button(calculator, text='1', command=one_func)
one_button.grid(row=5, column=0)

two_button = Button(calculator, text='2', command=two_func)
two_button.grid(row=5, column=1)

three_button = Button(calculator, text='3', command=three_func)
three_button.grid(row=5, column=2)

four_button = Button(calculator, text='4', command=four_func)
four_button.grid(row=4, column=0)

five_button = Button(calculator, text='5', command=five_func)
five_button.grid(row=4, column=1)

six_button = Button(calculator, text='6', command=six_func)
six_button.grid(row=4, column=2)

seven_button = Button(calculator, text='7', command=seven_func)
seven_button.grid(row=3, column=0)

eight_button = Button(calculator, text='8', command=eight_func)
eight_button.grid(row=3, column=1)

nine_button = Button(calculator, text='9', command=nine_func)
nine_button.grid(row=3, column=2)



calculator.mainloop()
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x400')
window.title('Digital Timer Application')
# initialize the remaining time
remaining_time = 0

# timers state, it is either active or inactive
timer_mode = True


def cancel_timer():
    global timer_mode
    global remaining_time

    timer_mode = False

    remaining_time = 0
    minutes_timer.config(text=f'00:')
    seconds_timer.config(text='00')

    minutes_entry.delete(0, 3)
    seconds_entry.delete(0, 3)

    minutes_entry.insert(0, '0')
    seconds_entry.insert(0, '0')



# stop the timer
def stop_timer():
    global timer_mode
    timer_mode = False

    # disable stop button only
    stop_button.config(state='disabled')
    start_button.config(state='active')
    resume_button.config(state='active')
    cancel_button.config(state='active')


# resume the timer
def resume_timer():

    global timer_mode
    timer_mode = True
    update_timer()

# update the timer
def update_timer():

    global remaining_time
    global timer_mode
    # disable the start button, enable the stop button, disable the resume button, enable cancel button
    start_button.config(state='disabled')
    stop_button.config(state='active')
    resume_button.config(state='disabled')
    cancel_button.config(state='active')

    # Maximum entry input of 99 minutes
    if 6000 > remaining_time >= 0 and timer_mode:
        current_minutes, current_seconds = divmod(remaining_time, 60)

        # update timer on screen
        minutes_timer.config(text=f'{current_minutes:02d}:')
        seconds_timer.config(text=f'{current_seconds:02d}')

        remaining_time -= 1
        window.after(1000, update_timer)

    else:
        timer_mode = False
        stop_timer()

# start the timer
def create_timer():

    global remaining_time
    global timer_mode



    try:
        minutes_entered = int(minutes_entry.get())
        seconds_entered = int(seconds_entry.get())
    except ValueError:
        messagebox.showwarning('Invalid input', 'please enter a valid integer')
    else:

        # Total time in seconds
        remaining_time = 60 * minutes_entered + seconds_entered

        # Maximum entry input of 99 minutes
        if 6000 > remaining_time >= 0:
            timer_mode = True
            update_timer()
        else:
            if remaining_time >= 6000 :
                messagebox.showwarning('Max digit limit',
                                       'please a maximum of 2 digits in each entry')
                timer_mode = False
                stop_timer()
            else:
                timer_mode = False
                stop_timer()




minutes_label = Label(window, text='Minutes:', padx=5)
minutes_label.grid(row=0, column=0)

minutes_entry = Entry(window)
minutes_entry.insert(0, '0')
minutes_entry.grid(row=0, column=1)

seconds_label = Label(window, text='Seconds:', padx=5)
seconds_label.grid(row=1, column=0)

seconds_entry = Entry(window)
seconds_entry.insert(0, '0')
seconds_entry.grid(row=1, column=1)

minutes_timer = Label(window, text='00:', font=('Ariel', 50, 'normal'))
minutes_timer.grid(row=2, column=0, sticky=E)

seconds_timer = Label(window, text='00', font=('Ariel', 50, 'normal'))
seconds_timer.grid(row=2, column=1, sticky=W)

start_button = Button(window, text='start', font=(50), command=create_timer)
start_button.grid(row=3, column=0, sticky=SW, ipadx=13)

stop_button = Button(window, text='stop', font=(50), command=stop_timer, state='disabled')
stop_button.grid(row=3, column=1, sticky=SW, ipadx=13)

resume_button = Button(window, text='resume', font=(50), command=resume_timer, state='disabled')
resume_button.grid(row=4, column=1, sticky=SW)

cancel_button = Button(window, text='cancel', font=50, command=cancel_timer, state='disabled' )
cancel_button.grid(row=4, column=0, sticky=SW, ipadx=6)

window.mainloop()

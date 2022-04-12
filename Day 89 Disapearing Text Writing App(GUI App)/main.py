from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Dangerous typing app")
root.minsize(500, 600)
root.config(padx=20, pady=20)

main_frame = Frame(root)
text_frame = Frame(root)


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def text_area():
    text_frame.pack()
    main_frame.forget()


def delete_text():
    text.delete("1.0", END)


def get_time():
    once = True
    global seconds
    while once == True:
        choice = combo.get()
        seconds = int(choice) * 60
        once = False


def check_if_done():
    global time_left
    if time == float(seconds):
        text.config(state=DISABLED)
        return timer_label.set("Congrats you've done it!")
    elif text_lenght == len(text.get("1.0", END)) and len(text.get("1.0", END)) > 2:
        b = time_left + 1
        time_left = b
        print(time_left)
        if time_left == 5:
            text.delete("1.0", END)
            text.config(state=DISABLED)
            return timer_label.set("You lost")
    else:
        time_left = 0
    update_label()


time_left = 0


def update_label():
    global text_lenght
    global seconds
    global time_left
    global time
    # get the time from the string
    time = float(timer_label.get()[:-1])
    print(time)
    # increment the time and put it back in timer_label
    timer_label.set(str(time+1) + 's')

    text_lenght = len(text.get("1.0", END))
    # calling this function again 1000ms later, which will call this again 1000ms later
    text_frame.after(1000, check_if_done)
    button.configure(state=DISABLED)

options = [
    "1",
    "5",
    "10",
    "15",
    "20",
    "30",
]

label = Label(main_frame, text="Welcome the most Dangerous Typing Game!", font=("Helvetica", 18))
label.grid(row=0, column=0, columnspan=2)

label_explain = Label(main_frame, text="Don't stop typing or your progress will be lost FOREVER!", font=("Helvetica", 18))
label_explain.config(pady=10)
label_explain.grid(row=1, column=0, columnspan=2)

label_time = Label(main_frame, text="Please select the minutes:", font=("Helvetica", 18))
label_time.config(pady=10)
label_time.grid(row=2, column=0)

combo = ttk.Combobox(main_frame, value=options, font=("Helvetica", 18))
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(row=2, column=1)

button = Button(main_frame, text="Start writing now", font=["Helvetica", 18], command=combine_funcs(get_time, text_area, update_label))
button.grid(row=3, column=0, columnspan=2)

text = Text(text_frame, font=("Helvetica", 16))
text.pack(expand=True, fill=BOTH)


main_frame.pack(fill=BOTH, expand=1)

timer_frame = Frame(text_frame).pack()
timer_label = StringVar(text_frame)
timer_label.set("0.0s")

Label(timer_frame, textvariable=timer_label, font=['Consolas', 20, 'bold'], pady=5).pack()

root.mainloop()
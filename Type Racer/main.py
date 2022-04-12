from tkinter import *
import random

FONT_NAME = "Courier"
reps = 0

words = ["abridge", "lung", "concentrate", "licence", "object", "grounds", "coal", "bean", "explosion", "piano",
         "abandon", "strange", "painter", "describe", "magazine", "experiment", "insistence", "retired", "modernize",
         "woman", "oh", "pool", "ambiguity", "dirty", "product", "desire", "poem", "ethics", "rotation", "grounds",
         "fold", "association", "bar", "holiday", "quest", "return", "tycoon", "conservative", "basic", "sink",
         "safety", "thirsty", "guilt"]

def delete_word(event):
    global list_words
    global player_word
    global combined_char
    player_word = player_text.get("1.0", 'end-1c')
    text_word = text.get("1.0", 'end-1c')
    new_words = text_word
    list = new_words.split(" ", len(words))
    list_words = [n + " " for n in list]
    if player_word == list_words[0]:
        char = len(list_words[0])
        text.config(state=NORMAL)
        for n in range(char):
            text.delete("1.0")
        text.config(state=DISABLED)
        player_text.delete('1.0', 'end')
        combined_char = sum(len(i) for i in list_words)
        print(combined_char)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def start_char():
    global combined_char_one
    text_start = text.get("1.0", 'end-1c')
    new_words_start = text_start
    list_start = new_words_start.split(" ", len(words))
    list_words_start = [n + " " for n in list_start]
    combined_char_one = sum(len(i) for i in list_words_start)
    print(combined_char_one)


def update_label():
    # get the time from the string
    time = float(timer_label.get()[:-1])

    # increment the time and put it back in timer_label
    timer_label.set(str(time+1) + 's')

    if time == 60.0:
        player_text.config(state=DISABLED)
        wpm = ((combined_char_one - combined_char)/5)/1

        return timer_label.set(f"WPM: {wpm}")

    # calling this function again 1000ms later, which will call this again 1000ms later
    window.after(1000, update_label)
    button.configure(state=DISABLED)


window = Tk()

window.bind("<space>", delete_word)
window.title("Type Racer")
window.config(bg="#398AB9", padx=20, pady=20)
window.minsize(370, 370)

text = Text(window, height=5, width=20, font=(FONT_NAME, 20, "bold"))
text.insert(END, random.sample(words, len(words)))
text.config(state=DISABLED)
text.grid(row=0, column=0)

player_text = Text(height=1, width=20, font=(FONT_NAME, 15, "bold"))
player_text.grid(row=1, column=0, pady=20)

timer_frame = Frame(window).grid(row=2,column=0)
timer_label = StringVar()
timer_label.set("0.0s")

Label(timer_frame, textvariable=timer_label, bg="#398AB9", font=['Consolas', 20, 'bold'], pady=25).grid(row=2, column=0)

button = Button(text="Start", bg="#398AB9", command=combine_funcs(start_char, update_label))
button.grid(row=3, column=0)

window.mainloop()
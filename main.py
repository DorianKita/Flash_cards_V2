import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
words = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient='records')
else:
    words = df.to_dict(orient='records')


random_word = {}



def next_card():
    global random_word,flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words)
    canvas.itemconfig(front_card, image=card_front_image)
    canvas.itemconfig(word, text=random_word["French"], fill='black')
    canvas.itemconfig(title, text="French", fill='black')

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(front_card, image=card_back_image)
    canvas.itemconfig(word, text=random_word["English"], fill='white')
    canvas.itemconfig(title, text="English", fill='white')


def remove_card():
    words.remove(random_word)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
front_card = canvas.create_image(400,263, image= card_front_image)
title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

check_button_photo = PhotoImage(file="images/right.png")
cross_button_photo = PhotoImage(file="images/wrong.png")

right_button = Button(image=check_button_photo, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)
wrong_button = Button(image=cross_button_photo, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
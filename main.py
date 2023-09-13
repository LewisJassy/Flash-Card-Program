import pandas
import pandas as pd
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word = original_data.to_dict(orient="records")
else:
    word = data.to_dict(orient="records")


def button_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="red")
    canvas.itemconfig(card_word, text=current_card["English"], fill="orange")
    canvas.itemconfig(canvas_image, image=old_image)


def is_known():
    word.remove(current_card)
    new_data = pandas.DataFrame(word)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    button_next_word()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
old_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
canvas.itemconfig(canvas_image, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="French", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


check_button = PhotoImage(file="./images/right.png")
right_button = Button(image=check_button, highlightthickness=0, command=button_next_word)
right_button.grid(column=0, row=1)

check_button2 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=check_button2, highlightthickness=0, command=is_known)
wrong_button.grid(column=1, row=1)
button_next_word()
window.mainloop()

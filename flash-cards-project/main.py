from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_lear = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_img, image=card_front)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="purple")
    canvas.itemconfig(card_word, text=current_card["English"], fill="purple")
    canvas.itemconfig(card_img, image=card_back)


def is_known():
    to_learn.remove(current_card)
    next_card()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)


BACKGROUND_COLOR = "white"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="card-front.png")
card_back = PhotoImage(file="card-back.png")

canvas = Canvas(width=593, height=396, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(295, 198, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


correct_image = PhotoImage(file="right.png")
wrong_image = PhotoImage(file="wrong.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

card_title = canvas.create_text(270, 120, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(270, 220, text="", font=("Ariel", 60, "bold"))

next_card()

window.mainloop()

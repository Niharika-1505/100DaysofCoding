import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Pacifico"
french_word_record = {}
try:
    remaining_words_to_learn_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_df = pandas.read_csv("data/french_words.csv")
    french_words_dict = french_words_df.to_dict(orient="records")
else:
    french_words_dict = remaining_words_to_learn_df.to_dict(orient="records")


# ---------------------------- Generate French Word ------------------------------- #
def generate_new_french_word():
    global french_word_record, flip_timer
    window.after_cancel(flip_timer)
    french_word_record = random.choice(french_words_dict)
    french_word = french_word_record["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=reveal_answer_card)


# ----------------------------Reveal Answer Card------------------------------- #
def reveal_answer_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word_text, text=french_word_record["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ----------------------------Reveal Answer Card------------------------------- #
def learnt_cards():
    french_words_dict.remove(french_word_record)
    data = pandas.DataFrame(french_words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_new_french_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=reveal_answer_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_new_french_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=learnt_cards)
right_button.grid(row=1, column=1)

generate_new_french_word()
window.mainloop()

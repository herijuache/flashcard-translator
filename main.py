import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
GUESSING_TIME = 3000
current_card = {}
to_learn = {}

# -------------------------- LOGIC SETUP ------------------------------ #
# TODO: Get all words/translation rows out as a list of dictionaries
#  i.e. [{french_word: english_word}, {french_word2: english_word2}, etc.]
# Read the data
try:
    data_frame = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")


# Pick random French word/translation
def random_word():
    global current_card, flip_timer
    # cancels the countdown to change flip the card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)

    # Goes to next card
    flip_timer = window.after(GUESSING_TIME, func=flip_card)


def known_word():
    to_learn.remove(current_card)
    # Create and update csv file "words_to_learn"

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    random_word()


def flip_card():
    canvas.itemconfig(canvas_image, image=answer_card)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(height=600, width=850)

flip_timer = window.after(GUESSING_TIME, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
answer_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 275, image=front_card)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_img, highlightthickness=0, command=random_word)
btn_wrong.grid(row=1, column=0, pady=10)

right_img = PhotoImage(file="images/right.png")
btn_right = Button(image=right_img, highlightthickness=0, command=known_word)
btn_right.grid(row=1, column=1, pady=10)

random_word()

window.mainloop()

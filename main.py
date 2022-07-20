from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(height=600, width=850)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 275, image=front_card)
title_text = canvas.create_text(400, 150,text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=wrong_img, highlightthickness=0)
btn_wrong.grid(row=1, column=0, pady=10)
right_img = PhotoImage(file="./images/right.png")
btn_right = Button(image=right_img, highlightthickness=0)
btn_right.grid(row=1, column=1, pady=10)


window.mainloop()

from idlelib.outwin import file_line_pats
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image= card_front)
canvas.create_text(400,150, text="language", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

check_button_photo = PhotoImage(file="images/right.png")
cross_button_photo = PhotoImage(file="images/wrong.png")

right_button = Button(image=check_button_photo, highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_button = Button(image=cross_button_photo, highlightthickness=0)
wrong_button.grid(row=1, column=0)


window.mainloop()
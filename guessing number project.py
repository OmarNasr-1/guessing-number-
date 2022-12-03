import tkinter
from tkinter import *
import random

# User have 10 chances
chances = 10

# Answer is randomly generated between 1 and 99
answer = random.randint(1, 99)
def check():
    global chances
    global text

    # attempts is decreased by 1 to reflect users remaining attempts.
    chances -= 1

    # Getting users input
    # int for converting it to integer data type
    guess = int(entry_window.get())

    # Comparing guess to answer
    if answer == guess:
        root.configure(bg='green')
        text.set("You win!!")
        btn_check.pack_forget()
    # Ensuring the user still has attempts - if not remove option for more attempts.
    elif chances == 0:
        root.configure(bg='red')
        text.set("You are out of attempts ,Better Luck Next Time")
        btn_check.pack_forget()
    # If guess is less than the answer - update user with remaining attempts and tell them to enter a higher number.
    elif guess < answer:
        root.configure(bg='red')
        text.set("Incorrect! - You have  "  +  str(chances)  +  "  Attempts Try Again! You guessed too small")
        # Clearing the input box for next attempt.
        entry_window.delete(0, END)
    # If guess is higher than the answer - update user with remaining attempts and tell them to enter a lower number.
    elif guess > answer:
        root.configure(bg='red')
        text.set("Incorrect! - You have "  +  str(chances)  +  "  Attempts Try Again! You guessed too high")
        entry_window.delete(0, END)
    return

root = Tk()

# bg = PhotoImage(file = "F2qRmLhRnmebc8jJAUjr_GuessTheNumber@3x.png")
# label1 = Label(root, image=bg)
# label1.place(x=0, y=0 ,relwidth=1, relheight=1)
# frame
# frame1 = Frame(root)
# frame1.pack(pady = 20 )

root.title("Guess The Number by omar & ahmed")
#  size of the window .
root.geometry("500x150")
root.configure(bg='#856ff8')
# Label to instruct the user on what to do.
label = Label(root, font='sans 16 bold',text="Guess the number between 0 and 100")
label.pack()
# User input box.
entry_window = Entry(root, width=80, borderwidth=5)
entry_window.pack()
# Check button to find out if the entered amount is correct.
btn_check = Button(root,font='sans 10 bold', bg='green', text="Check number", command=check)
btn_check.pack()
# Quit button so that the user can leave the game
btn_quit = Button(root,font='sans 10 bold',bg='red', text="  Exit  ", command=root.destroy)
btn_quit.pack()

# Creating a variable so we can update thr game progresses.
text = StringVar()
text.set("You have 10 chances ! Good luck...!")
guess_chance = Label(root, textvariable=text)
guess_chance.pack()

# loop for the program
root.mainloop()
from tkinter import *
import random

def roll_dice():
    n = dice_entry.get()
    n = int(n)
    rolls = [random.randint(1, 6) for _ in range(n)]
    output_label.config(text=f"Rolls: {rolls}")
    roll_button.config(state=DISABLED)  
    roll_again_button.config(state=NORMAL)  

def roll_again():
    dice_entry.delete(0, END)
    output_label.config(text="")
    roll_button.config(state=NORMAL) 
    roll_again_button.config(state=DISABLED) 

def quit_app():
    root.destroy()

root = Tk()
root.title("Dice Roller")
root.geometry("200x250")

result_label = Label(root, text="Enter number of dice to roll")
result_label.pack()

dice_entry = Entry(root)
dice_entry.pack()

roll_button = Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

roll_again_button = Button(root, text="Roll Again", command=roll_again, state=DISABLED)
roll_again_button.pack()

quit_button = Button(root, text="Quit", command=quit_app)
quit_button.pack()

output_label = Label(root)
output_label.pack()

root.mainloop()

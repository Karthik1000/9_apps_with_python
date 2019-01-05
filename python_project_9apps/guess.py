from tkinter import *
#from tkinter import filedialog
from tkinter import messagebox
import random

computer_guess = random.randint(1,10)

def check():
	user_guess = int(txt_guess.get())

	if user_guess < computer_guess:
		msg = "Higher!"
	elif user_guess > computer_guess:
		msg = "Lower!"
	elif user_guess == computer_guess:
		msg = "Correct!"
	#else:
	#	msg = "Something went wrong..."
	heading2["text"] = msg
	txt_guess.delete(0, 5)

def reset():
	global computer_guess
	computer_guess = random.randint(1,20)
	heading2["text"] = "Game reset. Guess again!"


def quit():
	ans=messagebox.askyesno(title="Exit",message="Do you wish to close the program?")
	if ans > 0:
		root.destroy()
		return
		

root = Tk()
root.title("Guess the number!")
root.geometry("250x300")
root.configure(bg="white")
heading1= Label(root, text="Welcome to the Guessing Game!", bg="white",font=("Helvetica",10)) 
heading1.grid(row=0,columnspan=3,pady=5)

heading2= Label(root, text="Good Luck!", bg="white") 
heading2.grid(row=1,columnspan=3)

btn_check = Button(root, text="Check", fg="green", bg="white", command=check)
btn_check.grid(row=6,column=0,padx=13)

btn_reset = Button(root, text="Reset", fg="red", bg="white", command=reset)
btn_reset.grid(row=6,column=1,padx=13)

txt_guess =Entry(root, width=15)
txt_guess.grid(row=2,columnspan=3)

btn = Button(root, text="Quit", fg="red", bg="white", command=quit)
btn.grid(row=6,column=2,pady=100,padx=13)

root.title("Guess the number")
root.mainloop()



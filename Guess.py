import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < number:
            result_label.config(text="Too Low! Try again.")
        elif guess > number:
            result_label.config(text="Too High! Try again.")
        else:
            result_label.config(
                text=f"🎉 Correct! You guessed it in {attempts} attempts."
            )
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Game Reset! Guess a number.")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

tk.Label(root, text="Guess the Number (1–100)", font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Check Guess", font=("Arial", 12), command=check_guess).pack(pady=5)
tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game).pack(pady=5)

result_label = tk.Label(root, font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()

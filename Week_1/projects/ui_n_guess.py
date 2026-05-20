import tkinter as tk
import random

# Generate random number
n = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess > n:
            result_label.config(text="Too high!")
        elif guess < n:
            result_label.config(text="Too low!")
        else:
            result_label.config(text=f"🎉 Correct! Guessed in {attempts} attempts.")
            guess_button.config(state="disabled")  # disable after win
    except ValueError:
        result_label.config(text="Enter a valid number!")

# Main window
root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess the number (1-100):").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

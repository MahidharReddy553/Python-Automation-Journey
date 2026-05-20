import tkinter as tk
from tkinter import messagebox

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero!"

def calculate(operation):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = operation(a, b)
        messagebox.showinfo("Result", f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter value of a:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Enter value of b:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

# Buttons
tk.Button(root, text="Add", command=lambda: calculate(add)).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=lambda: calculate(sub)).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=lambda: calculate(mul)).grid(row=3, column=0)
tk.Button(root, text="Divide", command=lambda: calculate(div)).grid(row=3, column=1)

root.mainloop()

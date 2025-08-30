import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwarning(
                "Too Short", "Password should be at least 4 characters long."
            )
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    use_upper = upper_var.get()
    use_numbers = number_var.get()
    use_symbols = symbol_var.get()

    char_set = list(string.ascii_lowercase)
    if use_upper:
        char_set += list(string.ascii_uppercase)
    if use_numbers:
        char_set += list(string.digits)
    if use_symbols:
        char_set += list("!@#$%^&*()-_=+[]{};:,.<>?")

    if not char_set:
        messagebox.showerror(
            "No Options Selected", "Please select at least one character set."
        )
        return

    # Ensure at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{};:,.<>?"))

    while len(password) < length:
        password.append(random.choice(char_set))

    random.shuffle(password)
    result_var.set("".join(password))


# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Variables
length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Layout
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=length_var).grid(row=0, column=1)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).grid(
    row=1, column=0, sticky="w"
)
tk.Checkbutton(root, text="Include Numbers", variable=number_var).grid(
    row=2, column=0, sticky="w"
)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).grid(
    row=3, column=0, sticky="w"
)

tk.Button(root, text="Generate Password", command=generate_password).grid(
    row=4, column=0, columnspan=2, pady=10
)

tk.Entry(root, textvariable=result_var, width=40, font=("Arial", 12)).grid(
    row=5, column=0, columnspan=2, pady=10
)

root.mainloop()

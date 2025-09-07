import tkinter as tk
from tkinter import ttk, messagebox

from caesar_cipher import caesar_encrypt, caesar_decrypt


def on_encrypt():
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer!")
        return
    encrypted = caesar_encrypt(text, shift)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encrypted)


def on_decrypt():
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer!")
        return
    decrypted = caesar_decrypt(text, shift)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, decrypted)


root = tk.Tk()
root.title("Caesar Cipher")

# Input Text
ttk.Label(root, text="Input Text:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Shift Amount
ttk.Label(root, text="Shift:").grid(row=2, column=0, sticky=tk.W, padx=5)
shift_entry = ttk.Entry(root, width=5)
shift_entry.grid(row=2, column=1, sticky=tk.W)
shift_entry.insert(0, "3")

# Buttons
encrypt_button = ttk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=3, column=0, pady=10)

decrypt_button = ttk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=3, column=1, pady=10)

# Result Text
ttk.Label(root, text="Result:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
result_text = tk.Text(root, height=5, width=40)
result_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

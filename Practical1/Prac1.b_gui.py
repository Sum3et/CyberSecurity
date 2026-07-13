import tkinter as tk
from tkinter import ttk, messagebox
import math

#Rail Fence
def rail_encrypt(text, key):
    if key <= 1 or key >= len(text):
        return text

    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    row = 0
    direction = False

    for col in range(len(text)):
        if row == 0 or row == key - 1:
            direction = not direction

        rail[row][col] = text[col]

        if direction:
            row += 1
        else:
            row -= 1

    cipher = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                cipher += rail[i][j]

    return cipher


def rail_decrypt(cipher, key):
    if key <= 1 or key >= len(cipher):
        return cipher

    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    row = 0
    direction = None

    for col in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        rail[row][col] = '*'

        if direction:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0

    for col in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        result += rail[row][col]

        if direction:
            row += 1
        else:
            row -= 1

    return result


#Columnar
def column_encrypt(text, key):
    if key <= 1 or key >= len(text):
        return text

    cipher = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(text):
            cipher[col] += text[pointer]
            pointer += key

    return ''.join(cipher)


def column_decrypt(cipher, key):
    if key <= 1 or key >= len(cipher):
        return cipher

    columns = math.ceil(len(cipher) / key)
    rows = key
    shaded = columns * rows - len(cipher)

    plain = [''] * columns

    col = 0
    row = 0

    for symbol in cipher:
        plain[col] += symbol
        col += 1

        if col == columns or (col == columns - 1 and row >= rows - shaded):
            col = 0
            row += 1

    return ''.join(plain)


#GUI
def encrypt():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2 or key >= len(text):
            messagebox.showerror("Error", "Key must be between 2 and message length - 1")
            return

        if technique.get() == "Rail Fence":
            output.set(rail_encrypt(text, key))
        else:
            output.set(column_encrypt(text, key))

    except:
        messagebox.showerror("Error", "Invalid Key")


def decrypt():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2 or key >= len(text):
            messagebox.showerror("Error", "Key must be between 2 and message length - 1")
            return

        if technique.get() == "Rail Fence":
            output.set(rail_decrypt(text, key))
        else:
            output.set(column_decrypt(text, key))

    except:
        messagebox.showerror("Error", "Invalid Key")


root = tk.Tk()
root.title("Transposition Cipher")
root.geometry("420x320")
root.resizable(False, False)

tk.Label(root, text="Transposition Cipher",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Message").pack()
message_entry = tk.Entry(root, width=40)
message_entry.pack()

tk.Label(root, text="Key").pack()
key_entry = tk.Entry(root, width=10)
key_entry.pack()

tk.Label(root, text="Technique").pack()

technique = ttk.Combobox(
    root,
    values=["Rail Fence", "Columnar"],
    state="readonly",
    width=20
)
technique.current(0)
technique.pack(pady=5)

tk.Button(root,
          text="Encrypt",
          width=15,
          command=encrypt).pack(pady=5)

tk.Button(root,
          text="Decrypt",
          width=15,
          command=decrypt).pack()

output = tk.StringVar()

tk.Label(root, text="Result").pack(pady=10)
tk.Entry(root,
         textvariable=output,
         width=45,
         state="readonly").pack()

root.mainloop()

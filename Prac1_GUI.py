# Practical 1.A GUI
import tkinter as tk
from tkinter import ttk
import string

#Caesar Cipher
def caesar_encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


#Monoalphabetic Cipher
alphabet = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

encrypt_dict = {}
decrypt_dict = {}

for i in range(26):
    encrypt_dict[alphabet[i]] = key[i]
    decrypt_dict[key[i]] = alphabet[i]


def mono_encrypt(text):
    result = ""

    for ch in text.upper():
        if ch in encrypt_dict:
            result += encrypt_dict[ch]
        else:
            result += ch

    return result


def mono_decrypt(text):
    result = ""

    for ch in text.upper():
        if ch in decrypt_dict:
            result += decrypt_dict[ch]
        else:
            result += ch

    return result


#GUI Functions
def encrypt_message():

    cipher = cipher_choice.get()
    message = message_entry.get()

    if cipher == "Caesar Cipher":
        key = int(key_entry.get())
        result = caesar_encrypt(message, key)

    else:
        result = mono_encrypt(message)

    output.set(result)


def decrypt_message():

    cipher = cipher_choice.get()
    message = message_entry.get()

    if cipher == "Caesar Cipher":
        key = int(key_entry.get())
        result = caesar_decrypt(message, key)

    else:
        result = mono_decrypt(message)

    output.set(result)


#GUI Window
root = tk.Tk()
root.title("Classical Substitution Techniques")
root.geometry("500x400")


title = tk.Label(
    root,
    text="Caesar & Monoalphabetic Cipher",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)


# Cipher Selection
tk.Label(root, text="Select Cipher").pack()

cipher_choice = ttk.Combobox(
    root,
    values=[
        "Caesar Cipher",
        "Monoalphabetic Cipher"
    ]
)

cipher_choice.current(0)
cipher_choice.pack()


# Message Input
tk.Label(root, text="Enter Message").pack()

message_entry = tk.Entry(
    root,
    width=45
)

message_entry.pack()


# Key Input
tk.Label(root, text="Enter Key (Caesar only)").pack()

key_entry = tk.Entry(root)
key_entry.pack()


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)


encrypt_button = tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    command=encrypt_message
)

encrypt_button.grid(row=0, column=0, padx=10)


decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    command=decrypt_message
)

decrypt_button.grid(row=0, column=1, padx=10)


# Output
tk.Label(root, text="Result").pack()

output = tk.StringVar()

result_entry = tk.Entry(
    root,
    textvariable=output,
    width=45
)

result_entry.pack()


root.mainloop()

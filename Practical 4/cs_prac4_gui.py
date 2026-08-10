import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import math


# =========================================================
# RSA FUNCTIONS
# =========================================================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def generate_prime():
    while True:
        number = random.randint(100, 300)

        if is_prime(number):
            return number


def generate_keys():
    global public_key, private_key

    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    while math.gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    public_key_label.config(
        text=f"Public Key:\n{public_key}"
    )

    private_key_label.config(
        text=f"Private Key:\n{private_key}"
    )

    signature_entry.delete(0, tk.END)

    result_label.config(
        text="READY\n\nEnter a message and click SIGN MESSAGE",
        fg="#2563eb"
    )

    status_label.config(
        text="RSA keys generated successfully.",
        fg="green"
    )


def get_hash(message, n):

    hash_value = hashlib.sha256(
        message.encode()
    ).hexdigest()

    hash_integer = int(hash_value, 16)

    return hash_value, hash_integer % n


def sign_message():

    if public_key is None or private_key is None:
        messagebox.showwarning(
            "Warning",
            "Please generate RSA keys first."
        )
        return

    message = message_text.get(
        "1.0",
        tk.END
    ).strip()

    if not message:
        messagebox.showwarning(
            "Warning",
            "Please enter a message."
        )
        return

    d, n = private_key

    hash_value, hash_integer = get_hash(
        message,
        n
    )

    signature = pow(
        hash_integer,
        d,
        n
    )

    hash_entry.delete(
        0,
        tk.END
    )

    hash_entry.insert(
        0,
        hash_value
    )

    signature_entry.delete(
        0,
        tk.END
    )

    signature_entry.insert(
        0,
        str(signature)
    )

    result_label.config(
        text="✓ MESSAGE SIGNED\n\n"
             "Digital signature generated successfully.\n"
             "Click VERIFY SIGNATURE to verify.",
        fg="#2563eb"
    )

    status_label.config(
        text="Digital signature generated successfully.",
        fg="green"
    )


def verify_signature():

    if public_key is None:
        messagebox.showwarning(
            "Warning",
            "Please generate RSA keys first."
        )
        return

    message = message_text.get(
        "1.0",
        tk.END
    ).strip()

    signature_text = signature_entry.get().strip()

    if not message:
        messagebox.showwarning(
            "Warning",
            "Please enter a message."
        )
        return

    if not signature_text:
        messagebox.showwarning(
            "Warning",
            "Please generate a signature first."
        )
        return

    try:
        signature = int(signature_text)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Invalid digital signature."
        )
        return

    e, n = public_key

    # Recover hash from signature
    received_hash = pow(
        signature,
        e,
        n
    )

    # Calculate hash of current message
    hash_value, current_hash = get_hash(
        message,
        n
    )

    # Compare hashes
    if received_hash == current_hash:

        result_label.config(
            text="✓  SIGNATURE VALID\n\n"
                 "MESSAGE IS AUTHENTIC\n"
                 "MESSAGE INTEGRITY VERIFIED",
            fg="#16a34a"
        )

        status_label.config(
            text="✓ Verification successful",
            fg="#16a34a"
        )

    else:

        result_label.config(
            text="✕  SIGNATURE INVALID\n\n"
                 "MESSAGE MAY HAVE BEEN MODIFIED\n"
                 "INTEGRITY VERIFICATION FAILED",
            fg="#dc2626"
        )

        status_label.config(
            text="✕ Verification failed",
            fg="#dc2626"
        )


def clear_all():

    message_text.delete(
        "1.0",
        tk.END
    )

    hash_entry.delete(
        0,
        tk.END
    )

    signature_entry.delete(
        0,
        tk.END
    )

    result_label.config(
        text="READY\n\nEnter a message and click SIGN MESSAGE",
        fg="#2563eb"
    )

    status_label.config(
        text="Ready",
        fg="#555555"
    )


# =========================================================
# GUI
# =========================================================

root = tk.Tk()

root.title(
    "RSA Digital Signature"
)

# Increased window height
root.geometry(
    "850x780"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#f4f6f8"
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg="#172554",
    height=85
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


title = tk.Label(
    header,
    text="🔐  RSA DIGITAL SIGNATURE",
    font=("Arial", 24, "bold"),
    bg="#172554",
    fg="white"
)

title.pack(
    pady=15
)


subtitle = tk.Label(
    header,
    text="Cyber & Information Security | MU NEP 2020 | Semester 5",
    font=("Arial", 10),
    bg="#172554",
    fg="#bfdbfe"
)

subtitle.pack()


# =========================================================
# KEY SECTION
# =========================================================

key_frame = tk.LabelFrame(
    root,
    text="🔑  RSA KEY GENERATION",
    font=("Arial", 11, "bold"),
    bg="white",
    padx=15,
    pady=10
)

key_frame.pack(
    fill="x",
    padx=25,
    pady=10
)


generate_button = tk.Button(
    key_frame,
    text="⚡ GENERATE RSA KEYS",
    command=generate_keys,
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)

generate_button.pack(
    pady=5
)


public_key_label = tk.Label(
    key_frame,
    text="Public Key: Not generated",
    anchor="w",
    justify="left",
    font=("Consolas", 9),
    bg="white"
)

public_key_label.pack(
    fill="x",
    pady=3
)


private_key_label = tk.Label(
    key_frame,
    text="Private Key: Not generated",
    anchor="w",
    justify="left",
    font=("Consolas", 9),
    bg="white"
)

private_key_label.pack(
    fill="x"
)


# =========================================================
# MESSAGE
# =========================================================

message_frame = tk.LabelFrame(
    root,
    text="✉  MESSAGE",
    font=("Arial", 11, "bold"),
    bg="white",
    padx=10,
    pady=10
)

message_frame.pack(
    fill="x",
    padx=25,
    pady=5
)


message_text = tk.Text(
    message_frame,
    height=3,
    font=("Arial", 11),
    wrap="word",
    relief="solid",
    bd=1
)

message_text.pack(
    fill="x"
)


# =========================================================
# HASH
# =========================================================

hash_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

hash_frame.pack(
    fill="x",
    padx=25,
    pady=5
)


tk.Label(
    hash_frame,
    text="SHA-256 Hash:",
    font=("Arial", 10, "bold"),
    bg="#f4f6f8"
).pack(
    anchor="w"
)


hash_entry = tk.Entry(
    hash_frame,
    font=("Consolas", 9),
    relief="solid",
    bd=1
)

hash_entry.pack(
    fill="x",
    pady=3
)


# =========================================================
# DIGITAL SIGNATURE
# =========================================================

signature_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

signature_frame.pack(
    fill="x",
    padx=25,
    pady=5
)


tk.Label(
    signature_frame,
    text="Digital Signature:",
    font=("Arial", 10, "bold"),
    bg="#f4f6f8"
).pack(
    anchor="w"
)


signature_entry = tk.Entry(
    signature_frame,
    font=("Consolas", 10),
    relief="solid",
    bd=1
)

signature_entry.pack(
    fill="x",
    pady=3
)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

button_frame.pack(
    pady=10
)


sign_button = tk.Button(
    button_frame,
    text="✍  SIGN MESSAGE",
    command=sign_message,
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)

sign_button.grid(
    row=0,
    column=0,
    padx=8
)


verify_button = tk.Button(
    button_frame,
    text="🛡  VERIFY SIGNATURE",
    command=verify_signature,
    font=("Arial", 10, "bold"),
    bg="#16a34a",
    fg="white",
    activebackground="#15803d",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)

verify_button.grid(
    row=0,
    column=1,
    padx=8
)


clear_button = tk.Button(
    button_frame,
    text="↻  CLEAR",
    command=clear_all,
    font=("Arial", 10, "bold"),
    bg="#64748b",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=8,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=2,
    padx=8
)


# =========================================================
# LARGE VERIFICATION RESULT
# =========================================================

result_frame = tk.LabelFrame(
    root,
    text="🛡  VERIFICATION RESULT",
    font=("Arial", 11, "bold"),
    bg="white",
    padx=10,
    pady=10
)

result_frame.pack(
    fill="x",
    padx=25,
    pady=5
)


result_label = tk.Label(
    result_frame,
    text="READY\n\nEnter a message and click SIGN MESSAGE",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="#2563eb",
    justify="center",
    height=4
)

result_label.pack(
    fill="x"
)


# =========================================================
# STATUS
# =========================================================

status_label = tk.Label(
    root,
    text="● Ready",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#555555"
)

status_label.pack(
    pady=5
)


# =========================================================
# VARIABLES
# =========================================================

public_key = None
private_key = None


# =========================================================
# START GUI
# =========================================================

root.mainloop()

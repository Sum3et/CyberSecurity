import tkinter as tk
from tkinter import messagebox

# DIFFIE-HELLMAN KEY EXCHANGE
def calculate_exchange():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())
        a = int(alice_private_entry.get())
        b = int(bob_private_entry.get())

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )
        return

    if p <= 1:
        messagebox.showerror(
            "Invalid Prime",
            "Prime number must be greater than 1."
        )
        return

    if a <= 0 or b <= 0:
        messagebox.showerror(
            "Invalid Private Key",
            "Private keys must be positive."
        )
        return

    # Alice's public key
    alice_public = pow(g, a, p)

    # Bob's public key
    bob_public = pow(g, b, p)

    # Shared secrets
    alice_secret = pow(
        bob_public,
        a,
        p
    )

    bob_secret = pow(
        alice_public,
        b,
        p
    )

    # Display Alice
    alice_public_value.config(
        text=str(alice_public)
    )

    alice_secret_value.config(
        text=str(alice_secret)
    )

    # Display Bob
    bob_public_value.config(
        text=str(bob_public)
    )

    bob_secret_value.config(
        text=str(bob_secret)
    )

    # Verify
    if alice_secret == bob_secret:

        result_title.config(
            text="✓ KEY EXCHANGE SUCCESSFUL",
            fg="#22c55e"
        )

        result_message.config(
            text="Alice and Bob generated the same shared secret key."
        )

        status_label.config(
            text="● Secure shared key established",
            fg="#22c55e"
        )

    else:

        result_title.config(
            text="✕ KEY EXCHANGE FAILED",
            fg="#ef4444"
        )

        result_message.config(
            text="The shared secret keys do not match."
        )

        status_label.config(
            text="● Key exchange failed",
            fg="#ef4444"
        )


def clear_all():

    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)

    alice_private_entry.delete(0, tk.END)
    bob_private_entry.delete(0, tk.END)

    alice_public_value.config(text="—")
    alice_secret_value.config(text="—")

    bob_public_value.config(text="—")
    bob_secret_value.config(text="—")

    result_title.config(
        text="READY",
        fg="#60a5fa"
    )

    result_message.config(
        text="Enter the parameters and start the key exchange."
    )

    status_label.config(
        text="● Ready",
        fg="#94a3b8"
    )

# GUI
root = tk.Tk()

root.title(
    "Diffie-Hellman Key Exchange"
)

root.geometry(
    "950x720"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#0b1120"
)

# HEADER
header = tk.Frame(
    root,
    bg="#111827",
    height=100
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


tk.Label(
    header,
    text="🔐  DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 24, "bold"),
    bg="#111827",
    fg="white"
).pack(
    pady=(18, 5)
)


tk.Label(
    header,
    text="Cyber & Information Security  |  MU NEP 2020  |  Semester 5",
    font=("Arial", 10),
    bg="#111827",
    fg="#94a3b8"
).pack()

# PUBLIC PARAMETERS
parameter_frame = tk.LabelFrame(
    root,
    text="  PUBLIC PARAMETERS  ",
    font=("Arial", 11, "bold"),
    bg="#111827",
    fg="white",
    padx=15,
    pady=10
)

parameter_frame.pack(
    fill="x",
    padx=30,
    pady=15
)


# Prime
tk.Label(
    parameter_frame,
    text="Prime Number (p)",
    font=("Arial", 10, "bold"),
    bg="#111827",
    fg="#cbd5e1"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


p_entry = tk.Entry(
    parameter_frame,
    font=("Consolas", 11),
    width=18,
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat"
)

p_entry.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)

p_entry.insert(
    0,
    "23"
)


# Primitive root
tk.Label(
    parameter_frame,
    text="Primitive Root (g)",
    font=("Arial", 10, "bold"),
    bg="#111827",
    fg="#cbd5e1"
).grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


g_entry = tk.Entry(
    parameter_frame,
    font=("Consolas", 11),
    width=18,
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat"
)

g_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)

g_entry.insert(
    0,
    "5"
)

# ALICE AND BOB
people_frame = tk.Frame(
    root,
    bg="#0b1120"
)

people_frame.pack(
    fill="x",
    padx=30
)

# ALICE
alice_frame = tk.LabelFrame(
    people_frame,
    text="  👩 ALICE  ",
    font=("Arial", 12, "bold"),
    bg="#111827",
    fg="#60a5fa",
    padx=20,
    pady=10
)

alice_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)


tk.Label(
    alice_frame,
    text="Private Key (a)",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w"
)


alice_private_entry = tk.Entry(
    alice_frame,
    font=("Consolas", 11),
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat"
)

alice_private_entry.pack(
    fill="x",
    pady=5
)

alice_private_entry.insert(
    0,
    "6"
)


tk.Label(
    alice_frame,
    text="Public Key (A)",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w",
    pady=(8, 0)
)


alice_public_value = tk.Label(
    alice_frame,
    text="—",
    font=("Consolas", 16, "bold"),
    bg="#0f172a",
    fg="#60a5fa",
    anchor="w",
    padx=10,
    pady=8
)

alice_public_value.pack(
    fill="x",
    pady=5
)


tk.Label(
    alice_frame,
    text="Shared Secret",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w",
    pady=(8, 0)
)


alice_secret_value = tk.Label(
    alice_frame,
    text="—",
    font=("Consolas", 16, "bold"),
    bg="#0f172a",
    fg="#22c55e",
    anchor="w",
    padx=10,
    pady=8
)

alice_secret_value.pack(
    fill="x",
    pady=5
)


#BOB
bob_frame = tk.LabelFrame(
    people_frame,
    text="  👨 BOB  ",
    font=("Arial", 12, "bold"),
    bg="#111827",
    fg="#c084fc",
    padx=20,
    pady=10
)

bob_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(10, 0)
)


tk.Label(
    bob_frame,
    text="Private Key (b)",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w"
)


bob_private_entry = tk.Entry(
    bob_frame,
    font=("Consolas", 11),
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat"
)

bob_private_entry.pack(
    fill="x",
    pady=5
)

bob_private_entry.insert(
    0,
    "15"
)


tk.Label(
    bob_frame,
    text="Public Key (B)",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w",
    pady=(8, 0)
)


bob_public_value = tk.Label(
    bob_frame,
    text="—",
    font=("Consolas", 16, "bold"),
    bg="#0f172a",
    fg="#c084fc",
    anchor="w",
    padx=10,
    pady=8
)

bob_public_value.pack(
    fill="x",
    pady=5
)


tk.Label(
    bob_frame,
    text="Shared Secret",
    font=("Arial", 10),
    bg="#111827",
    fg="#cbd5e1"
).pack(
    anchor="w",
    pady=(8, 0)
)


bob_secret_value = tk.Label(
    bob_frame,
    text="—",
    font=("Consolas", 16, "bold"),
    bg="#0f172a",
    fg="#22c55e",
    anchor="w",
    padx=10,
    pady=8
)

bob_secret_value.pack(
    fill="x",
    pady=5
)

# BUTTONS
button_frame = tk.Frame(
    root,
    bg="#0b1120"
)

button_frame.pack(
    pady=18
)


tk.Button(
    button_frame,
    text="🔄  EXCHANGE KEYS",
    command=calculate_exchange,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=30,
    pady=10,
    cursor="hand2"
).grid(
    row=0,
    column=0,
    padx=8
)


tk.Button(
    button_frame,
    text="↻  CLEAR",
    command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#475569",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    padx=30,
    pady=10,
    cursor="hand2"
).grid(
    row=0,
    column=1,
    padx=8
)

# RESULT
result_frame = tk.LabelFrame(
    root,
    text="  🔐 KEY EXCHANGE RESULT  ",
    font=("Arial", 11, "bold"),
    bg="#111827",
    fg="white",
    padx=10,
    pady=8
)

result_frame.pack(
    fill="x",
    padx=30
)


result_title = tk.Label(
    result_frame,
    text="READY",
    font=("Arial", 16, "bold"),
    bg="#111827",
    fg="#60a5fa"
)

result_title.pack(
    pady=(5, 2)
)


result_message = tk.Label(
    result_frame,
    text="Enter the parameters and start the key exchange.",
    font=("Arial", 10),
    bg="#111827",
    fg="#94a3b8"
)

result_message.pack(
    pady=(0, 8)
)

# STATUS
status_label = tk.Label(
    root,
    text="● Ready",
    font=("Arial", 9),
    bg="#0b1120",
    fg="#94a3b8"
)

status_label.pack(
    pady=8
)


root.mainloop()

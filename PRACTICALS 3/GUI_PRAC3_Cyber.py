import tkinter as tk
from tkinter import ttk, messagebox
import hmac
import hashlib

# -------------------- Functions --------------------

def generate_mac(key, message):
    return hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()


def generate():
    key = key_entry.get()
    message = message_entry.get()

    if not key or not message:
        messagebox.showerror("Error", "Please enter the Secret Key and Message.")
        return

    mac = generate_mac(key, message)

    generated_mac.config(state="normal")
    generated_mac.delete(0, tk.END)
    generated_mac.insert(0, mac)
    generated_mac.config(state="readonly")


def verify():
    key = key_entry.get()
    message = verify_message.get()
    mac = verify_mac.get()

    if not key or not message or not mac:
        messagebox.showerror("Error", "Please fill all verification fields.")
        return

    calculated = generate_mac(key, message)

    if hmac.compare_digest(calculated, mac):
        messagebox.showinfo("Verification", "✅ Message Verified Successfully")
    else:
        messagebox.showerror("Verification", "❌ Message Verification Failed")


# -------------------- Window --------------------

root = tk.Tk()
root.title("HMAC Message Authentication")
root.geometry("720x480")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#EAF4FC",
                font=("Segoe UI", 11))

style.configure("Title.TLabel",
                font=("Segoe UI", 18, "bold"),
                foreground="#1E3A8A",
                background="#EAF4FC")

style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                padding=6)

# -------------------- Title --------------------

title = ttk.Label(root,
                  text="🔐 HMAC Message Authentication",
                  style="Title.TLabel")
title.pack(pady=15)

# -------------------- Generate Frame --------------------

gen_frame = tk.LabelFrame(root,
                          text=" Generate MAC ",
                          font=("Segoe UI", 11, "bold"),
                          bg="white",
                          fg="#1E3A8A",
                          padx=15,
                          pady=10)

gen_frame.pack(fill="x", padx=20, pady=10)

ttk.Label(gen_frame, text="Secret Key").grid(row=0, column=0, sticky="w", pady=8)

key_entry = ttk.Entry(gen_frame, width=55)
key_entry.grid(row=0, column=1, padx=10)

ttk.Label(gen_frame, text="Message").grid(row=1, column=0, sticky="w", pady=8)

message_entry = ttk.Entry(gen_frame, width=55)
message_entry.grid(row=1, column=1, padx=10)

ttk.Button(gen_frame,
           text="Generate MAC",
           command=generate).grid(row=2, column=1, pady=10)

ttk.Label(gen_frame, text="Generated MAC").grid(row=3, column=0, sticky="w", pady=8)

generated_mac = ttk.Entry(gen_frame, width=75)
generated_mac.grid(row=3, column=1, padx=10)
generated_mac.config(state="readonly")

# -------------------- Verification Frame --------------------

verify_frame = tk.LabelFrame(root,
                             text=" Verify MAC ",
                             font=("Segoe UI", 11, "bold"),
                             bg="white",
                             fg="#1E3A8A",
                             padx=15,
                             pady=10)

verify_frame.pack(fill="x", padx=20, pady=10)

ttk.Label(verify_frame, text="Message").grid(row=0, column=0, sticky="w", pady=8)

verify_message = ttk.Entry(verify_frame, width=55)
verify_message.grid(row=0, column=1, padx=10)

ttk.Label(verify_frame, text="MAC").grid(row=1, column=0, sticky="w", pady=8)

verify_mac = ttk.Entry(verify_frame, width=75)
verify_mac.grid(row=1, column=1, padx=10)

ttk.Button(verify_frame,
           text="Verify MAC",
           command=verify).grid(row=2, column=1, pady=15)

# -------------------- Footer --------------------

footer = tk.Label(root,
                  text="HMAC using SHA-256",
                  bg="#EAF4FC",
                  fg="gray40",
                  font=("Segoe UI", 9))

footer.pack(side="bottom", pady=10)

root.mainloop()

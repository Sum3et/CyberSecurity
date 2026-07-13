# Practical 1.A
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


#Main Menu
while True:

    print("\n===== Classical Substitution Techniques =====")
    print("1. Caesar Cipher")
    print("2. Monoalphabetic Cipher")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        print("\n1. Encrypt")
        print("2. Decrypt")

        op = input("Enter Choice: ")

        message = input("Enter Message: ")
        shift = int(input("Enter Key: "))

        if op == "1":
            print("Encrypted Message :", caesar_encrypt(message, shift))
        elif op == "2":
            print("Decrypted Message :", caesar_decrypt(message, shift))
        else:
            print("Invalid Choice")

    elif choice == "2":

        print("\n1. Encrypt")
        print("2. Decrypt")

        op = input("Enter Choice: ")

        message = input("Enter Message: ")

        if op == "1":
            print("Encrypted Message :", mono_encrypt(message))
        elif op == "2":
            print("Decrypted Message :", mono_decrypt(message))
        else:
            print("Invalid Choice")

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")



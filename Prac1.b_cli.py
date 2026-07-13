import math

#Rail Fence Cipher
def rail_encrypt(text, key):
    if key <= 1:
        return text

    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    row = 0
    direction = False

    for col in range(len(text)):
        if row == 0 or row == key - 1:
            direction = not direction

        rail[row][col] = text[col]
        row += 1 if direction else -1

    cipher = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                cipher += rail[i][j]

    return cipher


def rail_decrypt(cipher, key):
    if key <= 1:
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
        row += 1 if direction else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    direction = None

    for col in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        result += rail[row][col]
        row += 1 if direction else -1

    return result


#Columnar Transposition Cipher
def column_encrypt(message, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key

    return ''.join(cipher)


def column_decrypt(cipher, key):
    cols = math.ceil(len(cipher) / key)
    rows = key
    shaded = cols * rows - len(cipher)

    plain = [''] * cols

    col = 0
    row = 0

    for symbol in cipher:
        plain[col] += symbol
        col += 1

        if col == cols or (col == cols - 1 and row >= rows - shaded):
            col = 0
            row += 1

    return ''.join(plain)


#Main Program
while True:
    print("\n===== TRANSPOSITION CIPHER =====")
    print("1. Rail Fence Cipher")
    print("2. Columnar Transposition Cipher")
    print("3. Exit")

    choice = input("Select Technique: ")

    if choice == "3":
        print("Program Ended.")
        break

    if choice not in ["1", "2"]:
        print("Invalid Choice!")
        continue

    print("\n1. Encrypt")
    print("2. Decrypt")
    operation = input("Choose Operation: ")

    text = input("Enter Message: ")
    key = int(input("Enter Key: "))

    if choice == "1":
        if operation == "1":
            print("Encrypted Text:", rail_encrypt(text, key))
        elif operation == "2":
            print("Decrypted Text:", rail_decrypt(text, key))
        else:
            print("Invalid Operation!")

    elif choice == "2":
        if operation == "1":
            print("Encrypted Text:", column_encrypt(text, key))
        elif operation == "2":
            print("Decrypted Text:", column_decrypt(text, key))
        else:
            print("Invalid Operation!")

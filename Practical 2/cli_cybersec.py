from math import gcd

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Input two prime numbers
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

# Choose e
e = int(input("Enter value of e: "))

if gcd(e, phi) != 1:
    print("Error: e must be co-prime with phi(n).")
    exit()

# Calculate d
d = mod_inverse(e, phi)

if d is None:
    print("Error: Could not calculate private key.")
    exit()

print("\nPublic Key :", (e, n))
print("Private Key:", (d, n))

# Encrypt
msg = int(input("\nEnter message (integer less than n): "))

if msg >= n:
    print("Error: Message must be less than", n)
    exit()

cipher = pow(msg, e, n)
print("Encrypted Message:", cipher)

# Decrypt
plain = pow(cipher, d, n)
print("Decrypted Message:", plain)

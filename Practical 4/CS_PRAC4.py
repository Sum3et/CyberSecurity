import hashlib
import random
import math

# Generate a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime():
    while True:
        n = random.randint(100, 300)
        if is_prime(n):
            return n


# Generate RSA keys
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

print("RSA Keys Generated")
print("Public Key :", public_key)
print("Private Key:", private_key)


# Get message
message = input("\nEnter message: ")

# Hash the message
hash_value = hashlib.sha256(message.encode()).hexdigest()

# Convert hash to integer
hash_int = int(hash_value, 16)

# Reduce hash to fit small demonstration RSA key
hash_int = hash_int % n


# Create digital signature using private key
signature = pow(hash_int, d, n)

print("\nSHA-256 Hash:", hash_value)
print("Digital Signature:", signature)


# Verify signature
received_hash = pow(signature, e, n)

current_hash = int(
    hashlib.sha256(message.encode()).hexdigest(),
    16
) % n

if received_hash == current_hash:
    print("\nSignature Verification: SUCCESS")
    print("Message is authentic and has not been modified.")
else:
    print("\nSignature Verification: FAILED")


# Test modified message
modified_message = input("\nEnter modified message: ")

modified_hash = int(
    hashlib.sha256(modified_message.encode()).hexdigest(),
    16
) % n

if received_hash == modified_hash:
    print("Modified message: VALID")
else:
    print("Modified message: INVALID")
    print("Integrity check failed.")

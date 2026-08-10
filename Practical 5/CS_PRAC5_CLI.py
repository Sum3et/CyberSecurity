# Diffie-Hellman Key Exchange
# Cyber & Information Security - MU NEP 2020 Sem 5

print("=" * 55)
print("       DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 55)

# Public values
p = int(input("\nEnter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Private keys
a = int(input("\nEnter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

# Alice generates public key
A = pow(g, a, p)

# Bob generates public key
B = pow(g, b, p)

# Shared secret keys
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("\n" + "-" * 55)
print("PUBLIC PARAMETERS")
print("-" * 55)

print("Prime (p):", p)
print("Primitive Root (g):", g)

print("\n" + "-" * 55)
print("KEY EXCHANGE")
print("-" * 55)

print("Alice Private Key:", a)
print("Alice Public Key :", A)

print("\nBob Private Key  :", b)
print("Bob Public Key   :", B)

print("\n" + "-" * 55)
print("SHARED SECRET")
print("-" * 55)

print("Alice's Shared Secret:", alice_secret)
print("Bob's Shared Secret  :", bob_secret)

if alice_secret == bob_secret:
    print("\n✓ KEY EXCHANGE SUCCESSFUL")
    print("Both Alice and Bob have the same secret key.")
else:
    print("\n✗ KEY EXCHANGE FAILED")

print("=" * 55)

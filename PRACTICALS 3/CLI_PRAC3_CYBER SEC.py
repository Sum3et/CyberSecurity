import hmac
import hashlib

# Function to generate MAC
def generate_mac(key, message):
    return hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

# Function to verify MAC
def verify_mac(key, message, received_mac):
    calculated_mac = generate_mac(key, message)
    return hmac.compare_digest(calculated_mac, received_mac)

# User input
key = input("Enter the secret key: ")
message = input("Enter the message: ")

# Generate MAC
mac = generate_mac(key, message)
print("\nGenerated MAC:", mac)

# Verification
print("\n--- Verification ---")
verify_message = input("Enter the message to verify: ")
received_mac = input("Enter the MAC to verify: ")

if verify_mac(key, verify_message, received_mac):
    print("Message Verified Successfully")
else:
    print("Message Verification Failed")

# Simple encryption and decryption with Caesar Cipher
print("🔐 Simple Python Cryptography Demo")

# Function to encrypt a message with a shift
def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            stay_in_alphabet = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - stay_in_alphabet + shift) % 26 + stay_in_alphabet)
        else:
            encrypted += char
    return encrypted

# Function to decrypt by reversing the shift
def decrypt(text, shift):
    return encrypt(text, -shift)

# Test the functions
message = "Hello World!"
shift = 3
encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


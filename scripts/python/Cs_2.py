def text_to_hex(text):
    return ''.join(hex(ord(char))[2:].zfill(2) for char in text)

def hex_to_text(hex_string):
    return ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))

def xor_hex_strings(hex_str1, hex_str2):
    return hex(int(hex_str1, 16) ^ int(hex_str2, 16))[2:]

plaintext = 'Pay $1000 to Bob'
key = '7e4d6c73d5240a948f86951bc29481a5'

# Print plaintext
print("Plaintext:")
print(plaintext)

# Convert plaintext to hex
plaintext_hex = text_to_hex(plaintext)
print("\nPlaintext in Hex:")
print(plaintext_hex)

# Compute ciphertext
ciphertext_hex = xor_hex_strings(plaintext_hex, key)
print("\nCiphertext in Hex:")
print(ciphertext_hex)

# Decrypt ciphertext
decrypted_hex = xor_hex_strings(ciphertext_hex, key)
print("\nDecrypted Plaintext in Hex:")
print(decrypted_hex)

# Convert decrypted plaintext from hex to text
decrypted_plaintext = hex_to_text(decrypted_hex)
print("\nDecrypted Plaintext:")
print(decrypted_plaintext)

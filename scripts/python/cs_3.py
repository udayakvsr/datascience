def text_to_hex(text):
    return ''.join(hex(ord(char))[2:].zfill(2) for char in text)

def hex_to_text(hex_string):
    return ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))

def xor_hex_strings(hex_str1, hex_str2):
    return hex(int(hex_str1, 16) ^ int(hex_str2, 16))[2:]

plaintext = 'Pay $1000 to Bob'
key = '7e4d6c73d5240a948f86951bc29481a5'

# Convert plaintext to hex
plaintext_hex = text_to_hex(plaintext)
print("Plaintext in Hex:")
print(plaintext_hex)

# Compute ciphertext
ciphertext_hex = xor_hex_strings(plaintext_hex, key)
print("\nCiphertext in Hex:")
print(ciphertext_hex)

# Decrypt ciphertext
decrypted_hex = xor_hex_strings(ciphertext_hex, key)
print("\nDecrypted Plaintext in Hex:")
print(decrypted_hex)

# Copy ciphertext to ciphertext1 and modify ciphertext1 for the malleability attack
ciphertext1_hex = ciphertext_hex[:]
# Perform malleability attack by XORing the difference between plaintexts with ciphertext
modified_plaintext_hex = text_to_hex('Pay $9000 to Bob')
malleability_difference_hex = xor_hex_strings(plaintext_hex, modified_plaintext_hex)
ciphertext1_hex = xor_hex_strings(ciphertext1_hex, malleability_difference_hex)
print("\nCiphertext1 in Hex:")
print(ciphertext1_hex)

# Decrypt modified ciphertext1
decrypted_ciphertext1_hex = xor_hex_strings(ciphertext1_hex, key)
print("\nDecrypted Plaintext from Modified Ciphertext1 in Hex:")
print(decrypted_ciphertext1_hex)

# Convert decrypted plaintext from hex to text
decrypted_plaintext1 = hex_to_text(decrypted_ciphertext1_hex)
print("\nDecrypted Plaintext from Modified Ciphertext1:")
print(decrypted_plaintext1)

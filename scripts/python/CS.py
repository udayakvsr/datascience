def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def texttohex(text):
    return ''.join(hex(ord(char))[2:].zfill(2) for char in text)

def hextotext(hex_string):
    return ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))

def xorhexstrings(hex_str1, hex_str2):
    return hex(int(hex_str1, 16) ^ int(hex_str2, 16))[2:]

def one_time_pad_encrypt(plaintext, key):
    return xorhexstrings(plaintext, key)

### Question 3 :
print('\n################## Answer 3 ######################')
# Read plaintext from file
plaintext = read_file(r'C:\Users\Public\plaintext.txt')
print("Plaintext:",plaintext)
plaintexthex = texttohex(plaintext)
print("Plaintext Hex:",plaintexthex)
# Read key from file
key = read_file(r'C:\Users\Public\key.txt')
print("Key output:",key)

# creating ciphertext
ciphertext = xorhexstrings(plaintexthex, key)
print("Ciphertext Hex:",ciphertext)

# Save ciphertext to file
write_file(r'C:\Users\Public\ciphertext.txt', ciphertext)

### Question 4 :
print('\n################## Answer 4 ######################')
# Decrypt ciphertext
decrypted = xorhexstrings(ciphertext, key)
print("Decrypted Hex for Plaintext :",decrypted)

# Convert decrypted plaintext from hex to text
decryptedplaintext_output = hextotext(decrypted)
print("Decrypted Plaintext Output:",decryptedplaintext_output)


### Question 5 :
print('\n################## Answer 5 #######################')
# Copy ciphertext.txt to ciphertext1.txt and modify ciphertext1 for the malleability attack
ciphertext1 = ciphertext[:]
write_file(r'C:\Users\Public\ciphertext1.txt', ciphertext1)
# Perform malleability attack by difference between plaintexts with ciphertext
modifiedplaintext = texttohex('Pay $9000 to Bob')
malleabilitydifference = xorhexstrings(plaintexthex, modifiedplaintext)
ciphertext1 = xorhexstrings(ciphertext1, malleabilitydifference)
print("Ciphertext1 in Hex:",ciphertext1)

# Decrypt ciphertext1
ciphertext1decrypted = xorhexstrings(ciphertext1, key)
print("Decrypted Ciphertext1 :",ciphertext1decrypted)

# Convert decrypted ciphertext1 from hex to text
decryptedciphertext1 = hextotext(ciphertext1decrypted)
print("Decrypted Plaintext of Ciphertext1:",decryptedciphertext1)

### Question 6 :
print('\n################## Answer 6 ######################')
#  Bitwise XOR of ciphertexts
xor_result_hex = xorhexstrings(ciphertext, ciphertext1)

#  XOR result
print("Bitwise XOR of ciphertexts:",xor_result_hex)

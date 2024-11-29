import os

def monoalphabetic_encrypt(text):
    key = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPLKJHGFDSAZXCVBNM")
    return text.translate(key)

def polyalphabetic_encrypt(text, key="KEY"):
    result = []
    key = key.upper()
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def vernam_encrypt(text, key="SECRET"):
    result = []
    key = key.upper()
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            result.append(chr(((ord(char) - ord('A')) ^ (ord(key[i % len(key)]) - ord('A'))) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_encrypt(text, key="SECRET"):
    return polyalphabetic_encrypt(text, key)

def transpositional_encrypt(text):
    return text[::-1]

def rsa_encrypt(text):
    # Simple mock-up for RSA encryption (for educational purposes)
    return ''.join(chr(ord(char) + 3) for char in text)

def encrypt_file(filepath, output_dir):
    with open(filepath, 'r') as file:
        content = file.read()

    # Apply all encryption algorithms sequentially
    content = monoalphabetic_encrypt(content)
    content = polyalphabetic_encrypt(content)
    content = vernam_encrypt(content)
    content = vigenere_encrypt(content)
    content = transpositional_encrypt(content)
    content = rsa_encrypt(content)

    encrypted_filepath = os.path.join(output_dir, 'encrypted_' + os.path.basename(filepath))
    with open(encrypted_filepath, 'w') as file:
        file.write(content)

    return encrypted_filepath

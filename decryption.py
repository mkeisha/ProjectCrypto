import os

def monoalphabetic_decrypt(text):
    key = str.maketrans("QWERTYUIOPLKJHGFDSAZXCVBNM", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return text.translate(key)

def polyalphabetic_decrypt(text, key="KEY"):
    result = []
    key = key.upper()
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def vernam_decrypt(text, key="SECRET"):
    result = []
    key = key.upper()
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            result.append(chr(((ord(char) - ord('A')) ^ (ord(key[i % len(key)]) - ord('A'))) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key="SECRET"):
    return polyalphabetic_decrypt(text, key)

def transpositional_decrypt(text):
    return text[::-1]

def rsa_decrypt(text):
    # Simple mock-up for RSA decryption (for educational purposes)
    return ''.join(chr(ord(char) - 3) for char in text)

def decrypt_file(filepath, output_dir):
    with open(filepath, 'r') as file:
        content = file.read()

    # Apply all decryption algorithms in reverse order
    content = rsa_decrypt(content)
    content = transpositional_decrypt(content)
    content = vigenere_decrypt(content)
    content = vernam_decrypt(content)
    content = polyalphabetic_decrypt(content)
    content = monoalphabetic_decrypt(content)

    decrypted_filepath = os.path.join(output_dir, 'decrypted_' + os.path.basename(filepath))
    with open(decrypted_filepath, 'w') as file:
        file.write(content)

    return decrypted_filepath

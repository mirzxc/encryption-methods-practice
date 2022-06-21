import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    count_engalphabet = 26
    keyword *= len(plaintext) // len(keyword) + 1
    for i in range(len(plaintext) - len(keyword)):
        keyword += keyword[i]
    for i, letter in enumerate(plaintext):
        if keyword[i].upper() in string.ascii_uppercase:
            shift = ord(keyword[i].upper()) % count_engalphabet + ord("A")
        if letter in string.ascii_lowercase:
            ciphertext += chr(
                (ord(letter) + shift - ord("a")) % count_engalphabet + ord("a")
            )  # encrypt lowercase
        elif letter in string.ascii_uppercase:
            ciphertext += chr(
                (ord(letter) + shift - ord("A")) % count_engalphabet + ord("A")
            )  # encrypt uppercase
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    count_engalphabet = 26
    keyword *= len(ciphertext) // len(keyword) + 1
    for i in range(len(ciphertext) - len(keyword)):
        keyword += keyword[i]
    for i, letter in enumerate(ciphertext):
        if keyword[i].upper() in string.ascii_uppercase:
            shift = ord(keyword[i].upper()) % count_engalphabet + ord("A")
        if letter in string.ascii_lowercase:
            # encrypt lowercase
            plaintext += chr((ord(letter) - shift - ord("a")) % count_engalphabet + ord("a"))
        elif letter in string.ascii_uppercase:
            # encrypt uppercase
            plaintext += chr((ord(letter) - shift - ord("A")) % count_engalphabet + ord("A"))
        else:
            plaintext += letter
    return plaintext

import string
import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    count_engalphabet = 26
    for letter in plaintext:
        if ord("a") <= ord(letter) <= ord("z"):
            # encrypt lowercase
            ciphertext += chr((ord(letter) + shift - ord("a")) % count_engalphabet + ord("a"))
        elif letter in string.ascii_uppercase:
            # encrypt uppercase
            ciphertext += chr((ord(letter) + shift - ord("A")) % count_engalphabet + ord("A"))
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    count_engalphabet = 26
    for letter in ciphertext:
        if ord("a") <= ord(letter) <= ord("z"):
            plaintext += chr(
                (ord(letter) - shift - ord("a")) % count_engalphabet + ord("a")
            )  # decrypt lowercase
        elif letter in string.ascii_uppercase:
            plaintext += chr(
                (ord(letter) - shift - ord("A")) % count_engalphabet + ord("A")
            )  # decrypt uppercase
        else:
            plaintext += letter
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift

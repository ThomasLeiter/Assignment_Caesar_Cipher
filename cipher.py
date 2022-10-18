"""
Simple module for text encryption/decryption

CONSTANTS:
----------
LOWER_CASE_ALPHABET
UPPER_CASE_ALPHABET
NUMERIC_CIPHERS
SPECIAL_CHARACTERS
FULL_ALPHABET

CLASSES:
--------
CaesarCipher
ShiftCipher
VigenereCipher
"""

LOWER_CASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_ALPHABET = LOWER_CASE_ALPHABET.upper()
NUMERIC_CIPHERS = "0123456789"
SPECIAL_CHARACTERS = ",;.:-_!?()[]{}/\ \n\t=+*#<>|"

FULL_ALPHABET = LOWER_CASE_ALPHABET + UPPER_CASE_ALPHABET + \
    NUMERIC_CIPHERS + SPECIAL_CHARACTERS


class CaesarCipher:
    """
    Base class for a caesar style cipher. Should be initialized with a key.

    METHODS:
    --------
    encrypt:
        str -> str
        Encrypt a given message
    decrypt:
        str -> str
        Decrypt a given message
    """
    def __init__(self, key):
        self.__key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    def encipher(self, text):
        """
        PARAMETERS:
        -----------
        text: str
            the text message to encrypt
        
        RETURNS:
        --------
        str:
            the encrypted message
        """
        raise NotImplementedError

    def decipher(self, text):
        """
        PARAMETERS:
        -----------
        text: str
            the text message to decrypt
        
        RETURNS:
        --------
        str:
            the decrypted message
        """
        raise NotImplementedError


class ShiftCipher(CaesarCipher):
    """
    Simple implementation of a Caesar Cipher that shifts 
    an alphabet by a natural number and substitutes 
    message characters by their shifted cousins.
    """

    def __init__(self, key, alphabet=LOWER_CASE_ALPHABET):
        super().__init__(key)
        self.__alphabet = alphabet

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet):
        self.__alphabet = alphabet

    # Overrides encipher method
    def encipher(self, text):
        alpha_len = len(self.alphabet)
        substitution_dict = {self.alphabet[i]: self.alphabet[(
            i + self.key) % alpha_len] for i in range(alpha_len)}
        return "".join(substitution_dict[c] for c in text)

    # Overrides decipher method
    def decipher(self, text):
        alpha_len = len(self.alphabet)
        substitution_dict = {self.alphabet[i]: self.alphabet[(
            i - self.key) % alpha_len] for i in range(alpha_len)}
        return "".join(substitution_dict[c] for c in text)


def test_shift_cipher():
    cipher = ShiftCipher(7)
    print(cipher.__doc__)
    dec_text = "abcdefghijklmnopqrstuvwxyz"
    enc_text = cipher.encipher(dec_text)
    print(f"{dec_text=}\n{enc_text=}\n")
    cipher.key = 3
    enc_text = "glhvhuwhawlvwyhuvfkoxhvvhow"
    dec_text = cipher.decipher(enc_text)
    print(f"{enc_text=}\n{dec_text=}\n")


class VigenereCipher(CaesarCipher):
    """
    Simple Implementation of the Vigenere Cipher 

    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    """
    def __init__(self, key, alphabet=FULL_ALPHABET):
        super().__init__(key)
        self.__alphabet = alphabet

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet):
        self.__alphabet = alphabet

    # Overrides encipher method
    def encipher(self, text):
        alpha_len = len(self.alphabet)
        key_len = len(self.key)
        idx = {self.alphabet[i]: i for i in range(alpha_len)}
        return "".join(self.alphabet[(idx[text[i]] + idx[self.key[i % key_len]]) %
                                     alpha_len] for i in range(len(text)))

    # Overrides decipher method
    def decipher(self, text):
        alpha_len = len(self.alphabet)
        key_len = len(self.key)
        idx = {self.alphabet[i]: i for i in range(alpha_len)}
        return "".join(self.alphabet[(idx[text[i]] - idx[self.key[i % key_len]]) %
                                     alpha_len] for i in range(len(text)))


def test_vigenere_cipher():
    key = "!--Pa55w0rD--!"
    cipher = VigenereCipher(key)
    print(cipher.__doc__)
    original_file = "vigenere_cipher.txt"
    encrypted_file = "vigenere_cipher_encrypted.txt"
    with open(original_file) as f:
        text = f.read()
    print(f"Original Text:\n\n{text}\n")
    encrypted_text = cipher.encipher(text)
    print(f"Encrypted Text:\n\n{encrypted_text}\n")
    with open(encrypted_file, "w") as f:
        f.write(encrypted_text)
    print(f"Retrieving and decrypting file ...\n")
    with open(encrypted_file, "r") as f:
        encrypted_text = f.read()
    decrypted_text = cipher.decipher(encrypted_text)
    print(f"Decrypted Text:\n\n{decrypted_text}\n")


if __name__ == "__main__":
    print(__doc__)
    test_shift_cipher()
    test_vigenere_cipher()

"""
Implementation of a simple Caesar Cipher

AUTHORS:
--------
Trang Chu Thi
Thomas Leiter
"""

class ShiftCipher:
    def __init__(self, key):
        self.__key = key

    def encipher(self, text):
        abc = "abcdefghijklmnopqrstuvwxyz"
        cipher_alphabet = abc[self.__key:] + abc[:self.__key]
        encrypted_text = ""
        for char in text:
            # Find position in abc
            position = abc.index(char)
            # Find char in cipher alphabet
            encrypted_char = cipher_alphabet[position]
            encrypted_text += encrypted_char
        return encrypted_text

    def decipher(self, text):
        abc = "abcdefghijklmnopqrstuvwxyz"
        cipher_alphabet = abc[self.__key:] + abc[:self.__key]
        decrypted_text = ""
        for char in text:
            # Find position in cipher_alphabet
            position = cipher_alphabet.index(char)
            # Find char in abc
            decrypted_char = abc[position]
            decrypted_text += decrypted_char
        return decrypted_text    

    # Define Property
    @property
    def my_key(self):
        # Getter for hidden key is not implemented
        raise NotImplemented
    
    # Implement setter for property
    @my_key.setter
    def my_key(self, key):
        self.__key = key
    
def test_shift_cipher():
    # Create Instance with key = 22
    cipher = ShiftCipher(22)
    # Change/Set key to 3
    cipher.my_key = 3

    # Try to use the getter
    try:
        secret_key = cipher.my_key
        print(f"The secret key is {secret_key}")
    except:
        print(f"Access via getter denied!")
        # Accessing hidden variable
        print(f"Secret key still found as {cipher._ShiftCipher__key=}\n")

    # Test encryption and decryption with three different messages
    for msg in ["hallowelt", "hallo welt", "strenggeheim"]:
        try:
            encrypted_msg = cipher.encipher(msg)
            decrypted_msg = cipher.decipher(encrypted_msg)
            print(f"{msg=} => {encrypted_msg=} => {decrypted_msg=}\n")
        except:
            print(f"Exception raised for {msg=}\n")

if __name__ == "__main__":
    test_shift_cipher()
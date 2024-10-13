class CaesarCipher:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def encrypt(plain_text, shift_key):
        plain_text = plain_text.lower()
        cipher_text = ""
        for char in plain_text:
            char_position = CaesarCipher.ALPHABET.index(char)
            key_val = (shift_key + char_position) % 26
            replace_val = CaesarCipher.ALPHABET[key_val]
            cipher_text += replace_val
        return cipher_text

    @staticmethod
    def decrypt(cipher_text, shift_key):
        cipher_text = cipher_text.lower()
        plain_text = ""
        for char in cipher_text:
            char_position = CaesarCipher.ALPHABET.index(char)
            key_val = (char_position - shift_key) % 26
            if key_val < 0:
                key_val += len(CaesarCipher.ALPHABET)
            replace_val = CaesarCipher.ALPHABET[key_val]
            plain_text += replace_val
        return plain_text

if __name__ == "__main__":
    message = input("Enter the String for Encryption: ")
    encrypted_message = CaesarCipher.encrypt(message, 3)
    print("the encrypted message is --> ",encrypted_message)
    print("the decrypted text is --> ",CaesarCipher.decrypt(encrypted_message, 3))


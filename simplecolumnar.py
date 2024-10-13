import numpy as np

class SimpleColumn:
    @staticmethod
    def main():
        message = input("\nEnter plaintext(enter in lower case): ")
        key = input("\nEnter key in numbers: ")
        column_count = len(key)
        row_count = (len(message) + column_count) // column_count
        plain_text = np.zeros((row_count, column_count), dtype=int)
        cipher_text = np.zeros((row_count, column_count), dtype=int)
        
        print("\n-----Encryption-----\n")
        cipher_text = SimpleColumn.encrypt(plain_text, cipher_text, message, row_count, column_count, key)
        ct = ""
        for i in range(column_count):
            for j in range(row_count):
                if cipher_text[j][i] == 0:
                    ct += 'x'
                else:
                    ct += chr(cipher_text[j][i])
        print("\nCipher Text: " + ct)
        print("\n\n\n-----Decryption-----\n")
        plain_text = SimpleColumn.decrypt(plain_text, cipher_text, ct, row_count, column_count, key)
        pt = ""
        for i in range(row_count):
            for j in range(column_count):
                if plain_text[i][j] == 0:
                    pt += ""
                else:
                    pt += chr(plain_text[i][j])
        print("\nPlain Text: " + pt)
        print()

    @staticmethod
    def encrypt(plain_text, cipher_text, message, row_count, column_count, key):
        k = 0
        for i in range(row_count):
            for j in range(column_count):
                if k < len(message):
                    plain_text[i][j] = ord(message[k])
                    k += 1
                else:
                    break
        for i in range(column_count):
            current_col = int(key[i]) - 1
            for j in range(row_count):
                cipher_text[j][i] = plain_text[j][current_col]
        print("Cipher Array(read column by column): \n")
        for i in range(row_count):
            for j in range(column_count):
                print(chr(cipher_text[i][j]), end="\t")
            print()
        return cipher_text

    @staticmethod
    def decrypt(plain_text, cipher_text, message, row_count, column_count, key):
        for i in range(column_count):
            current_col = int(key[i]) - 1
            for j in range(row_count):
                plain_text[j][current_col] = cipher_text[j][i]
        print("Plain Array(read row by row): \n")
        for i in range(row_count):
            for j in range(column_count):
                print(chr(plain_text[i][j]), end="\t")
            print()
        return plain_text

if __name__ == "__main__":
    SimpleColumn.main()


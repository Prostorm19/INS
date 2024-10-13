class RailFenceCipher:

    @staticmethod
    def main():
        try:
            rf = RailFenceBasic()
            plain_text = input("Enter plain Text : ")
            depth = int(input("Enter number of rails to use : "))
            cipher_text = rf.encryption(plain_text, depth)
            print("Encrypted Text is:\n" + cipher_text)
            decrypted_text = rf.decryption(cipher_text, depth)
            print("Decrypted Text is:\n" + decrypted_text)
        except Exception as e:
            pass

class RailFenceBasic:
    def encryption(self, plain_text, depth):
        r = depth
        length = len(plain_text)
        c = length // depth + (1 if length % depth != 0 else 0)
        mat = [['X' for _ in range(c)] for _ in range(r)]
        k = 0
        cipher_text = ""
        
        for i in range(c):
            for j in range(r):
                if k != length:
                    mat[j][i] = plain_text[k]
                    k += 1
        
        for i in range(r):
            for j in range(c):
                cipher_text += mat[i][j]
        
        return cipher_text

    def decryption(self, cipher_text, depth):
        r = depth
        length = len(cipher_text)
        c = length // depth
        mat = [['' for _ in range(c)] for _ in range(r)]
        k = 0
        plain_text = ""
        
        for i in range(r):
            for j in range(c):
                mat[i][j] = cipher_text[k]
                k += 1
        
        for i in range(c):
            for j in range(r):
                plain_text += mat[j][i]
        
        return plain_text

if __name__ == "__main__":
    RailFenceCipher.main()


p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ch = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

def do_encryption(s):
    c = [''] * len(s)
    for i in range(len(s)):
        for j in range(26):
            if p[j] == s[i]:
                c[i] = ch[j]
                break
    return ''.join(c)

def do_decryption(s):
    p1 = [''] * len(s)
    for i in range(len(s)):
        for j in range(26):
            if ch[j] == s[i]:
                p1[i] = p[j]
                break
    return ''.join(p1)

if __name__ == "__main__":
    en = do_encryption(input("Enter a Message: ").lower())
    print("Encrypted Message: " + en)
    print("Decrypted Message: " + do_decryption(en))


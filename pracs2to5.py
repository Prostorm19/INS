# # Prac 2a
# pip install pycryptodome pycrypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
msg = 'SIES Nerul'
b = bytes(msg, 'utf-8')
b = msg.encode('utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(b)
print("Encrypted:", binascii.hexlify(encrypted))

# # Prac 2b
import math
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)
while (e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
k = 2
d = (1 + (k*phi))/e
msg = 12.0
print("Message data = ", msg)
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)


# # Method 2
import random
import math
prime = set()
public_key = None
private_key = None
n = None
def primefiller():
    seive = [True] * 250
    seive[0] = False
    seive[1] = False
    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            seive[j] = False
    for i in range(len(seive)):
        if seive[i]:
            prime.add(i)
def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)
    ret = next(it)
    prime.remove(ret)
    return ret
def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime()
    prime2 = pickrandomprime()
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
    public_key = e
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
    private_key = d
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text

def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted

def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s

primefiller()
setkeys()
message = "Test Message"
coded = encoder(message)
print("Initial message:")
print(message)
print("\n\nThe encoded message(encrypted by public key)\n")
print(''.join(str(p) for p in coded))
print("\n\nThe decoded message(decrypted by public key)\n")
print(''.join(str(p) for p in decoder(coded)))

# Prac 3
# MD5 Algorithm
import hashlib
result = hashlib.md5(b'NetworkSecurity')
result1 = hashlib.md5(b'NetworkSecuriti')
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())

# SHA algorithm
import hashlib
str = input(" Enter the value to encode ")
result = hashlib.sha1(str.encode())
print("The hexadecima equivalent if SHA1 is : ")
print(result.hexdigest())

# # Prac4(not working)
# # pip install pycryptodome
# from Crypto.PublicKey import RSA
# from Crypto.Signature import pkcs1_15
# from Crypto.Hash import SHA256
# key = RSA.generate(2048)
# private_key = key.export_key()
# public_key = key.publickey().export_key()
# original_document = b"This is the original document content."
# modified_document = b"This is the modified document content."
# original_hash = SHA256.new(original_document)
# modified_hash = SHA256.new(modified_document)
# signature = pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)
# try:
#     pkcs1_15.new(RSA.import_key(public_key)).verify(modified_hash, signature)
#     print("Signature is valid.")
# except (ValueError, TypeError):
#     print("Signature is invalid.")

# Prac 5
from random import randint
P = 23
G = 9
print('The Value of P is :%d'%(P))
print('The Value of G is :%d'%(G))
a = 4
print('Secret Number for Alice is :%d'%(a))
x = int(pow(G,a,P))
b = 6
print('Secret Number for Bob is :%d'%(b))
y = int(pow(G,b,P))
ka = int(pow(y,a,P))
kb = int(pow(x,b,P))
print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))
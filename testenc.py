from Crypto.Cipher import AES
import hashlib

password = 'kitty'
key = hashlib.sha256(password).digest()

IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = "Pas"
ciphertext = encryptor.encrypt(text)
print(ciphertext)



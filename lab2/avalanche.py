'''
Modes of Operation: Image Encryption
'''

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(16)

# Plaintext data (Hex)
data = bytes.fromhex('100102030405060708090A0B0C0D0E0F')
print('Plaintext: ', data.hex())

# Initialize Cipher with key and mode.
cipher = Cipher(algorithms.AES(key), modes.ECB())


# Only encrypt the file body
encryptor = cipher.encryptor()
ct = encryptor.update(data) + encryptor.finalize()

print('Ciphertext: ', ct.hex())

# Decryption
decryptor = cipher.decryptor()
decrypted = decryptor.update(ct) + decryptor.finalize()

print('Decrypted Plaintext: ', decrypted.hex())

'''
Modes of Operation: Image Encryption
'''

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(16)

# Plaintext data (Hex)
data1 = bytes.fromhex('100102030405060708090A0B0C0D0E0F')
data2 = bytes.fromhex('000102030405060708090A0B0C0D0E0F')

# Initialize Cipher with key and mode.
cipher = Cipher(algorithms.AES(key), modes.ECB())

# Encryption
encryptor = cipher.encryptor()
ct1 = encryptor.update(data1)
ct2 = encryptor.update(data2) + encryptor.finalize()

print('Ciphertext (1): ', ct1.hex())
print('Ciphertext (2): ', ct2.hex())

# Decryption
decryptor = cipher.decryptor()
decrypted1 = decryptor.update(ct1)
decrypted2 = decryptor.update(ct2) + decryptor.finalize()

print('Decrypted Plaintext: ', decrypted1.hex())

print('Decrypted Plaintext: ', decrypted2.hex())

# Counting the bit differences between ct1 & ct2 (It should be close to 50%)
diffCount = bin(int(ct1.hex(), 16) ^ int(ct2.hex(), 16)).count('1')
print('Percentage of bit change due to avalanche = ',
      str(diffCount*100/128), ' %')

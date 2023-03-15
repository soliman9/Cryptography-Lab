'''
Modes of Operation: Error Propagation
'''

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


key = os.urandom(32)
iv = os.urandom(16)

with open('plain.txt', 'rb') as f:
    plain = f.read()

# cipher = Cipher(algorithms.AES(key), modes.ECB())
# cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
# cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
cipher = Cipher(algorithms.AES(key), modes.OFB(iv))
encryptor = cipher.encryptor()


padder = padding.PKCS7(128).padder()
padded_data = padder.update(plain)
padded_data += padder.finalize()

ct = encryptor.update(padded_data) + encryptor.finalize()

# Write encrypted file
with open('cipher.bin', 'wb') as f:
    f.write(ct)

# Add Error in one byte
error = ct[:20] + (ct[20] + 1).to_bytes(1, 'big') + ct[21:]
print(ct[20].to_bytes(1, 'big').hex())
print((ct[20] + 1).to_bytes(1, 'big').hex())

# Decryption
decryptor = cipher.decryptor()
decrypted = decryptor.update(error) + decryptor.finalize()


with open('dec_out.txt', 'wb') as f:
    f.write(decrypted)

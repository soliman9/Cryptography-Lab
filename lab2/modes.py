'''
Modes of Operation: Image Encryption
'''

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(32)
iv = os.urandom(16)  # Not used in ECB mode.

with open('image.bmp', 'rb') as f:
    image = f.read()

# split the bmp file header and body
header = image[:54]
body = image[54:]

# Initialize Cipher with key and mode.
cipher = Cipher(algorithms.AES(key), modes.ECB())
# cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
# cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
# cipher = Cipher(algorithms.AES(key), modes.OFB(iv))

# Only encrypt the file body
encryptor = cipher.encryptor()
ct = encryptor.update(body) + encryptor.finalize()

# Write encrypted file
with open('out4.bmp', 'wb') as f:
    f.write(header + ct)  # Append the original header to the ciphertext.

# Decryption
decryptor = cipher.decryptor()
decrypted = decryptor.update(ct) + decryptor.finalize()

with open('dec_out.bmp', 'wb') as f:
    f.write(header + decrypted)

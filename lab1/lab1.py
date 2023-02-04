''' Cryptography-CIE 582 
======================================================================
Lab 1
======================================================================
Lab Description:
    In this lab, we are going to implement a random-key mono-alphabetic 
    classic substitution cipher. For simplicity, the cipher will keep
    spaces, commas, numbers, and special characters unchanged.

Lab Objectives:
    * Know how to implement a mono-alphabetic classic substitution 
        cipher using Python.
    * Analyze the frequency of english letters in ciphertext.

Self-practice:
    * Write a script to decrypt a ciphertext given a key.
    * Perform letters frequency analysis attack to a given ciphertext only.
References:
    https://www.sciencedirect.com/topics/computer-science/substitution-cipher

@author Ahmed Soliman [ahsoliman@zewailcity.edu.eg]
'''

import random
from string import ascii_lowercase


# Key generation
#alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = ascii_lowercase
keyList = random.sample(alphabet, len(alphabet))

# This is needed for display only (not part of encryption)
key = ''.join(keyList)
print(alphabet)
print(key)

# Map plaintext letter  to ciphertext letter
keyMap = dict(zip(list(alphabet), keyList))
#print(keyMap)  # Uncomment this to print the plaintext/ciphertext map

# Read plaintext file
with open('plaintext.txt', 'r') as file:
    plaintext = file.read().lower()

# Encrypt text
ciphertext = "".join(keyMap.get(letter, letter) for letter in plaintext)

# Write ciphertext to file
with open('ciphertext.txt', 'w') as file:
    file.write(ciphertext)

# Letter frequency analysis
lettersFreq = {}
for c in ascii_lowercase:
    lettersFreq[c] = ciphertext.count(c)

#print(lettersFreq)
lettersFreqSorted = dict(
    sorted(lettersFreq.items(), key=lambda item: item[1], reverse=True)
)
print(lettersFreqSorted)

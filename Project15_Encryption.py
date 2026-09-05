from random import shuffle
import random 
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

charslist = list(chars)

key = charslist.copy()

random.shuffle(key)

#Encryption

plain_text = input("Choose a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"Your encrypted message: {cipher_text}")
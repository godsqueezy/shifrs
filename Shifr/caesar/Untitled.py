#!/usr/bin/env python
# coding: utf-8

# In[8]:


import string

text = "BAIDIN"
shift = 3
text = text.lower()

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)

encrypted = text.translate(table)

print('Алфавит')
print(alphabet.upper())
print('Сдвигаем алфавит на 3')
print(shifted.upper())
print()
print('Текст для шифровки', text.upper())
print('Шифрованный текст', encrypted.upper())


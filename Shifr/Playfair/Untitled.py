#!/usr/bin/env python
# coding: utf-8

# Чтобы составить ключевую матрицу, в первую очередь нужно заполнить пустые ячейки матрицы буквами ключевого слова (не записывая повторяющиеся символы), потом заполнить оставшиеся ячейки матрицы символами алфавита, не встречающимися в ключевом слове, по порядку (заменяя «J» на «I»).

# Если два символа биграммы совпадают (или если остался один символ), добавляем после первого символа «Х», зашифровываем новую пару символов и продолжаем.
# 
# Если символы биграммы исходного текста встречаются в одной строке, то эти символы замещаются на символы, расположенные в ближайших столбцах справа от соответствующих символов. Если символ является последним в строке, то он заменяется на первый символ этой же строки.
# 
# Если символы биграммы исходного текста встречаются в одном столбце, то они преобразуются в символы того же столбца, находящиеся непосредственно под ними. Если символ является нижним в столбце, то он заменяется на первый символ этого же столбца.
# 
# Если символы биграммы исходного текста находятся в разных столбцах и разных строках, то они заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам прямоугольника.

# In[1]:


import numpy as np


# In[3]:


# Key generator function (based on keyword)
# Function to generate the 5x5 matrix used as key in this algorithm
def generate_key(keyword):
  keyword = keyword.upper()
  keyword = keyword.replace(' ', '')
  keyword = keyword.replace('J', 'I')
  alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
  key = np.array([
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
  ])
  index = 0
  for letter in keyword:
    if letter in alphabet:
      key[index // 5, index % 5] = letter
      alphabet = alphabet.replace(letter, '')
      index += 1
  for letter in alphabet:
    key[index // 5, index % 5] = letter
    index += 1
  return key


# In[5]:


#Encrypy function
#Function to encrypt a given message using a given key with the playfair algorithm
def encrypt(message, key):
  message = message.upper()
  message = message.replace(' ', '')
  message = message.replace('J', 'I')
  for index in range(0, len(message), 2):
    if message[index] == message[index + 1]:
      message = message[:index + 1] + 'X' + message[index + 1:]
  if len(message) % 2 == 1:
    message = message + 'X'
  result = ''
  for index in range(0, len(message), 2):
    index0 = np.where(key == message[index])
    index1 = np.where(key == message[index + 1])
    if index0[0][0] == index1[0][0]:
      result = result + key[index0[0][0], (index0[1][0] + 1) % 5] + key[index1[0][0], (index1[1][0] + 1) % 5]
    elif index0[1][0] == index1[1][0]:
      result = result + key[(index0[0][0] + 1) % 5, index0[1][0]] + key[(index1[0][0] + 1) % 5, index1[1][0]]
    else:
      result = result + key[index0[0][0], index1[1][0]] + key[index1[0][0], index0[1][0]]  
  return result


# In[7]:


#Decrypt function
#Function to decrypt a given covered message using a given key with the playfair algorithm
def decrypt(message, key):
  result = ''
  for index in range(0, len(message), 2):
    index0 = np.where(key == message[index])
    index1 = np.where(key == message[index + 1])
    if index0[0][0] == index1[0][0]:
      result = result + key[index0[0][0], (index0[1][0] + 4) % 5] + key[index1[0][0], (index1[1][0] + 4) % 5]
    elif index0[1][0] == index1[1][0]:
      result = result + key[(index0[0][0] + 4) % 5, index0[1][0]] + key[(index1[0][0] + 4) % 5, index1[1][0]]
    else:
      result = result + key[index0[0][0], index1[1][0]] + key[index1[0][0], index0[1][0]]  
  return result


# In[8]:


#Playfair function
def playfair(message, key, decrypt_mode=True):
  if decrypt_mode:
    return decrypt(message, key)
  else:
    return encrypt(message, key)


# In[22]:


# Generate playfair key using keyword 'CRYPTOGRAPHY'
key = generate_key('VLADISLAVARTUROVICH')
print("Ключ: \n", key)

# Define the message to encrypt using this algorithm
message = 'BAIDIN' 
print("Текст для шифра: \n", message)

# Cipher the message using the playfair algorithm
ciphertext = playfair(message, key, decrypt_mode=False)
print("Шифрованный текст: \n", ciphertext)

# Recover the original message using the playfair algorithm (undebugged message)
recovered_message = playfair(ciphertext, key, decrypt_mode=True)
print("Дешефрованный текст: \n", recovered_message)


#!/usr/bin/env python
# coding: utf-8

# Если $${\displaystyle n}$$  — количество букв в алфавите, $${\displaystyle m_{j}} $$— номер буквы открытого текста,  $${\displaystyle k_{j}}$$ — номер буквы ключа в алфавите, то шифрование Виженера можно записать следующим образом:
# 
# $${\displaystyle c_{j}=(m_{j}+k_{j})\mod {n}}$$
# 
# И расшифровывание:
# 
# $${\displaystyle m_{j}=(c_{j}-k_{j})\mod {n}}$$

# In[41]:


def vigenere_cipher_encrypt(text, key):
    
    t = list(text)
    key = list(key) 

# Checking the length of key and text are equal or not 

    if len(text) == len(key):
        key = key
    else:
        subtraction =  len(text) - len(key)
        for i in range(subtraction):
            h = key[i % len(key)]
            key.append(h)

  
    textt=[]
    
    k = key
    print('Преобразованный ключ: ', *k)
    for i in range(len(t)):

      #Encrypting uppercase characters
      if (t[i].isupper()):
         m = chr(((ord(t[i]) - 65 ) + (ord(k[i]) - 65)) % 26 + ord('A'))      
         textt.append(m)

      # Encrypting lowercase characters
      elif (t[i].islower()):
          m =  chr(((ord(t[i]) - 97 ) + (ord(k[i]) - 97)) % 26 + ord('a'))   
          textt.append(m)

      # Checking empty list index 
      else:
        textt.append(" ")

    texttt =""
    return (texttt.join(textt))
 


#checking the vigenere_cipher_encrypt function  
vigenere_text = input("Текст для шифрования : ")
vigenere_key = input("Ключ : ")


print ("Шифрованный текст : ", vigenere_cipher_encrypt(vigenere_text, vigenere_key))


# In[42]:


# Python codes for Vigenere Cipher decryption

def vigenere_cipher_decrypt(text, key):

   
    t = list(text)
    key = list(key) 

# Checking the length of key and text are equal or not 

    if len(text) == len(key):
        key = key
    else:
        subtraction =  len(text) - len(key)
        for i in range(subtraction):
            h = key[i % len(key)]
            key.append(h)

  
    textt=[]
      
    k = key

    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
           m = chr(((ord(t[i]) - 65 ) - (ord(k[i]) - 65)) % 26 + ord('A'))  
           textt.append(m)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          m =  chr(((ord(t[i]) - 97 ) - (ord(k[i]) - 97)) % 26 + ord('a')) 
          textt.append(m)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))

decryption = vigenere_cipher_encrypt(vigenere_text, vigenere_key)

print ("Дешифрованный текст : ", vigenere_cipher_decrypt(decryption, vigenere_key))


# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
# 
# B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 
# C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
# 
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
# 
# E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
# 
# F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
# 
# G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
# 
# H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
# 
# I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
# 
# J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
# 
# K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
# 
# L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
# 
# M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
# 
# N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
# 
# O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
# 
# P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
# 
# Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
# 
# R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
# 
# S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
# 
# T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
# 
# U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
# 
# V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
# 
# W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
# 
# X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
# 
# Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
# 
# Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

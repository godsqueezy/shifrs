#!/usr/bin/env python
# coding: utf-8

# In[16]:


def vigenere_cipher_encrypt(text, key):
    
    t = list(text)
    key = list(key) 

# Checking the length of key and text are equal or not 

    if len(text) == len(key):
        key = key
    else:
        subtraction =  len(text) - len(key)
        for i in range(subtraction):
            h = t[i % len(key)]
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


# In[14]:


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
            h = t[i % len(key)]
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

decryption = 'WLIGQFGLVDZLFRJVZVB'
print ("Дешифрованный текст : ", vigenere_cipher_decrypt(decryption, 'BAIDINVLADISLAVARTU'))


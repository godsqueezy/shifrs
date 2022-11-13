#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
from hill_cipher import *
from egcd import egcd
init_printing(use_latex='mathjax')


# In[2]:


K = np.array([[4, 18, 5], [10, 11, 19], [25, 5, 23]])
print('Ключевая матрица')
K


# In[3]:


message = "VLADISLAV"


# In[4]:


show_encoding()


# In[5]:


numbers = char2num(message)
numbers


# In[6]:


print('Разбиваем VLADISLAV на вектора')
v1 = np.array(numbers[:3])  # a vector consisting of the first 3 entries of the list
v2 = np.array(numbers[3:6]) # a vector consisting of the next 3 entries of the list
v3 = np.array(numbers[6:]) # and so on...
v1, v2, v3


# In[7]:


print('Перемножаем Ключевую матрицу с векторами слова VLADISLAV по модулю 27')
w1 = np.matmul(K, v1) % 27
w2 = np.matmul(K, v2) % 27
w3 = np.matmul(K, v3) % 27
w1, w2, w3


# In[8]:


print('Переводим значение цифер в буквы')
num2char([12, 20, 12, 3, 14, 15, 14, 9, 1])


# In[9]:


det = int(np.round(np.linalg.det(K)))
det_inv = egcd(det, 27)[1] % 27
print('Находим определитель матрицы по модулю 27')
det_inv


# In[10]:


matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(K)).astype(int) % 27
    )
print('Находим обратную матрицу, умножая определитель матрицы на матрицу алгб. дополнений по модулю 27')
matrix_modulus_inv


# In[11]:


decrypt1 = np.matmul(matrix_modulus_inv, w1) % 27
decrypt2 = np.matmul(matrix_modulus_inv, w2) % 27
decrypt3 = np.matmul(matrix_modulus_inv, w3) % 27
print('Перемножаем обратную матрицу с векторами зашифровоного слова')
decrypt1, decrypt2, decrypt3


# In[12]:


print('Переводим значение цифер в буквы из полученных векторов')
num2char([22, 12, 1, 4, 9, 19, 12, 1, 22])


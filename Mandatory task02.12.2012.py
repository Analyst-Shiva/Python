#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a program to create a 5 dimensional array with all zeros and ones


import numpy as np

array_zeros = np.zeros((2, 3, 4, 5, 6), dtype=int)
array_ones = np.ones((2, 3, 4, 5, 6), dtype=int)

print("Array of Zeros:")
print(array_zeros)

print("\nArray of Ones:")
print(array_ones)


# In[2]:


#2) Write a program to create an array of 10 zeros,10 ones, and 10 fives in row 1 2 and 3 which create a new array of shape (3,10)


import numpy as np

array = np.array([0] * 10 + [1] * 10 + [5] * 10).reshape(3, 10)

print(array)


# In[3]:


#3) Write a program to create a 3x4 matrix filled with values from 10 to 21.

import numpy as np

matrix = np.arange(10, 22).reshape(3, 4)

print(matrix)


# In[4]:


#4) Write a program to create a 10x10 zero matrix with elements on the main diagonal equal to 0,1,2,3,4,5,6,7,8,9,


import numpy as np

matrix = np.zeros((10, 10), dtype=int)
np.fill_diagonal(matrix, np.arange(10))

print(matrix)


# In[5]:


#5)Write a program to create a 4x4 array. Create an array from below array by swapping first and last, second and third columns.

import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

array[:, [0, 3]] = array[:, [3, 0]]
array[:, [1, 2]] = array[:, [2, 1]]

print(array)


# In[6]:


#6) Write a program to reverse an array (the first element becomes the last). Given array: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ]


import numpy as np

given_array = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
reversed_array = np.flip(given_array)

print(reversed_array)


# In[7]:


#7) Write a program to access all the elements greater than 30 and less than 80 and multiples of 5 from an array of shape 10,10 .Elements range from 1 to 100

import numpy as np

array = np.arange(1, 101).reshape(10, 10)
result = array[(array > 30) & (array < 80) & (array % 5 == 0)]

print(result)


# In[8]:


#8) Write a program to create a 2D array with 1 on the border and 0 inside.
import numpy as np

array = np.ones((5, 5), dtype=int)
array[1:-1, 1:-1] = 0

print(array)


# In[9]:


#9) Write a program to create a checkerboard pattern .Don't use default array function. Checkerboard pattern:

import numpy as np

size = 8
checkerboard = np.zeros((size, size), dtype=int)

checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1

print(checkerboard)


# In[ ]:





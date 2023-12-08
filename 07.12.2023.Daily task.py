#!/usr/bin/env python
# coding: utf-8

# In[2]:


#lexsort
import numpy as np

arr1 = np.array([3, 1, 2, 4])
arr2 = np.array(['a', 'b', 'c', 'd'])

sorted_indices = np.lexsort((arr2, arr1))

print(sorted_indices)



# In[5]:


#Sample 1

import numpy as np

x = np.array([0, np.pi/2, np.pi])

result = np.sin(x)


# In[7]:


#Braodcasting

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2


# In[8]:


#sample 2

import numpy as np

# Example using NumPy broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2

print(result)


# In[9]:


#Vectorisation

import numpy as np

# Non-vectorized approach
def non_vectorized_addition(a, b):
    result = []
    for ai, bi in zip(a, b):
        result.append(ai + bi)
    return result

# Vectorized approach
def vectorized_addition(a, b):
    return np.array(a) + np.array(b)

# Example data
array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]

# Non-vectorized addition
result_non_vectorized = non_vectorized_addition(array1, array2)
print("Non-vectorized result:", result_non_vectorized)

# Vectorized addition
result_vectorized = vectorized_addition(array1, array2)
print("Vectorized result:", result_vectorized)


# In[10]:


#sample2

import numpy as np

# Non-vectorized approach
def non_vectorized_addition(a, b):
    result = []
    for ai, bi in zip(a, b):
        result.append(ai + bi)
    return result

# Vectorized approach
def vectorized_addition(a, b):
    return np.array(a) + np.array(b)

# Example data
array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]

# Non-vectorized addition
result_non_vectorized = non_vectorized_addition(array1, array2)

# Vectorized addition
result_vectorized = vectorized_addition(array1, array2)


# In[29]:


#Asssigment

x=np.genfromtxt(r'C:\Users\user\Downloads\train_extended.csv',delimiter = ',', skip_header = 1)
x


# In[30]:


np.shape(x)


# In[36]:


length=x[:,0]
np.min(length)


# In[37]:


length=x[:,0]
np.max(length)


# In[38]:


weight=x[:,3]
np.average(x)


# In[48]:


high_avg=x[:,3]

np.average(high_avg)


# In[49]:


def row_height(x):
    if float(x[:2]) > 0.4:
        return "row_height"

example_value = ""  # Replace with your actual value
result = row_height(example_value)

if result:
    print(result)


# In[50]:


shell_weight=x[:,6]
np.sum(shell_weight)


# numpy.lexsort(keys, axis=-1)
# keys: A sequence of arrays that are used to determine the order of the sort. The last array in the sequence is the primary key.
# 
# axis: Axis along which to sort. Default is -1, which means the last axis.
# 
# Example:
# python
# Copy code
# import numpy as np
# 
# -# Creating a sample array
# arr = np.array([[3, 1, 4],
#                 [2, 0, 5],
#                 [1, 2, 6]])
# 
# -# Using lexsort to get indices for sorting
# indices = np.lexsort((arr[:, 0], arr[:, 1]))
# 
# -# Reconstructing the sorted array
# sorted_arr = arr[indices]
# 
# print("Original array:")
# print(arr)
# print("\nSorted array:")
# print(sorted_arr)
# In this example, np.lexsort((arr[:, 0], arr[:, 1])) sorts the array first by the second column (arr[:, 1]) and then by the first column (arr[:, 0]). The resulting indices array can be used to obtain the sorted array.
# 
# Keep in mind that lexsort performs an indirect sort, meaning it returns an array of indices rather than sorting the original array in place. You can then use these indices to construct the sorted array or rearrange other associated data.

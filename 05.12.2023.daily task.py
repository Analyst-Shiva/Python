#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sample 1 . np.min

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

min_value = np.min(arr)
print("Minimum value in the entire array:", min_value)

min_values_along_columns = np.min(arr, axis=0)
print("Minimum values along columns:", min_values_along_columns)

min_values_along_rows = np.min(arr, axis=1)
print("Minimum values along rows:", min_values_along_rows)


# In[3]:


x=np.random.randint(-10,10),(4,3)
x


# In[5]:


import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Find the minimum value along columns (axis=0)
min_values_along_columns = np.min(arr, axis=0)
print("Minimum values along columns:", min_values_along_columns)


# In[6]:


np.min(arr,axis=1)


# In[7]:


np.max(arr,axis=1)


# In[8]:


np.min(arr,axis=0)


# In[9]:


np.max(arr,axis=0)


# In[10]:


#np.argmin

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 1, 6],
                [7, 8, 1]])

min_index = np.argmin(arr)
print("Index of the minimum value in the entire array:", min_index)

min_indices_along_columns = np.argmin(arr, axis=0)
print("Indices of minimum values along columns:", min_indices_along_columns)


min_indices_along_rows = np.argmin(arr, axis=1)
print("Indices of minimum values along rows:", min_indices_along_rows)


# In[13]:


#3d matrix and use random

x= np.random.randint(-24,24,(2,3,4))
x


# In[14]:


np.min(x,axis=0)


# In[15]:


np.max(x,axis=0)


# In[16]:


np.min(x,axis=1)


# In[17]:


np.max(x,axis=1)


# In[19]:


x= np.random.randint(-120,120,(2,3,4,5))
x.shape


# In[20]:


np.min(x)


# In[21]:


np.max(x)


# In[22]:


np.min(x,axis=0).shape


# In[23]:


np.min(x,axis=1).shape


# In[24]:


np.max(x,axis=1).shape


# In[25]:


np.min(x,axis=-1)


# In[27]:


#Mean

x=np.random.randint(1,100,5)
x


# In[28]:


np.mean(x)


# In[34]:


x=np.random.randint(1,100,(3,3))
x


# In[36]:


np.mean(x),np.mean(x,axis=0),np.mean(x,axis=1)


# In[39]:


np.median(x)


# In[43]:


#Mode

import numpy as np

def calculate_mode(data):
    unique_elements, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)

    mode_value = unique_elements[max_count_index]
    return mode_value

# Example usage
data = np.array([2,2,2,2,2,2,2,2,3])
result = calculate_mode(data)

print("Mode:", result)


# In[44]:


#np.unique

x= np.random.randint(1,5,15)
x


# In[45]:


np.unique(x,return_counts=True)


# In[51]:


#Unique and mode

import numpy as np

def calculate_mode(data):
    unique_elements, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)

    mode_value = unique_elements[max_count_index]
    return mode_value

# Example usage
data = np.array([2,2,2,2,2,2,2,2,3])
result = calculate_mode(data)

print("Mode:", result)
np.unique(x,return_index=True, return_counts=True)


# In[47]:


#np.unique

x= np.random.randint(1,5,15)
x


# In[52]:


#np.std and varriance

np.std


# In[53]:


x= np.random.randint(1,5,15)
x


# In[55]:


np.unique(x,return_counts=True)
np.std


# In[56]:


#np.std

import numpy as np

data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6])

std_deviation = np.std(data)

print("Standard Deviation:", std_deviation)


# In[58]:


#sorting - ascending or descending

x=np.random.randint(1,100,(3,4))
x


# In[59]:


np.sort(x)


# In[61]:


np.sort(x,axis=0)


# In[62]:


x=np.random.randint(1,100,(3,4,5))
x


# In[63]:


np.sort(x,axis=0)


# In[64]:


np.sort(x,axis=1)


# In[65]:


np.sort(x,axis=-1)


# In[67]:


np.sort(x,axis=-2)


# In[69]:


#Mean,Median and Mode in Numphy

import numpy as np
from scipy import stats

# Create a 2D array as a sample dataset
data_2d = np.array([[1, 2, 3, 4],
                    [4, 5, 6, 6],
                    [7, 8, 9, 9]])

# Mean
mean_value = np.mean(data_2d)
print("Mean:", mean_value)

# Median
median_value = np.median(data_2d)
print("Median:", median_value)

# Mode along columns (axis=0)
mode_result_columns = stats.mode(data_2d, axis=0)
print("Mode along columns:", mode_result_columns.mode[0])

# Mode along rows (axis=1)
mode_result_rows = stats.mode(data_2d, axis=1)
print("Mode along rows:", mode_result_rows.mode[0])


# In[70]:


x=np.random.randint(1,5,19)
x


# In[73]:


m=np.unique(x,return_counts=True)
m


# In[75]:


m[1]


# In[83]:


mSorted = list(m[1])

mSorted.sort(reverse=True)
mSorted


# In[84]:


#arg is nothng but the indexed positons

x=np.random.randint(1,5,19)
x


# In[86]:


help(np.lexsort)


# In[89]:


#np.lexsort sample 1

import numpy as np

# Create a sample 2D array
x = np.array([[3, 2, 5],
              [1, 4, 6],
              [2, 9, 1]])

# Use np.lexsort on the first column
sorted_indices = np.lexsort((x[:, 0],))

# Access the sorted array using the sorted indices
sorted_x = x[sorted_indices]

print(sorted_x)


# In[90]:


#Boolean mask

x= np.random.randint(1,10,19)
x



# In[91]:


x>5


# In[92]:


x[x>5]


# In[93]:


x[x>=5]


# In[94]:


x[x<=5]


# In[95]:


help(np.lexsort)


# In[96]:


x%2==0


# In[97]:


[x%2==0 &(x>4)]


# In[98]:


x=np.array([4,5,6,7,8])
print(x%2==0)
print(' &'*4)
print(x>4)
print(x)


# In[100]:


#[F,F,T,F,T]
x[[2,4]]


# In[101]:


x[(x%2==0) & (x>4)]


# In[103]:


x=np.random.randint(1,50,(3,4))
x


# In[106]:


x[np.where(x>5)]


# In[1]:


#Function sample1

def greet(name):
    print(f"Hello, {name}!")

greet("Vijay")
greet("Kate")


# In[7]:


#Class sample1

class Vijay:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value: {self.value}")

# Create instances of the class
instance1 = Vijay(24)
instance2 = Vijay("Hello")

# Call the display method for each instance
instance1.show()
instance2.show()


# In[14]:


#Sample 1 Class with function

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_info(self):
        print(f"Name: {self.name}, Bond: {self.roll_number}")

student1 = Student("The Vijay", "007")
student1.display_info()


# In[15]:


#Create a 2d numpy array.

import numpy as np

array_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])


# In[17]:


#Stacking

#vertical stacking and horizontal stacking

import numpy as np

x, y, z = np.random.randint(1, 100, (5, 5)), np.random.randint(1, 100, (3, 5)), np.random.randint(1, 100, (5, 4))
print(x, y, z, sep='\n\n')


# In[18]:


np.hstack((x,z))


# In[20]:


np.vstack((x,y))


# In[25]:


np.concatenate((z,x), axis=1)


# In[26]:


np.concatenate((y,x), axis=0)


# In[27]:


#Concatenate

import numpy as np

array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

result = np.concatenate((array1, array2), axis=0)

print(result)


# In[28]:


a,b = np.random.randint(1,100,(2,3,3)), np.random.randint(1,100,(3,3,3))

print(a,b, sep='\n\n')


# In[30]:


#Sample 2

import numpy as THE

The = THE.array([[1, 2, 3],
                  [4, 5, 6]])

result = THE.concatenate((The, [[7, 8, 9], [10, 11, 12]]), axis=0)

print(result)


# In[31]:


#Sample 2

import numpy as np

# Create two arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

# Concatenate along axis 0 (rows)
result = np.concatenate((array1, array2), axis=0)

print(result)


# In[33]:


#r__

import numpy as np

# Using r_ to create an array using slicing syntax
result = np.r_[1:5, 7, 10:15]

print(result)


# In[36]:


#Broadcasting

xx=np.arange(1,10).reshape(3,3)
xx


# xx+np.array([1,2,3])

# In[37]:


#Transpose of a mtrix

xx.transpose()


# In[38]:


a


# In[42]:


a.T


# In[43]:


#coloumn transpose

xx.transpose()


# In[46]:


xx+(np.array([1,2,3]).reshape(3,1))


# In[47]:


#Matrix Multiplication

import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

result_dot = np.dot(matrix1, matrix2)
result_at = matrix1 @ matrix2

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication using np.dot:")
print(result_dot)

print("\nMatrix Multiplication using @ operator:")
print(result_at)


# In[52]:


import numpy as np

m, n, o = np.random.randint(1, 9, (3, 3)), np.random.randint(1, 9, (3, 2)), np.random.randint(1, 9, (2, 3))

print(m, n, o, sep='\n\n')


# In[54]:


np.matmul(m,n)


# In[55]:


m


# In[56]:


n


# In[59]:


p=np.eye(3)


# m@p

# In[60]:


2*3


# In[62]:


np.diag(xx)


# In[68]:


for i in xx:
    print('\n')
    for j in i:
        print(j,',')
    print('\n')  


# In[71]:


#create a cvs file using genfromtxt

import numpy as np

data = np.random.randint(1, 9, (3, 3))
csv_file = "example.csv"
np.savetxt(csv_file, data, delimiter=',')
loaded_data = np.genfromtxt(csv_file, delimiter=',')

print("Original Data:")
print(data)

print("\nLoaded Data from CSV:")
print(loaded_data)


# In[74]:


import numpy as np

data = np.array([
    ['Name', 'Age', 'City'],
    ['Vijay', 25, 'New York'],
    ['Kate', 30, 'San Francisco'],
    ['Jlo', 22, 'Los Angeles']
])

file_path = 'example_numpy.csv'

np.savetxt(file_path, data, delimiter=',', fmt='%s')

print(f'CSV file "{file_path}" created successfully.')



# In[76]:


np.genfromtxt(example_numpy.csv)


# In[ ]:



    


# In[ ]:





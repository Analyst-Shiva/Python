#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a function, foo_1, that takes a NumPy array arr and returns the indices of the elements that are closest to a given target. If target is not in the given array, it should return ‘no item found’


# In[5]:


import numpy as np
arr = np.array([3, 8, 7, 7, 7, 7, 7, 8, 7, 10])
target = int(input('enter a number:'))
differences = np.abs(arr - target)
indices = np.argsort(differences)

def foo(arr, target):
    if target in arr:
        return indices
    else:
        return 'item not found'

foo(arr, 7)
foo(arr, 22)

arr = np.array([3, 8, 7, 7, 7, 7, 7, 8, 7, 10])
target = int(input('enter a number:'))
differences = np.abs(arr - target)
indices = np.argsort(differences)

foo(arr, 8)
foo(arr, 44)


# In[6]:


#2.Write a user defined function foo_2 that takes a 1 or 2 dim NumPy array arr and returns a new n-1 dim array, where each element is replaced by the count of non-zero elements wrt axis.


# In[12]:


import numpy as np

def foo_2(arr, axis):
    non_zero = np.count_nonzero(arr, axis=axis)
    return non_zero

arr = np.array([[5, 0, 3, 1],
                [0, 4, 0, 0],
                [2, 0, 1, 0]])

result = foo_2(arr, axis=1)
print(result)

arr = np.array([[9, 3, 7, 2],
                [0, 1, 0, 0],
                [8, 0, 5, 0]])

result = foo_2(arr, axis=0)
print(result)

arr1 = np.array([[[1, 0, 3, 4],
                  [7, 8, 0, 0],
                  [2, 4, 1, 6]],

                 [[2, 0, 1, 3],
                  [0, 5, 0, 5],
                  [1, 2, 3, 4]]])

result = foo_2(arr1, axis=0)
print(result)

arr1 = np.array([[[1, 2, 0, 4],
                  [0, 5, 0, 0],
                  [2, 0, 1, 0]],

                 [[2, 0, 1, 0],
                  [0, 5, 0, 0],
                  [1, 2, 3, 4]]])

result = foo_2(arr1, axis=1)
print(result)

arr1 = np.array([[[1, 2, 3, 4],
                  [0, 5, 0, 0],
                  [2, 0, 1, 0]],

                 [[2, 0, 1, 0],
                  [0, 5, 0, 0],
                  [1, 2, 3, 4]]])

result = foo_2(arr1, axis=2)
print(result)


# In[13]:


#3.1 You are given a 2D NumPy array of data representing student scores. Each row represents a student, and each column represents a subject. Extract the scores of all students who scored above 90 in at least one subject. Provide the resulting array.


# In[14]:


import numpy as np

data = np.array([[85, 89, 88],
                 [78, 89, 94],
                 [91, 87, 90],
                 [87, 95, 84]])

above_90_mask = np.any(data > 90, axis=1)
result = data[above_90_mask]

result


# In[15]:


#3.2 You are provided with a 2D NumPy array of data representing sales data for different products. Each row corresponds to a product, and each column represents the monthly sales for a specific month. Calculate the following statistics for each product: mean, median, standard deviation, and the month with the highest sales.


# In[16]:


import numpy as np

sales_data = np.array([[120, 150, 130, 110],
                      [200, 180, 220, 250],
                      [90, 100, 95, 110],
                      [300, 280, 320, 340]])

mean_values = np.mean(sales_data, axis=1)
median_values = np.median(sales_data, axis=1)
standard_deviation_values = np.std(sales_data, axis=1)
best_month_sales = np.argmax(sales_data, axis=1)

for i in range(len(mean_values)):
    print(f"Product {i + 1}:")
    print(f"Mean: {mean_values[i]}")
    print(f"Median: {median_values[i]}")
    print(f"Standard Deviation: {standard_deviation_values[i]}")
    print(f"Month with the highest sales: Month {best_month_sales[i] + 1}")
    print()


# In[17]:


#3.3 Create a NumPy array of size 1000 with random integers between 1 and 100. Then, use NumPy functions to find the top 10 most frequently occurring values in the array.


# In[18]:


import numpy as np

random_array = np.random.randint(1, 101, size=1000)

unique_values, counts = np.unique(random_array, return_counts=True)
sorted_indices = np.argsort(counts)[::-1]

top_values = unique_values[sorted_indices[:10]]
top_counts = counts[sorted_indices[:10]]

print("Top 10 most frequently occurring values:")
for value, count in zip(top_values, top_counts):
    print(f"{value}: {count} occurrences")


# In[ ]:





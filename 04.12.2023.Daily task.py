#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sample

import numpy as np

my_array = np.full((3, 3), 7)
print(my_array)


# In[3]:


#Sample 1

import numpy as np


x = np.arange(1, 37)

reshaped_array = x.reshape((3, 3, 4))


print(reshaped_array)


# In[4]:


#Identity matrix

import numpy as np


identity_matrix = np.eye(3)

print("Identity Matrix:")
print(identity_matrix)


# In[10]:


#linspace

#Syntax:numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)


import numpy as np
arr = np.linspace(0, 1, num=10)

print(arr)


# In[8]:


np.linspace(0,10,4)


# In[9]:


np.linspace(0,10,5)


# In[11]:


x=np.linspace(0,10)
x.size


# In[13]:


#np.repeat

import numpy as np

# Example array
arr = np.array([1, 2,])

repeated_arr = np.repeat(arr, 3)

print(repeated_arr)


# In[15]:


np.repeat(np.arange(1,6),2)


# In[18]:


np.min(np.arange(1,5))


# In[19]:


np.max(np.arange(1,5))


# In[20]:


import numpy as np

# Example array
arr = np.array([5, 2, 8, 1, 7])

index_of_min_value = np.argmin(arr)

print(index_of_min_value)


# In[21]:


np.min(x,axis=0)


# In[22]:


np.max(x,axis=0)


# In[25]:


np.min(x,axis=2)


# In[28]:


#sample

import numpy as np

x = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]],
              [[10, 11, 12],
               [13, 14, 15],
               [16, 17, 18]],
              [[19, 20, 21],
               [22, 23, 24],
               [25, 26, 27]]])
result = np.min(x, axis=2)


# In[ ]:





# In[ ]:





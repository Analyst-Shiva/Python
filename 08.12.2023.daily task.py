#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


plt.imshow(np.zeros((3,3)))


# In[13]:


import numpy as np
import matplotlib.pyplot as plt

# Create a simple 2D array as a grayscale image
image_array = np.array([
    [0, 255, 0, 255],
    [255, 0, 255, 0],
    [0, 255, 0, 255],
    [255, 0, 255, 0]
], dtype=np.uint8)

# Display the image using Matplotlib
plt.imshow(image_array, cmap='gray', vmin=0, vmax=255)
plt.title("Simple Grayscale Image")
plt.show()


# In[27]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Generate some sample 3D data (replace this with your own data)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
x, y = np.meshgrid(x, y)
z = np.random.random((10, 10))

#Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Plot the 3D surface
surf = ax.plot_surface(x, y, z, cmap='viridis')

#Add a colorbar for reference
fig.colorbar(surf)

#Show the plot
plt.show()


# In[28]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Set the text properties
text = 'THE VIJAY'
x, y, z = 0, 0, 0
font_size = 20
font_weight = 'bold'

#Create 3D text
ax.text(x, y, z, text, fontsize=font_size, fontweight=font_weight, va='center', ha='center', color='blue')

#Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

#Set axis labels (optional)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#Show the plot
plt.show()


# In[ ]:





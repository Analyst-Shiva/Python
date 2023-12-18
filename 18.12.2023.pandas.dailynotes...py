#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import numpy as np


# In[121]:


x=pd.DataFrame([pd.date_range('14-10-2023','23-10-2023'),
                         np.random.randint(-100,-1,10),
                         np.random.randint(1,100,10),
                         [chr(ele)for ele in np.random.randint(97,123,10)],
                         [chr(ele)for ele in np.random.randint(65,91,10)]])


# In[122]:


x


# In[123]:


x.T


# In[124]:


X = x.T.copy()


# In[125]:


X


# In[126]:


X.columns = ['col_'+str(ele) for ele in X.columns]
X.index = ['row_'+str(ele) for ele in X.index]
X


# In[127]:


X.T


# In[128]:


X.rename(columns = {'col_0':'date'},
        index = {'row_9':'ninthrow'},
        inplace = True)
X


# In[129]:


X.reset_index(drop = True, inplace = True)
X


# In[130]:


#X.index('date')


# In[131]:


X.set_index('date')


# In[132]:


X.set_index('date',drop = False)


# In[133]:


X.set_index('date')


# In[134]:


X.reset_index(drop= True, inplace = True)
X


# In[135]:


X['col_5'] = np.random.normal(0,1,10)
X


# In[136]:


X.insert( loc = 6, column = 'col_6', value = np.NAN)
X


# In[137]:


X.insert( loc = 0, column = 'subZero', value = np.NAN)
X


# In[146]:


z = pd.DataFrame(np.random.seed(23),
                 np.random.randint(-1000,1000,1000),
                 np.random.normal(0,1,3))
z


# In[148]:


np.random.seed(23)
z = pd.DataFrame({'col1':np.random.randint(-1000,1000,1000),
                 'col2':np.random.randint(-100,100,1000),
                 'col3':np.random.normal(0,1,1000)})
z


# In[149]:


z.tail()


# In[150]:


z.head()


# In[157]:


z.sample()


# In[158]:


z.sample(10)


# In[152]:


z.describe()


# In[153]:


z.describe().T # .describe to use the data in visulization


# In[162]:


help(pd.DataFrame.describe)


# In[167]:


z.describe(percentiles = [ele/100 for ele in range(1,10)]).T


# In[173]:


x = pd.DataFrame([pd.date_range('14-10-2023','23-10-2023'),
                         np.random.randint(-100,-1,10),
                         np.random.randint(1,100,10),
                         [chr(ele)for ele in np.random.randint(97,123,10)],
                         [chr(ele)for ele in np.random.randint(65,91,10)]])
x.T


# In[174]:


x.info()


# In[175]:


x.describe().T


# In[186]:


x['col_5'] = 10
x


# In[188]:


x.describe().T


# In[189]:


x.describe(include = 'all').T


# In[190]:


x.describe(include = ['object','int64']).T


# In[194]:


x['col_6'] = 10
x.T


# In[193]:


x.describe(exclude = 'float64').T


# In[195]:


x[1].dtype


# In[1]:


import numpy as np

x = np.array([1.5, '2', '3.3'])
x = x.astype('float64')
x[1], x[2] = x[1].astype('int64'), x[2].astype('int64')
print(x)


#!/usr/bin/env python
# coding: utf-8

# # Lambda Function
# 
# Syntax:
# 
# Lambda functions are created using the lambda keyword.
# 
# The general syntax is: lambda parameters: code
# 
# Anonymous Functions:Lambda functions are also known as anonymous functions because they don't have a name like regular functions.
# 
# Single Expression:Lambda functions can only have a single expression, and the result of that expression is returned.
# 
# No Statements:Lambda functions can't include statements or annotations, only expressions.
# 
# Conciseness:Lambda functions are often used for short, simple operations where a full function would be overkill.
# 
# Functional Programming:Lambda functions are often used in functional programming constructs like map, filter, and reduce.

# In[2]:


#lambda functions in Python! They're like the mini-versions of regular functions, handy for quick and simple operations. You create them using the lambda keyword, followed by parameters and an expression.

#example: Add

add = lambda x, y: x + y
print(add(3, 5))


# In[18]:


#Substraction

sub = lambda x,y,:x - y
print(sub(2, 8))


# In[19]:


#Multiplication

Mul = lambda x,y,:x*y
print(Mul(2, 8))


# In[21]:


#To check even and odd using lambda

# Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# Lambda function to check if a number is odd
is_odd = lambda x: x % 2 != 0

# Test the lambda functions
print(is_even(4))  # Outputs: True
print(is_odd(7))   # Outputs: True
print(is_even(3))  # Outputs: False
print(is_odd(10))  # Outputs: False


# In[26]:


#To check odd use lambda

x=5
#'Even' is x%2 ==0 else'odd'

check_even_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
result = check_even_odd(5)
print(result)  # Outputs: 'Odd'


# In[28]:


#To check even use lambda

x=5
#'Even' is x%2 ==0 else'odd'

check_even_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
result = check_even_odd(8)
print(result)  # Outputs: 'Odd'


# In[30]:


#Higher order functions

#higher-order functions, the maestros of Python programming! These are functions that can take other functions as arguments or return functions as results. It's like functions playing with other functions in the coding playground.

# Higher-order function example: map
numbers = [1, 2, 3, 4, 5]

# Using map to square each number in the list
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)
# Outputs: [1, 4, 9, 16, 25]


# # map,reduce,filter
# 
# #map
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# 
# Python map() Function
# 
# Syntax:map(fun, iter)
#     
# Parameters:
# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.

# In[33]:


#map exmaple

# Double all numbers using map and lambda 
  
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 


# In[35]:


z= map(lambda x:x/0, [1,2,3] )
z


# In[36]:


list[z]


# In[44]:


z= map(lambda x:x**2, [1,2,3])
z


# In[45]:


list(z)


# In[50]:


#Use typecast

list(map(lambda x,y:x+y,[1,2,3],[10,20,30]))


# In[54]:


list(map(lambda x,y:x**y,[5],[5]))


# In[56]:


#Multiply

z= map(lambda x:x**x,[1,2,3])
list(z)


# In[61]:


#Filter

#Definition and Usage
#The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

#Syntax :filter(function, iterable)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


# In[62]:


#Even using filter

list(filter(lambda x:True if x%2 ==0 else False,[1,2,3,4,5]))


# In[64]:


# Filter to get vowels

'String'

list(filter(lambda x:True if x in 'aeiou' else False,'Vijay'))


# In[69]:


# alphabets and numerics

list(filter(lambda x:True if x in 'ae123' else False,'Vijay123'))


# In[68]:


# special charecters

list(filter(lambda x:True if x in 'aei$%#' else False,'Vijayi$%#'))


# In[70]:


# alphabets and numerics method1

list(filter(lambda x:True if x.isalnum() else False,'1ab$23'))


# In[72]:


# Special cheracters method1

list(filter(lambda x:True if x.isalnum() is False else False,'1ab$23'))


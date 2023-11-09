#!/usr/bin/env python
# coding: utf-8

# In[8]:


#In Python, you can return a function from another function, just like in other programming languages

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Create a function that multiplies by 2
multiply_by_2 = create_multiplier(2)

# Create a function that multiplies by 3
multiply_by_3 = create_multiplier(3)

# Use the returned functions
result1 = multiply_by_2(5)  # result1 is 10
result2 = multiply_by_3(4)  # result2 is 12


# In[1]:


#Simple Function

def add_numbers(a, b):
    result = a + b
    return result

# Call the function
sum_result = add_numbers(5, 3)
print("The sum is:", sum_result)


# # return function sample question
# 
# S='abc123'--> 'the fisrt non alpha char is a spe char,#'
# 
# 
# S='abc123'--> 'the fisrt non alpha char is a numeric,1'

# In[12]:


#sample above question 1 Method1
def first_non_alpha(S):
    for char in S:
        if not char.isalpha():
            return f"the fisrt non alpha char is a spe char,#"
    return "There are no special characters in the string."

S = 'abc123'
result = first_non_alpha(S)
print(result)


# In[11]:


#sample above question 2 Method 1
def first_non_alpha(S):
    for char in S:
        if not char.isalpha():
            return f"the fisrt non alpha char is a numeric,1"
    return "There are no special characters in the string."

S = 'abc123'
result = first_non_alpha(S)
print(result)


# In[32]:


def separate_even_and_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers

# Example usage:
numbers = [7, 2, 9, 4, 5, 6, 7, 8, 9]
even, odd = separate_even_and_odd(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)


# In[52]:


#X = s3$Ab$-> $$3Asb

def Myfucntion(s):
    x=list(s)
    sc,n,u,l='','','',''
    a,b,c,d = [],[],[],[]
    for char in x:
        if char.isnumeric():
            b.append(char) 
        elif char.isupper():
            c.append(char)
        elif char.islower():
            d.append(char)
        
            #d.append(char)
        else:
            a.append(char)
    a.sort(),b.sort(),c.sort(),d.sort()
    return ''.join(a)+''.join(b)+''.join(c)+''.join(d)


# In[53]:


Myfucntion('s3$Ab$')


# In[55]:


#enumarate

my_list = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(my_list, start=1):
    print(f"Index {index}: {fruit}")


# In[57]:


#rfind
#syntax : string.rfind(substring, start, end)

text = "Hello, World, World"
position = text.rfind("World")

if position != -1:
    print(f"The last occurrence of 'World' is at position {position}")
else:
    print("Substring not found")


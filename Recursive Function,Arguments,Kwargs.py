#!/usr/bin/env python
# coding: utf-8

# ##Recursive function
# 
# A recursive function is a function that calls itself either directly or indirectly in order to solve a problem. Recursive functions are often used to solve problems that can be broken down into smaller, similar subproblems. Each recursive call should make progress toward a base case, which is a condition that can be easily solved without further recursion.
# 
# #sample
# def factorial(n):
#     # Base case: factorial of 0 or 1 is 1
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial(n - 1)
#         
# -------------------------------------------------------------------------------------------------------------------------------
# 
# result = factorial(5)
# print(result)  # Output: 120

# ##Recursive function is similar to loop
# #Sample 2
# 
# #loop
# In Python, you can use loops to repeatedly execute a block of code. There are two main types of loops: for loops and while loops.
# 
# --------------------------------------------------------------------------------------------------------------------------------
# #Calling a function in Python involves using the function's name followed by parentheses (). If the function takes any arguments, you include them inside the parentheses. Here's a simple example:
# 
# def greet(name):
#     print("Hello, " + name + "!")
# 
# Calling the function
# greet("Vijay")
# 
# --------------------------------------------------------------------------------------------------------------------------------------
# #Base Condition
# A base condition, also known as a base case or termination condition, is a crucial concept in recursive functions. In a recursive function, the base case defines the simplest scenario where the function can return a result without making further recursive calls. It helps prevent the function from calling itself indefinitely and establishes a stopping criterion.
# 
# def factorial(n):
#     # Base case: factorial of 0 or 1 is 1
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial(n - 1)
# 
# Sample
# result = factorial(5)
# print(result)  # Output: 120
# 
# -------------------------------------------------------------------------------------------------------------------------------

# In[9]:


##sample
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(3)
print(result)


# In[12]:


#sample 2
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)


# In[15]:


fact(5)


# In[19]:


fact(7)


# #Recursion Error
# 
# A "recursion error" typically refers to a situation where a recursive function calls itself in a way that doesn't reach a base case, causing the recursion to continue indefinitely. This leads to a stack overflow because each recursive call consumes space on the call stack, and if there's no termination condition (base case) to stop the recursion, the stack eventually overflows.
# 
# #Sample
# def infinite_recursion():
#     return infinite_recursion()
# 
# ###Calling the function
# 
# --------------------------------------------------------------------------------------------------------------------------------
# infinite_recursion()
# 
# #FIFO
# #"FIFO" stands for "First In, First Out," and it's a method of organizing and manipulating data structures. In a FIFO data structure, the first element added to the structure is the first one to be removed. 
# #LIFO
# #"LIFO" stands for "Last In, First Out," and it's a method of organizing and manipulating data structures. In a LIFO data structure, the last element added to the structure is the first one to be removed. 

# In[22]:


#Recursion sample 2

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(3)
print(result)  # Output: 6


# #Uses of Recursion Function
# 
# Simplicity and Readability: Recursive solutions can often be more concise and easier to understand than their iterative counterparts. They allow you to express the solution in a clear and intuitive manner, mirroring the problem's natural structure.
# 
# Divide and Conquer: Recursive algorithms naturally follow the "divide and conquer" paradigm. By breaking a problem into smaller subproblems and solving each subproblem independently, you can often simplify the overall problem-solving process.
# 
# Elegance: In some cases, recursive solutions can be more elegant and expressive than iterative solutions. Recursive code can be more closely aligned with the mathematical description of the problem.
# 
# Problem Decomposition: Recursive functions can help break down complex problems into smaller, more manageable parts. Each recursive call focuses on a specific part of the problem, leading to a clearer and modularized solution.
# 
# Tree and Graph Traversal: Recursive functions are commonly used for traversing tree-like or graph-like structures. Examples include depth-first search in trees, directory traversals, and navigating hierarchical data structures.
# 
# Dynamic Programming: Recursive solutions are often the foundation of dynamic programming approaches. The recursive structure is used to identify overlapping subproblems, and memoization or tabulation techniques are applied to avoid redundant.

# In[23]:


#The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

#Sample 1
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
result = fibonacci(10)
print(result)


# In[42]:


#Sample 2

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

#f(n)= f(n-1)+f(n-2)

def fooRecFib(n):
    if n<=1:
        return 1
    else:
        return fooRecFib(n-1)+fooRecFib(n-2)


# In[43]:


fooRecFib(4)


# In[45]:


#Sample 3

for i in range(5):
    print(fooRecFib(i), end= ',')


# In[2]:


#Sample 4

def fooRecFib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fooRecFib(n-1)+fooRecFib(n-2)


# In[3]:


fooRecFib(7)


# #Arguments
# 
# arguments are values that you pass to a function or a method when calling it. There are two main types of arguments: positional arguments and keyword arguments.
# 
# 
# Positional Arguments:
# 
# These are the most common type of arguments.
# The order in which you pass positional arguments matters.
# The values are assigned to parameters based on their position in the function signature.

# In[24]:


#Sample 

def add(a, b):
    return a + b
result = add(2, 3)


# In[21]:


#Sample 2 

def foo(a,b,c=0, *args, **kwargs):
    r=a+b+c
    for arg in args:
        r+=arg
    return r


# In[22]:


foo(1,2,3,*(4,5,6))


# #Keyword Arguments:
# 
# You can also pass arguments by explicitly naming the parameter and providing a value.
# Order doesn't matter for keyword arguments.

# In[26]:


#Sample 3

def foo(a,b,c=0, *args, **kwargs):
    r=a+b+c
    for arg in args:
        r+=arg
        
    for kwarg in kwargs:
        print(kwargs[kwarg])
    return r


# In[32]:


foo(1,2,3,*(4,5,6),**{'marks':[1,2,3]})


# In[33]:


#Sample 4

def fooStuMarks(**kwargs):
    for kwarg in kwargs:
        print(f'Total Marks Scored by {kwarg} is {sum(kwargs[kwarg])}')


# In[37]:


fooStuMarks(**{'Vijay':(10,20,30),'Arnold':(10,20,30),'jason':(10,20,30),})


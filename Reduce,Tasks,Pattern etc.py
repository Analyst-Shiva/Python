#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lambda functions are anonymous functions in Python, and they are often used for short, simple operations

# Syntax of a lambda function:
# lambda arguments: expression

# Example 1: Add two numbers using a lambda function
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

#reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))


# In[5]:


#reduce sample1

from functools import reduce
 
def do_sum(x1, x2): return x1 + x2

reduce(do_sum, [1, 2, 3, 4])


# In[6]:


#reduce sample 2

reduce(lambda x,y: x*y, [1,2],[3,4])


# In[9]:


#In a right-angled triangle, one angle is a right angle, which measures 90 degrees. The other two angles must add up to 90 degrees as well, according to the triangle sum theorem.

#These are the only combinations that satisfy the conditions for a right-angled triangle. So, there are two ways to create a right-angled triangle:

#Since the sum of angles in a triangle is always 180 degrees.

# Right angle traingle:

r=5
for i in range(1, r+1):
    for j in range(i):
        print('*', end = '')
    print()   


# In[17]:


#0 sample

def fooTriangle(r,c):
    for i in range(1,r+1):
        for j in range(i):
            print(c,end='')
        print()


# In[19]:


fooTriangle(5,'@')


# In[41]:


#1 sample

def fooTriangle(r):
    r=5
    for i in range(1,r+1):
        for j in range(i):
            print('1',end='')
        print()


# In[44]:


fooTriangle(5)


# In[45]:


#2 sample

def fooTriangle(r):
    r=5
    for i in range(1,r+1):
        for j in range(i):
            print(j,end='')
        print()


# In[46]:


fooTriangle(7)


# In[51]:


#3 sample

for i in range(5,0,-1):
    for j in range(i):
        print('$',end='')
    print()


# In[52]:


#4 sample

def footriangles(r):
    for i in range (r):
        for j in range(i, r):
            print(j, end = ' ')
        print()


# In[54]:


footriangles(5)


# In[55]:


#5 sample

def footriangles(r):
    for i in range (r):
        for j in range(i-1, r):
            print(j, end = ' ')
        print()


# In[56]:


footriangles(r)


# In[81]:


#6 sample

def footriangles(r):
    for i in range (r):
        for j in range(i+1, r):
            print(j, end = ' ')
        print()


# In[82]:


footriangles(5)


# In[87]:


#7 pyramid

def footriangles(r):
    for i in range (r):
        for j in range(i,r):
            print(' ', end = ' ')
        for j in range(i):
            print('$', end = ' ')
        for j in range(i+1):
            print('$', end = ' ')
        print()


# In[88]:


footriangles(5)


# In[94]:


#7 Invertedpyramid

def footriangles(r):
    for i in range (r):
        for j in range(i,r):
            print(' ', end = ' ')
        for j in range(i):
            print('""$""', end = ' ')
        for j in range(i+1):
            print('""$""', end = ' ')
        print()


# In[99]:


footriangles(3)


# In[102]:


#8 Daimond

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i, n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()


# In[103]:


9#Rhombus

n =5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i, n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()


# In[6]:


#10 Daimond

def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Make sure the height is odd for symmetry

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# Example: Print a diamond with height 5
print_diamond(5)


# In[ ]:


print_diamond(5)


# In[3]:


#11 Capital M

def print_m_pattern(size):
    if size % 2 == 0:
        size += 1  # Ensure size is odd for a symmetric pattern

    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or (i == j and i <= size // 2) or (i + j == size - 1 and i <= size // 2):
                print("M", end=" ")
            else:
                print(" ", end=" ")
        print()


# In[4]:


print_m_pattern(5)


# In[1]:


#12 Special Charecters

def print_m_pattern(size):
    if size % 2 == 0:
        size += 1  # Ensure size is odd for a symmetric pattern

    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or (i == j and i <= size // 2) or (i + j == size - 1 and i <= size // 2):
                print("%", end=" ")
            else:
                print(" ", end=" ")
        print() 


# In[3]:


print_m_pattern(5)


# In[4]:


#13 Star

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * i)


# In[5]:


print_star_pattern(5)


# In[10]:


#14 Fivepoint star

def draw_five_point_star(size):
    for i in range(5):
        # Print spaces for indentation
        print(' ' * (4 - i), end='')

        # Print the star points
        print('*', end='')

        # Print spaces between points
        print(' ' * (2 * i - 1), end='')

        # Print the second star point for each arm
        if i != 0:
            print('*', end='')

        # Move to the next line for the next arm
        print()

# Draw a five-point star with a size of 5
draw_five_point_star(100)


# In[20]:


#15 star

def draw_star(size):
    for i in range(size):
        if i % 2 == 0:
            spaces = (size - i) // 2
            stars = i + 1
            print(" " * spaces + "*" * stars)
    
    for i in range(size - 2, 0, -2):
        spaces = (size - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

# Set the size of the star
star_size = 5

# Draw the star
draw_star(star_size)


# In[32]:


#16 Hologram

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i, n-1):
        print('/',end=' ')
    for j in range(i,n):
        print('/',end=' ')
    print()
for i in range (n):
    for j in range(i,n):
        print(' ', end = ' ')
    for j in range(i):
        print('&', end = ' ')
    for j in range(i+1):
        print('&', end = ' ')
    print()


# In[1]:


#17 sample

r = 5
for i in range(r):
    for j in range(i, r):
        print(' ', end = ' ')
    for j in range(r):
        print(' ', end = '*')
    print()


# In[2]:


#18 sample

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(n - i - 1):
        print('*', end=' ')
    for j in range(n - i):
        print('*', end=' ')
    print()


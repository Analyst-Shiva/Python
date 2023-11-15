#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Daimond Sample

def print_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Adjust the value of 'n' to control the size of the rhombus
n = 5
print_rhombus(n)


# In[16]:


# To write patterns

# Example 1: range(stop)
for i in range(0,5):
    print(i)  # Output: 0, 1, 2, 3, 4


# In[17]:


# help syntax

help(print)


# In[18]:


#print syntax

print('Hello'),print('Vijay')


# In[19]:


print('Hello', end = " "),print('Vijay')


# In[23]:


# Sample pattern

num = int(input("Enter the number of rows: "))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end=" ")  # Added a space after "end"
    print()


# In[53]:


#Sample daimond

num = 9

for i in range(1, num+1):
  i = i - (num//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (num - i*2) + " "*i)


# In[ ]:


# The logic is the following:
(A space is represented as "0" here.)
# i = 1 | new i = 1 - 5 = -4 | * : 9 - 8 = 1 | 0000 + * + 0000
# i = 2 | new i = 2 - 5 = -3 | * : 9 - 6 = 3 | 000 + *** + 000
# i = 3 | new i = 3 - 5 = -2 | * : 9 - 4 = 5 | 00 + ***** + 00
# i = 4 | new i = 4 - 5 = -1 | * : 9 - 2 = 7 | 0 + ******* + 0
# i = 5 | new i = 5 - 5 = 0  | * : 9 - 0 = 9 |    ********* 
# i = 6 | new i = 6 - 5 = 1  | * : 9 - 2 = 7 | 0 + ******* + 0
# i = 7 | new i = 7 - 5 = 2  | * : 9 - 4 = 5 | 00 + ***** + 00
# i = 8 | new i = 8 - 5 = 3  | * : 9 - 6 = 3 | 000 + *** + 000
# i = 9 | new i = 9 - 5 = 4  | * : 9 - 8 = 1 | 0000 + * + 0000

# Let's break down the logic step by step:

The loop runs for i from 1 to 9, representing the rows of the diamond.

For each iteration, it calculates the number of spaces and asterisks to be printed. The formula for spaces is given by (n - i), where n is the total number of rows (in this case, 9), and the formula for asterisks is given by 2 * i - 1.

It then prints the spaces, followed by the asterisks, and finally, more spaces. The number of spaces on each side of the asterisks is determined by the calculations mentioned above.

The pattern is such that the number of asterisks increases from 1 to 9 and then decreases back to 1, forming the upper and lower halves of the diamond.

The new i values represent the adjusted values of i to create symmetry in the diamond pattern.

The comments in the code are explaining the calculations for spaces, asterisks, and the resulting pattern for each iteration.

Here's the breakdown for the first few iterations:

When i = 1, it prints one asterisk in the center surrounded by spaces.
When i = 2, it prints three asterisks in the center surrounded by spaces.
When i = 3, it prints five asterisks in the center surrounded by spaces.
This pattern continues until i = 5, where it prints nine asterisks forming the widest part of the diamond.
Then, it starts decreasing the number of asterisks until i = 9, completing the diamond shape.
The pattern is symmetric both horizontally and vertically, creating a diamond shape.


# In[31]:


num = 4

n=int(input('enter a value'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
    
for i in range(n-1):
    print (    ' '*(i+1)+'* '*(n-i-1)) 


# In[1]:


#97

def butterfly_pattern(size):
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        for k in range(2 * size - 2 * i):
            print(" ", end=" ")
        for l in range(1, i + 1):
            print("*", end=" ")
        print()

    for i in range(size, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        for k in range(2 * size - 2 * i):
            print(" ", end=" ")
        for l in range(1, i + 1):
            print("*", end=" ")
        print()

# Set the size of the butterfly pattern
pattern_size = 4

# Call the function to print the butterfly pattern
butterfly_pattern(pattern_size)


# In[7]:


#99

str="";    
for Row in range(0,7):    
    for Col in range(0,7):     
        if (Col == 1 or Col == 5 or (Row == 2 and (Col == 2 or Col == 4)) or (Row == 3 and Col == 3)):  
            str=str+"* "    
        else:      
            str=str+"  "    
    str=str+"\n"    
print(str); 


# In[39]:


#97

n = int(input('Enter the number of rows for the butterfly pattern: '))

# Upper wing of the butterfly
for i in range(n):
    for j in range(2 * n):
        if j < i or j >= 2 * n - i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()

# Lower wing of the butterfly
for i in range(n - 1, -1, -1):
    for j in range(2 * n):
        if j < i or j >= 2 * n - i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()


# In[12]:


#90

n = int(input('Enter the number:'))
i = 1
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end= ' ')
        j -= 1
    print('* ', end= ' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end= ' ')
        k += 1
    if i == 1:
        print()
    else:
        print('* ')
    i += 1

i = n - 1
while i >= 1:
    j = n
    while j > i:
        print(' ', end= ' ')
        j -= 1
    print('* ', end= ' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end= ' ')
        k += 1
    if i == 1:
        print( )
    else:
        print('*')
    i -= 1


# In[13]:


#91

n = int(input('Enter the number:'))
i = 1
num = 1

# Upper part of the diamond
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print(num, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(num)
    i += 1
    num += 1

# Lower part of the diamond
i = n - 1
num = 1
while i >= 1:
    j = n
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(num, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(num)
    i -= 1
    num += 1


# In[14]:


#92

n = int(input('Enter the number:'))
i = 1
num = 5

# Upper part of the diamond
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print(num, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(num)
    i += 1
    num -= 1

# Lower part of the diamond
i = n - 1
num = 5
while i >= 1:
    j = n
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(num, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(num)
    i -= 1
    num -= 1


# In[15]:


#94 

n = int(input('Enter the number:'))
i = 1
char = ord('E')

# Upper part of the diamond
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print(chr(char), end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(chr(char))
    i += 1
    char -= 1

# Lower part of the diamond
i = n - 1
char = ord('E')
while i >= 1:
    j = n
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(chr(char), end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(chr(char))
    i -= 1
    char -= 1


# In[17]:


#95 

n = int(input('Enter the number:'))
i = 1
char = ord('A') + n - 1

# Upper part of the diamond
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print(chr(char), end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(chr(char))
    i += 1
    char -= 1

# Lower part of the diamond
i = n - 1
char = ord('A') + n - 2
while i >= 1:
    j = n
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(chr(char), end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(chr(char))
    i -= 1
    char -= 1


# In[31]:


# Sample

n = int(input('Enter the number:'))
i = 0
while i <= n - 1:
    j = 0
    while j < i:
        # display space
        print(' ', end=' ')
        j += 1

    k = 0
    while k <= n - i - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = n - 1
while i >= 0:
    j = 0
    while j < i:
        print(' ', end=' ')
        j += 1

    k = 0
    while k <= n - i - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# In[46]:


#97

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    


# In[48]:


# sample

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# In[50]:


#95

rows = 14
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print(" " * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2


# In[56]:


#99

num = int(input("Enter the range: "))

# i loop for range(height) of the triangles
for i in range(num):
    # first j loop for printing space ' ' for the left triangle
    for j in range((num - i) - 1):
        print(end=" ")
    # second j loop for printing stars '*' for the left triangle
    for j in range(i + 1):
        print("*", end=" ")
    
    # Print space between the two triangles
    print(" ", end=" ")
    
    # third j loop for printing stars '*' for the right triangle
    for j in range(i + 1):
        print("*", end=" ")
    
    print()


# In[57]:


#98 

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


# In[58]:


#99 

length = int(input('Enter number of rows: '))
# upper section
for i in range(length):
    for j in range(i):
        print('*',end='')
    
    for k in range(2*(length-i)):
        print(' ',end='')
    
    for l in range(i):
        print('*',end='')
    
    print()  # for new line

# lower section
for i in range(length):
    for j in range((length-1)-i+1):
        print('*',end='')
    
    for k in range(2*i):
        print(' ',end='')
    
    for l in range((length-1)-i+1):
        print('*',end='')
    
    print()  #for new line

    


# In[62]:


#55

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(size, abs(x) - 1, -1):
        print(y, end="")
    print()


# In[60]:


##56

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(size, abs(x) - 1, -1):
        print(chr(y + 65), end="")
    print()


# In[63]:


##57

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(abs(x), size + 1):
        print(chr(y + 65), end="")
    print()


# In[64]:


#58

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(size, abs(x) - 1, -1):
        print("*", end="")
    print()


# In[65]:


#59

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(abs(x), 0, -1):
        print(" ", end="")
    for z in range(size, abs(x) - 1, -1):
        print(z, end="")
    print()


# In[66]:


#60

size = 3
for x in range(size, -(size + 1), -1):
    for y in range(abs(x), 0, -1):
        print(" ", end="")
    for z in range(abs(x), 4):
        print(z, end="")
    print()


# In[67]:


#96 

n = 5  # size=5
px = n
py = n
for x in range(1, n + 1):
    for y in range(1, n * 2):
        if (y <= x or y >= n * 2 - x):
            print("*", end="")
        else:
            print(" ", end="")
    px -= 1
    py += 1
    print()


# In[68]:


#97

n = 7  # size=5
px = 1
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if (y <= px or y >= n - px + 1):
            print("*", end="")
        else:
            print(" ", end="")
    if (x <= n / 2):
        px += 1
    else:
        px -= 1
    print()


# In[69]:


#98

ph = 5  # height
ps = ph - 1  # space
inc = 1  # min star

for x in range(0, ph):
    for y in range(ps, x, -1):
        print(" ", end="")
    for z in range(0, inc):
        print("*", end="")

    for y in range(ph + ph - 2, inc - 1, -1):
        print(" ", end="")
    for z in range(0, inc):
        print("*", end="")

    inc += 2
    print()


# In[70]:


#99

ph = 5  # height
ps = ph - 1  # space
inc = 1

for x in range(0, ph):
    for y in range(ps, x, -1):
        print(" ", end="")
    for z in range(0, x + 1):
        print("* ", end="")

    for y in range(ph + ph - 2, inc - 1, -1):
        print(" ", end="")
    for z in range(0, x + 1):
        print("* ", end="")

    inc += 2
    print()


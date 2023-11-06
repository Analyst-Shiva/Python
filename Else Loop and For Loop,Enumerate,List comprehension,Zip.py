#!/usr/bin/env python
# coding: utf-8

# Else in For Loop()
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
# for ele in range(5): # natural for else process
#     print(ele)
# else:
#     print('execution completed')
# 0
# 1
# 2
# 3
# 4
# execution completed
# The else block will NOT be executed if the loop is stopped by a break statement.
# for ele in range(10):
#     if ele == 5:
#         break
#     print(ele)
# else:
#     print('execution completed')
# 0
# 1
# 2
# 3
# 4
# Else While Loop()
# With the else statement we can run a block of code once when the condition no longer is true.
# ele = 0 # natural while else process
# while ele in range(5):
#     print(ele)
#     ele+=1
# else:
#     print('aa')
# 0
# 1
# 2
# 3
# 4
# aa
# With the break statement we can stop the loop even if the while condition is true.
# ele = 0  # natural while else process
# 
# while ele in range(5):
#     if ele == 3:
#         print("Break the loop =", ele)
#         break  # using break 
#     print(ele)
#     ele += 1
# else:
#     print('This will not be executed because the loop was terminated by the break statement.')
# 0
# 1
# 2
# Break the loop = 3

# In[ ]:


Else in For Loop()
The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
for ele in range(5): # natural for else process
    print(ele)
else:
    print('execution completed')
0
1
2
3
4
execution completed
The else block will NOT be executed if the loop is stopped by a break statement.
for ele in range(10):
    if ele == 5:
        break
    print(ele)
else:
    print('execution completed')
0
1
2
3
4
Else While Loop()
With the else statement we can run a block of code once when the condition no longer is true.
ele = 0 # natural while else process
while ele in range(5):
    print(ele)
    ele+=1
else:
    print('aa')
0
1
2
3
4
aa
With the break statement we can stop the loop even if the while condition is true.
ele = 0  # natural while else process

while ele in range(5):
    if ele == 3:
        print("Break the loop =", ele)
        break  # using break 
    print(ele)
    ele += 1
else:
    print('This will not be executed because the loop was terminated by the break statement.')
0
1
2
Break the loop = 3


# In[ ]:


enumerate()
The enumerate function takes a collection and returns it as an enumerate object.The enumerate function adds a counter as the key of the enumerate object.
syntax: enumerate(iterable, start)
x = 'string' # enumerate: gives index and value of index

for ind,val in enumerate(x):
    print(ind,val)
0 s
1 t
2 r
3 i
4 n
5 g
x = [1,2,3,0,4,5] # taking a list 
y = float(input('enter a num: '))

for i, ele in enumerate (x):
    print(i, ele)
    if ele == y:
        print(f'value {y} entered is there in the container at index {i}') # using format 
        break # using break
else: 
    print('value not found')
enter a num: 5
0 1
1 2
2 3
3 0
4 4
5 5
value 5.0 entered is there in the container at index 5
x = [1,2,3,0,4,5] # taking a list
y = float(input('enter a num: '))

for ele in enumerate (x): # with out taking i it is a tuple 
    print(ele)
    if ele == y:
        print(f'value {y} entered is there in the container at index {i}') # using format
        break
else: 
    print('value not found') 
enter a num: 4
(0, 1)
(1, 2)
(2, 3)
(3, 0)
(4, 4)
value not found
x = 'Vijay' # using key value pair in enumerate
{key : value for key, value in enumerate(x)}
{0: 'V', 1: 'i', 2: 'j', 3: 'a', 4: 'y',}


# In[ ]:


List Comprehension()
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
a = [] # taking empty list
for i in range(0,11):
    a.append(i) # appending i range to empty list.
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [ele for ele in range(0,11)] # with out using empty list we can use list comphrensive
x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [2*ele for ele in range(0,11) if ele%2 == 0] # syntax: [var for var in iterator if c.e(using the var)]
x
[0, 4, 8, 12, 16, 20]
y = ('Your ARE Looking gooD')  # using for check lower alphabets 
y = {var for var in y if var.islower()}
     
y
{'g', 'i', 'k', 'n', 'o', 'r', 'u'}
y = ('Your ARE Looking gooD') # using for check upper alphabets 
y = [var for var in y if var.isupper()]
y
['Y', 'A', 'R', 'E', 'L', 'D']
y = ('Your ARE Looking gooD') 
y = {var for var in y if var.isupper()} # duplicates are not allowe in sets.
     
y 
{'A', 'D', 'E', 'L', 'R', 'Y'}


# In[ ]:


zip()
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
for ele in zip([1,2,3,4], [11,22,33]):
    print(ele)
(1, 11)
(2, 22)
(3, 33)
{key : value for key, value in zip([1,11,22],['a', 'b', 'c'])} # using key value pair for zip
{1: 'a', 11: 'b', 22: 'c'}


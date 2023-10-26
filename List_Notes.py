#!/usr/bin/env python
# coding: utf-8

# # LIST
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets[ ].
# 
# l = ["apple", "banana", "cherry"]
# print(l)
# ['apple', 'banana', 'cherry']
# 

# # List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value
# L = ["apple", "banana", "cherry", "apple", "cherry"]
# L
# ['apple', 'banana', 'cherry', 'apple', 'cherry']

# # List Length
# To determine how many items a list has, use the len() function
# L = ["apple", "banana", "cherry", "apple", "cherry"]
# len(L)
# 5

# # type()
# From Python's perspective, lists are defined as objects with the data type 'list'
# L = ["apple", "banana", "cherry", "apple", "cherry"]
# print(type(L))
# <class 'list'>

# # Access List Elements
# In Python, lists are ordered and each item in a list is associated with a number. The number is known as a list index.
# The index of the first element is 0, second element is 1 and so on. For example,
# la = ["Python", "Sql", "Java"] 
# print(la[0]) # access item at index 0
# print(la[2]) # access item at index 2
# Python
# Java

# # Negative Indexing in list
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
# la = ["Python", "Sql", "Java"] 
# print(la[-1]) # access item at index -1
# print(la[-2]) # access item at index -2
# Java
# Sql

# # Slicing of a List
# In Python, it is possible to access a portion of a list using the slicing operator
# my_list = ['p','r','o','g','r','a','m','i','z']
# print(my_list[2:5]) # items from index 2 to index 4
# print(my_list[5:]) # items from index 5 to end
# print(my_list[:]) # items beginning to end
# ['o', 'g', 'r']
# ['a', 'm', 'i', 'z']
# ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# # nested lists
# It is a smart and concise way of creating lists by iterating over an iterable object. Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.
# l = [1, 2, 3, [4, 5, 6]]
# print(l, type(l), len(l),  hex(id(l)), sep = '\n')
# [1, 2, 3, [4, 5, 6]]
# <class 'list'>
# 4
# 0x18e9fe60880
# print(l[3])
# print(l[3][0])
# print(l[3][::-1])
# [4, 5, 6]
# 4
# [6, 5, 4]

# # range list
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# syntax: ranger(start, end, step) # end means till end
# r = range(1, 11)
# print(r, type(r), len(r),  hex(id(r)), sep = '\n')
# range(1, 11)
# <class 'range'>
# 10
# 0x18e9fde3d80
# list(r) # we called it is a type casting method , the range is converted to list.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = range(1, 19)
# print(r, type(r), len(r),  hex(id(r)), sep = '\n')
# range(1, 19)
# <class 'range'>
# 18
# 0x18e9fde2430
# r = range(10, 1, -1) # range in indexing method and slicinbg
# print(r, type(r), len(r),  hex(id(r)), sep = '\n')
# range(10, 1, -1)
# <class 'range'>
# 9
# 0x18e9fde2a60

# # dir(l)
# ['__add__',
#  '__class__',
#  '__class_getitem__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__getstate__',
#  '__gt__',
#  '__hash__',
#  '__iadd__',
#  '__imul__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__mul__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__reversed__',
#  '__rmul__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'append',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']

# # list methods
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# # append()
# The append() method adds an item at the end of the list.
# syntax (list.append(elmnt))
# help(list.append)
# Help on method_descriptor:
# 
# append(self, object, /)
#     Append object to the end of the list.
# 
# l = []
# print(l, type(l), len(l),  hex(id(l)), sep = '\n')
# []
# <class 'list'>
# 0
# 0x18e9fe72100
# l.append(100) # to add only one value in lsit we use .append. it adds to end of the list
# print(l, type(l), len(l),  hex(id(l)), sep = '\n')
# [100]
# <class 'list'>
# 1
# 0x18e9fe72100
# a = ['abc', 100,]
# b = ['xyz']
# a.append(b)
# print(a, type(a), len(a),  hex(id(a)), sep = '\n')
# ['abc', 100, ['xyz']]
# <class 'list'>
# 3
# 0x18e9fe69480

# # extend()
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# syntax:list.extend(iterable)
# help(list.extend)
# Help on method_descriptor:
# 
# extend(self, iterable, /)
#     Extend list by appending elements from the iterable.
# 
# l.extend('string') 
# print(l, type(l), len(l),  hex(id(l)), sep = '\n')
# [100, 's', 't', 'r', 'i', 'n', 'g']
# <class 'list'>
# 7
# 0x18e9fe72100

# # insert()
# append() method only works for the addition of elements at the end of the List, for the addition of elements at the desired position, insert() method is used. Unlike append() which takes only one argument, the insert() method requires two arguments.
# syntax: list.insert(pos, elmnt)
# help(list.insert)
# Help on method_descriptor:
# 
# insert(self, index, object, /)
#     Insert object before index.
# 
# l.insert(1, 50) # always it moves to right side and adding to a particular index .insert.
# l
# [100, 50, 's', 't', 'r', 'i', 'n', 'g']
# l.insert(-2, 'aaa')
# l
# [100, 50, 's', 't', 'r', 'i', 'aaa', 'n', 'g']

# # remove()
# Elements can be removed from the List by using the built-in remove() function but an Error arises if the element doesn’t exist in the list. Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.
# syntax: list.remove(element)
# help(list.remove)
# Help on method_descriptor:
# 
# remove(self, value, /)
#     Remove first occurrence of value.
#     
#     Raises ValueError if the value is not present.
# 
# x =list('malayalam') #.remove works with an element # .pop always works on the index
# x
# ['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
# x.remove('a')
# x
# ['m', 'l', 'a', 'y', 'a', 'l', 'a', 'm']

# # pop()
# The list pop() method removes the item at the specified index. The method also returns the removed item.
# syntax: list.pop(index)
# help(list.pop)
# Help on method_descriptor:
# 
# pop(self, index=-1, /)
#     Remove and return item at index (default last).
#     
#     Raises IndexError if list is empty or index is out of range.
# 
# l = [0, 1, 2, 3, 4, 5] # by default .pop removes last value of the index
# l
# [0, 1, 2, 3, 4, 5]
# l.pop()
# 5
# a = l.pop()
# a, l
# (4, [0, 1, 2, 3])

# # index()
# The index() method returns the index of the specified element in the list.
# syntax: list.index(element, start, end)
# help(list.index)
# Help on method_descriptor:
# 
# index(self, value, start=0, stop=9223372036854775807, /)
#     Return first index of value.
#     
#     Raises ValueError if the value is not present.
# 
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index = vowels.index('e') # index of 'e' in vowels
# 
# print('The index of e:', index)
# index = vowels.index('i') # element 'i' is searched # index of the first 'i' is returned
# print('The index of i:', index)
# The index of e: 1
# The index of i: 2

# # count()
# The count() method returns the number of times the specified element appears in the list.
# syntax: list.count(element)
# help(list.count)
# Help on method_descriptor:
# 
# count(self, value, /)
#     Return number of occurrences of value.
# 
# numbers = [2, 3, 5, 2, 11, 2, 7] 
# count = numbers.count(2)
# print('Count of 2:', count)
# Count of 2: 3

# # clear()
# The clear() method removes all items from the list.
# syntax: list.clear()
# help(list.clear)
# Help on method_descriptor:
# 
# clear(self, /)
#     Remove all items from list.
# 
# prime_numbers = [2, 3, 5, 7, 9, 11]
# prime_numbers.clear() # remove all elements
# print(prime_numbers)
# []

# # copy()
# The copy() method returns a shallow copy of the list.
# syntax: new_list = list.copy()
# help(list.copy)
# Help on method_descriptor:
# 
# copy(self, /)
#     Return a shallow copy of the list.
# 
# s = [2, 3, 5]
# numbers = s.copy() # copying a list
# print('Copied List:', s)
# Copied List: [2, 3, 5]

# # sort()
# The sort() method sorts the items of a list in ascending or descending order.
# syntax: list.sort(key=..., reverse=...) # Alternatively we can use function sorted(list, key=..., reverse=...)
# help(list.sort)
# Help on method_descriptor:
# 
# sort(self, /, *, key=None, reverse=False)
#     Sort the list in ascending order and return None.
#     
#     The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
#     order of two equal elements is maintained).
#     
#     If a key function is given, apply it once to each list item and sort them,
#     ascending or descending, according to their function values.
#     
#     The reverse flag can be set to sort in descending order.
# 
# x = [11, 3, 7, 5, 2]
# x.sort() # sorting the list in ascending order
# print(x)
# [2, 3, 5, 7, 11]

# # reverse()
# The reverse() method reverses the elements of the list.
# syntax: list.reverse()
# help(list.reverse)
# Help on method_descriptor:
# 
# reverse(self, /)
#     Reverse *IN PLACE*.
# 
# z = [2, 3, 5, 7]
# z.reverse() # reverse the order of list elements
# print('zee:', z)
# zee: [7, 5, 3, 2]

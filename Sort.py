#!/usr/bin/env python
# coding: utf-8

# # Sort
# 
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
# aa = [1, -8, 96, 10.1001]
# aa.sort(reverse=True)
# aa
# [96, 10.1001, 1, -8]
# 
# 

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

# # Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets or parantheses.
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value
# a = (1, 2.2, 3+3j, 'four', print, range)
# print(a, type(a), id(a), sep = '\n')
# (1, 2.2, (3+3j), 'four', <built-in function print>, <class 'range'>)
# <class 'tuple'>
# 2438456471232
# b = tuple(range(5))
# b
# (0, 1, 2, 3, 4)
# c = tuple('string')
# c
# ('s', 't', 'r', 'i', 'n', 'g')
# z = (5, ) # unpacking tuple # tuple it checks for unpacking or not
# z, type(z), len(z)
# ((5,), tuple, 1)
# b = (1, 2, 3, [11, 22]) # tuples are immutable but inside tuple if there is container it can be mutuble.
# b
# (1, 2, 3, [11, 22])
# b[3].append(33)
# b
# (1, 2, 3, [11, 22, 33])

# # dir(tuple)
# ['__add__',
#  '__class__',
#  '__class_getitem__',
#  '__contains__',
#  '__delattr__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__getnewargs__',
#  '__getstate__',
#  '__gt__',
#  '__hash__',
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
#  '__rmul__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'count',
#  'index']

# # list methods
# 'count', 'index'
# count()
# The count() method returns the number of times a specified value appears in the tuple.
# Parameter : value
# Description : Required The item to search for
# Syntax: tuple.count(value)
# help(list.count)
# Help on method_descriptor:
# 
# count(self, value, /)
#     Return number of occurrences of value.
# 
# t = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# 
# x = t.count(5)
# 
# print(x)
# 
# 2

# # index()
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# Parameter :value
# Description : Required. The item to search for
# Syntax: tuple.index(value)
# help(list.index)
# Help on method_descriptor:
# 
# index(self, value, start=0, stop=9223372036854775807, /)
#     Return first index of value.
#     
#     Raises ValueError if the value is not present.
# 
# i = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = i.index(8)
# print(x)
# 3

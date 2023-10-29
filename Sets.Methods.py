#!/usr/bin/env python
# coding: utf-8

# # SETS{}
# sets are a cluster of hetrogeneous data values, they aren't ordered we declares sets by using {}
# we can use set class to perform type-casting
# sets have methods that are unique to sets, like union, intersection etc
# sets are partially mutuable
# sets don't have duplicate values
# note: The values True and 1 are considered the same value in sets, and are treated as duplicates
# help(set)
# Help on class set in module builtins:
# 
# class set(object)
#  |  set() -> new empty set object
#  |  set(iterable) -> new set object
#  |  
#  |  Build an unordered collection of unique elements.
#  |  
#  |  Methods defined here:
#  |  
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |  
#  |  __contains__(...)
#  |      x.__contains__(y) <==> y in x.
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __iand__(self, value, /)
#  |      Return self&=value.
#  |  
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  __ior__(self, value, /)
#  |      Return self|=value.
#  |  
#  |  __isub__(self, value, /)
#  |      Return self-=value.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __ixor__(self, value, /)
#  |      Return self^=value.
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __or__(self, value, /)
#  |      Return self|value.
#  |  
#  |  __rand__(self, value, /)
#  |      Return value&self.
#  |  
#  |  __reduce__(...)
#  |      Return state information for pickling.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __ror__(self, value, /)
#  |      Return value|self.
#  |  
#  |  __rsub__(self, value, /)
#  |      Return value-self.
#  |  
#  |  __rxor__(self, value, /)
#  |      Return value^self.
#  |  
#  |  __sizeof__(...)
#  |      S.__sizeof__() -> size of S in memory, in bytes
#  |  
#  |  __sub__(self, value, /)
#  |      Return self-value.
#  |  
#  |  __xor__(self, value, /)
#  |      Return self^value.
#  |  
#  |  add(...)
#  |      Add an element to a set.
#  |      
#  |      This has no effect if the element is already present.
#  |  
#  |  clear(...)
#  |      Remove all elements from this set.
#  |  
#  |  copy(...)
#  |      Return a shallow copy of a set.
#  |  
#  |  difference(...)
#  |      Return the difference of two or more sets as a new set.
#  |      
#  |      (i.e. all elements that are in this set but not the others.)
#  |  
#  |  difference_update(...)
#  |      Remove all elements of another set from this set.
#  |  
#  |  discard(...)
#  |      Remove an element from a set if it is a member.
#  |      
#  |      Unlike set.remove(), the discard() method does not raise
#  |      an exception when an element is missing from the set.
#  |  
#  |  intersection(...)
#  |      Return the intersection of two sets as a new set.
#  |      
#  |      (i.e. all elements that are in both sets.)
#  |  
#  |  intersection_update(...)
#  |      Update a set with the intersection of itself and another.
#  |  
#  |  isdisjoint(...)
#  |      Return True if two sets have a null intersection.
#  |  
#  |  issubset(...)
#  |      Report whether another set contains this set.
#  |  
#  |  issuperset(...)
#  |      Report whether this set contains another set.
#  |  
#  |  pop(...)
#  |      Remove and return an arbitrary set element.
#  |      Raises KeyError if the set is empty.
#  |  
#  |  remove(...)
#  |      Remove an element from a set; it must be a member.
#  |      
#  |      If the element is not a member, raise a KeyError.
#  |  
#  |  symmetric_difference(...)
#  |      Return the symmetric difference of two sets as a new set.
#  |      
#  |      (i.e. all elements that are in exactly one of the sets.)
#  |  
#  |  symmetric_difference_update(...)
#  |      Update a set with the symmetric difference of itself and another.
#  |  
#  |  union(...)
#  |      Return the union of sets as a new set.
#  |      
#  |      (i.e. all elements that are in either set.)
#  |  
#  |  update(...)
#  |      Update a set with the union of itself and others.
#  |  
#  |  

# # |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.

# # |  Data and other attributes defined here:
#  |  
#  |  __hash__ = None
# 
# x, y ={1, 2.2, 3+3j, 'four', print, range, True}, set([1, 2.2, 3+3j, 'four', print, range, True])
# print(x, type(x), len(x), hex(id(x)), sep = '\n')
# print(y, type(y), len(y), hex(id(y)), sep = '\n')
# {1, 2.2, 'four', <built-in function print>, (3+3j), <class 'range'>}
# <class 'set'>
# 6
# 0x279838c11c0
# {1, 2.2, 'four', <built-in function print>, (3+3j), <class 'range'>}
# <class 'set'>
# 6
# 0x279838c1540

# # empty set
# x = {}
# print(x, type(x), len(x), hex(id(x)), sep = '\n')
# {}
# <class 'dict'>
# 0
# 0x2798393dbc0
# a = {1,1,1,2,2,2}
# a
# {1, 2}-

# # dir(set)
# ['__and__',
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
#  '__getstate__',
#  '__gt__',
#  '__hash__',
#  '__iand__',
#  '__init__',
#  '__init_subclass__',
#  '__ior__',
#  '__isub__',
#  '__iter__',
#  '__ixor__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__or__',
#  '__rand__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__ror__',
#  '__rsub__',
#  '__rxor__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__sub__',
#  '__subclasshook__',
#  '__xor__',
#  'add',
#  'clear',
#  'copy',
#  'difference',
#  'difference_update',
#  'discard',
#  'intersection',
#  'intersection_update',
#  'isdisjoint',
#  'issubset',
#  'issuperset',
#  'pop',
#  'remove',
#  'symmetric_difference',
#  'symmetric_difference_update',
#  'union',
#  'update']

# # set methods()
# ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# # add()
# The Python set add() method adds a given element to a set if the element is not present in the set in Python.
# Parameters: The element that needs to be added to a set.
# Syntax: set.add( elem )
# help(set.add)
# Help on method_descriptor:
# 
# add(...)
#     Add an element to a set.
#     
#     This has no effect if the element is already present.
# 
# x = set()
# x
# set()
# x.add(9) # Add Element to an Empty set
# x
# {9}

# # clear()
# Python Set clear() method removes all elements from the set.
# parameters: The clear() method doesn’t take any parameters.
# Return: None
# Syntax: set.clear()
# help(set.clear)
# Help on method_descriptor:
# 
# clear(...)
#     Remove all elements from this set.
# 
# x
# {9}
# x.clear() # by using clear() it clears every value and gives empty set
# x
# set()

# # copy()
# The copy() method returns a shallow copy of the set in python. If we use “=” to copy a set to another set, when we modify in the copied set, the changes are also reflected in the original set. So we have to create a shallow copy of the set such that when we modify something in the copied set, changes are not reflected back in the original set.
# Parameters:The copy() method for sets doesn’t take any parameters.
# Return value:The function returns a shallow copy of the original set. Below is the implementation of the above function
# Syntax: set_name.copy()
# help(set.copy)
# Help on method_descriptor:
# 
# copy(...)
#     Return a shallow copy of a set.
# 
# x = {1,2,3,4}
# x
# {1, 2, 3, 4}
# x.copy()
# {1, 2, 3, 4}

# # difference()
# The difference between the two sets in Python is equal to the difference between the number of elements in two sets. The function difference() returns a set that is the difference between two sets. Let’s try to find out what will be the difference between two sets A and B. Then (set A – set B) will be the elements present in set A but not in B and (set B – set A) will be the elements present in set B but not in set A.
# Parameter : set
# Description : Required. The set to check for differences in
# Syntax: set.difference(set)
# help(set.difference)
# Help on method_descriptor:
# 
# difference(...)
#     Return the difference of two or more sets as a new set.
#     
#     (i.e. all elements that are in this set but not the others.)
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# a,b
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})
# a.difference(b)
# {1, 2, 3}
#  b.difference(a)
# {6, 7, 8}
# a.difference(b),  b.difference(a)
# ({1, 2, 3}, {6, 7, 8})

# # difference_update()
# The difference_update() method helps in an in-place way of differentiating the set. The previously discussed set difference() helps to find out the difference between two sets and returns a new set with the difference value, but the difference_update() updates the existing caller set.
# Parameter : set
# Description : Required. The set to check for differences in
# Syntax: set.difference_update(set)
# help(set.difference_update)
# Help on method_descriptor:
# 
# difference_update(...)
#     Remove all elements of another set from this set.
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# a,b
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})
# a.difference_update(b), b.difference_update(a)
# (None, None)

# # discard()
# Python discard() is a built-in method to remove elements from the set. The discard() method takes exactly one argument. This method does not return any value.
# Parameter : element – an item to remove from the set.
# Return Value : return – discard() method doesn’t return any value.
# Syntax: set.discard(element)
# help(set.discard)
# Help on method_descriptor:
# 
# discard(...)
#     Remove an element from a set if it is a member.
#     
#     Unlike set.remove(), the discard() method does not raise
#     an exception when an element is missing from the set.
# 
# x
# {1, 2, 3, 4}
# x.discard(3)
# x
# {1, 2, 4}
# x.discard(3) # the discard() method will not raise an error if the specified item does not exist 
# x
# {1, 2, 4}

# # Intersection()
# The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
# Parameters : any number of sets can be passed
# Return: Returns a set which has the intersection of all sets(set1, set2, set3…) with set1. It returns a copy of set1 only if no parameter is passed.
# Syntax: set1.intersection(set2, set3, set4….)
# help(set.intersection)
# Help on method_descriptor:
# 
# intersection(...)
#     Return the intersection of two sets as a new set.
#     
#     (i.e. all elements that are in both sets.)
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'}
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# a.intersection(b)
# {4, 5}
# a.intersection(d)
# set()

# # intersection_update()
# Python intersection_update() method is used to update a set with common elements only of all the sets passed in parameter of intersection_update() method.
# Parameters: One or more sets
# Return : None
# Syntax: set.intersection_update(set1,set2,set3,………..,set n)
# help(set.intersection_update)
# Help on method_descriptor:
# 
# intersection_update(...)
#     Update a set with the intersection of itself and another.
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'}
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# a.intersection_update(b), b.intersection_update(a)
# (None, None)

# # isdisjoint()
# Python set isdisjoint() function check whether the two sets are disjoint or not, if it is disjoint then it returns True otherwise it will return False. Two sets are said to be disjoint when their intersection is null.
# Parameters: another set to compare with (or) an iterable (list, tuple, dictionary, and string)
# Return: bool
# Syntax: set1.isdisjoint(set2)
# help(set.isdisjoint)
# Help on method_descriptor:
# 
# isdisjoint(...)
#     Return True if two sets have a null intersection.
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# a,b
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})
# a.isdisjoint(b)
# False

# # issubset()
# Python set issubset() method returns True if all elements of a set A are present in another set B which is passed as an argument, and returns False if all elements are not present in Python.
# Parameter: other_set: any other set to compare with.
# Return: bool
# Syntax: set_obj.issubset(other_set)
# help(set.issubset)
# Help on method_descriptor:
# 
# issubset(...)
#     Report whether another set contains this set.
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'} 
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# a.issubset(c)
# True

# # issuperset()
# Python Set issuperset() method returns True if all elements of a set B are in set A. Then Set A is the superset of set B.
# Parameter: Any other Set to compare with
# Return: boolean value
# Syntax: A.issuperset(B)
# help(set.issuperset)
# Help on method_descriptor:
# 
# issuperset(...)
#     Report whether this set contains another set.
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'} 
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# c.issuperset(a)
# True

# # pop()
# Python set pop() removes any random element from the set and returns the removed element. In this article, we will see about the Python set pop() method.
# Parameter: set.pop() doesn’t take any parameter.
# Return: Returns the popped element from the set
# Syntax: set_obj.pop()
# help(set.pop)
# Help on method_descriptor:
# 
# pop(...)
#     Remove and return an arbitrary set element.
#     Raises KeyError if the set is empty.
# 
# x = {1,2,3,4,5}
# x
# {1, 2, 3, 4, 5}
# a = x.pop() # it removes random elements
# a,x
# (1, {2, 3, 4, 5})

# # remove()
# The remove() method removes the specified element from the set. is method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
# Parameter : item
# Description : Required. The item to search for, and remove
# syntax: set.remove(item)
# help(set.remove)
# Help on method_descriptor:
# 
# remove(...)
#     Remove an element from a set; it must be a member.
#     
#     If the element is not a member, raise a KeyError.
# 
# x = {1,2,3,4,5}
# x
# {1, 2, 3, 4, 5}
# x.remove(1)
# x
# {2, 3, 4, 5}
# x.remove(1) #the remove() method will raise an error if the specified item does not exist
# x

# # symmetric_difference()
# The symmetric difference of two sets set1 and set2 is the set of elements which are in either of the sets set1 or set2 but not in both.
# image.png
# 
# Parameters : It only takes a single set as the parameter. If a list, tuple or dictionary is passed it converts it a set and performs the task.
# Return value : Returns a set which is the symmetric difference between the two sets.
# Syntax : set1_name.symmetric_difference(set2_name)
# help(set.symmetric_difference)
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'} 
# sep = '\n'
# a,b,c,d
# a.symmetric_difference(b), b.symmetric_difference(a)

# # symmetric_difference_update()
# The symmetric difference between the two sets is the set of elements that are in either of the sets but not in both of them.
# Parameters: The symmetric_difference takes a single “iterable” as an argument. Iterable should contain hashable object.
# Returns: This method returns None (which indicates absence of a return value). It only updates the set calling symmetric_difference_update() with the symmetric difference of sets.
# Syntax: A.symmetric_difference_update(B)
# help(set.symmetric_difference_update)
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'} 
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# a.symmetric_difference_update(b), b.symmetric_difference_update(a)
# (None, None)

# # Union()
# Python set Union() Method returns a new set that contains all the items from the original set.The union of two given sets is the set that contains all the elements of both sets. The union of two given sets A and B is a set that consists of all the elements of A and all the elements of B such that no element is repeated.
# Parameters: zero or more sets
# Return: Returns a set, which has the union of all sets(set1, set2, set3…) with set1. It returns a copy of set1 only if no parameter is passed.
# Syntax: set1.union(set2, set3, set4….)
# help(set.union)
# Help on method_descriptor:
# 
# union(...)
#     Return the union of sets as a new set.
#     
#     (i.e. all elements that are in either set.)
# 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = set(range(1,9))
# d = {'a','b','c'} 
# sep = '\n'
# a,b,c,d
# ({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}, {'a', 'b', 'c'})
# a.union(b)
# {1, 2, 3, 4, 5, 6, 7, 8}
# b.union(d)
# {4, 5, 6, 7, 8, 'a', 'b', 'c'}
# c.union(b)
# {1, 2, 3, 4, 5, 6, 7, 8}

# # update()
# Python update() function in set adds elements from a set (passed as an argument) to the set.
# Parameters : Update() method takes any number of argument. The arguments can be a set, list, tuples or a dictionary. It automatically converts into a set and adds to the set.
# Return value : This method adds set2 to set1 and returns nothing. \
# set1.update(set2)
# help(set.update)
# Help on method_descriptor:
# 
# update(...)
#     Update a set with the union of itself and others.
# 
# x = {1,2,3,4,5}
# x
# {1, 2, 3, 4, 5}
# x.update((7,8,9))
# x
# {1, 2, 3, 4, 5, 7, 8, 9}

# # Dictionary{}
# dictionary are keya nd value pairs enclosed in{}
# key and value are seperated by : while key and value pairs are seperated by ,
# keys are mapped to their values
# in dictionaries, keys are unique, we can't have duplicate values
# (dict) is class of dictionary
# help(dict)
# Help on class dict in module builtins:
# 
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |  
#  |  Built-in subclasses:
#  |      StgDict
#  |  
#  |  Methods defined here:
#  |  
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |  
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  __ior__(self, value, /)
#  |      Return self|=value.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __or__(self, value, /)
#  |      Return self|value.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __reversed__(self, /)
#  |      Return a reverse iterator over the dict keys.
#  |  
#  |  __ror__(self, value, /)
#  |      Return value|self.
#  |  
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |  
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |  
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |  
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |  
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |  
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |  
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      
#  |      If the key is not found, return the default if given; otherwise,
#  |      raise a KeyError.
#  |  
#  |  popitem(self, /)
#  |      Remove and return a (key, value) pair as a 2-tuple.
#  |      
#  |      Pairs are returned in LIFO (last-in, first-out) order.
#  |      Raises KeyError if the dict is empty.
#  |  
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |      
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |  
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values

# # Class methods defined here:
#  |  
#  |  __class_getitem__(...) from builtins.type
#  |      See PEP 585
#  |  
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value.

# # Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.

# #  Data and other attributes defined here:
#  |  
#  |  __hash__ = None
# 
# d = { } # empty dictionary
# d
# {}
# x = {1 : [1,2,3],
#     'hello' : (4,5,6),
#     ('f', 'g') : 5}
# x
# {1: [1, 2, 3], 'hello': (4, 5, 6), ('f', 'g'): 5}
# x = {1 : [1,2,3],
#     'hello' : (4,5,6),
#     'hello' : ['hi']}
# x
# {1: [1, 2, 3], 'hello': ['hi']}
# x[1]
# [1, 2, 3]
# x['hello']
# ['hi']
# x['hello'][0][-1]
# 'i'
# ddict = {          # duplicate values not allowed
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(ddict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

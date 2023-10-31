#!/usr/bin/env python
# coding: utf-8

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

# Class methods defined here:
#  |  
#  |  __class_getitem__(...) from builtins.type
#  |      See PEP 585
#  |  
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value. |  

# In[ ]:


Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.


# Data and other attributes defined here:
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

# dir(dict)
# ['__class__',
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
#  '__init__',
#  '__init_subclass__',
#  '__ior__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__or__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__reversed__',
#  '__ror__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'clear',
#  'copy',
#  'fromkeys',
#  'get',
#  'items',
#  'keys',
#  'pop',
#  'popitem',
#  'setdefault',
#  'update',
#  'values']

# methods in dictionary
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# 
# clear()
# The clear() method removes all the elements from a dictionary.
# Syntax : dictionary.clear()
# help(dict.clear)
# Help on method_descriptor:
# 
# clear(...)
#     D.clear() -> None.  Remove all items from D.
# 
# c = {
#   "brand": "suzuki",
#   "model": "baleno",
#   "year": 2023
# }
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# c.clear() # it clears all the elements and gives empty dictionary.
# c
# {}
# copy()
# The copy() method returns a copy of the specified dictionary.
# syntax : dictionary.copy()
# help(dict.copy)
# Help on method_descriptor:
# 
# copy(...)
#     D.copy() -> a shallow copy of D
# 
# c = {
#   "brand": "suzuki",
#   "model": "baleno",
#   "year": 2023
# }
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# x = c.copy()
# print(x)
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# fromkeys()
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# Parameter
# keys Required: An iterable specifying the keys of the new dictionary
# value Optional: The value for all keys. Default value is None
# Syntax : dict.fromkeys(keys, value)
# help(dict.fromkeys)
# Help on built-in function fromkeys:
# 
# fromkeys(iterable, value=None, /) method of builtins.type instance
#     Create a new dictionary with keys from iterable and values set to value.
# 
# c = {'g':'god', # gives a keys in fromkeys
#      'h':'holla',
#     'i':'ice'}
# c
# {'g': 'god', 'h': 'holla', 'i': 'ice'}
# d = dict.fromkeys(c) # fromkeys is a class dictionary creates a new dictionary whose keys are given dictionary values all none.
# d
# {'g': None, 'h': None, 'i': None}
# get()
# The get() method returns the value of the item with the specified key.
# Parameter
# keyname: Required. The keyname of the item you want to return the value from
# value Optional: A value to return if the specified key does not exist.Default value None
# Syntax : dictionary.get(keyname, value)
# help(dict.get)
# Help on method_descriptor:
# 
# get(self, key, default=None, /)
#     Return the value for key if key is in the dictionary, else default.
# 
# x = {'k1':1,
#     'k2':2,
#     'k3':3}
# x
# {'k1': 1, 'k2': 2, 'k3': 3}
# x.get('k3')
# 3
# x['k'] # it shows error if the element is not executed

# KeyError                                  Traceback (most recent call last)
# Cell In[35], line 1
# ----> 1 x['k']
# 
# KeyError: 'k'
# x.get('k') # it not shows error if the element is not executed
# items()
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.The view object will reflect any changes done to the dictionary.
# Syntax : dictionary.items()
# help(dict.items)
# Help on method_descriptor:
# 
# items(...)
#     D.items() -> a set-like object providing a view on D's items
# 
# c = {
#   "brand": "suzuki",
#   "model": "baleno",
#   "year": 2023
# }
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# x = c.items() # the items we can find and we can change # it not allows duplicate keys so it over writes the value
# 
# c["year"] = 2025 
# 
# print(x)
# dict_items([('brand', 'suzuki'), ('model', 'baleno'), ('year', 2025)])
# keys()
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.The view object will reflect any changes done to the dictionary.
# syntax : dictionary.keys()
# help(dict.keys)
# Help on method_descriptor:
# 
# keys(...)
#     D.keys() -> a set-like object providing a view on D's keys
# 
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2025}
# y = c.keys() # keys shows only keys in dictionary
# print(y)
# dict_keys(['brand', 'model', 'year'])
# pop()
# The pop() method removes the specified item from the dictionary.The value of the removed item is the return value of the pop() method.
# Parameter
# keyname Required:The keyname of the item you want to remove
# defaultvalue Optional: A value to return if the specified key do not exist.If this parameter is not specified, and the no item with the specified key is found, an error is raised
# Syntax : dictionary.pop(keyname, defaultvalue)
# help(dict.pop)
# 
# Help on method_descriptor:
# 
# pop(...)
#     D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#     
#     If the key is not found, return the default if given; otherwise,
#     raise a KeyError.
# 
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# c.pop('year') # it pops out the value
# c
# {'brand': 'suzuki', 'model': 'baleno'}
# popitem()
# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.The removed item is the return value of the popitem() method, as a tuple.
# Syntax : dictionary.popitem()
# help(dict.popitem)
# Help on method_descriptor:
# 
# popitem(self, /)
#     Remove and return a (key, value) pair as a 2-tuple.
#     
#     Pairs are returned in LIFO (last-in, first-out) order.
#     Raises KeyError if the dict is empty.
# 
# c = {
#   "brand": "suzuki",
#   "model": "baleno",
#   "year": 2023
# }
# c
# {'brand': 'suzuki', 'model': 'baleno', 'year': 2023}
# c.popitem() # if we not mention any value it pop outs very end value.
# print(c)
# {'brand': 'suzuki', 'model': 'baleno'}
# update()
# The update() method inserts the specified items to the dictionary.The specified items can be a dictionary, or an iterable object with key value pairs.
# Parameter Description
# iterable: A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary
# Syntax : dictionary.update(iterable)
# help(dict.update)
# Help on method_descriptor:
# 
# update(...)
#     D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#     If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#     If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#     In either case, this is followed by: for k in F:  D[k] = F[k]
# 
# x = {'k1':1,
#     'k2':2,
#     'k3':3}
# x
# {'k1': 1, 'k2': 2, 'k3': 3}
# x['k4'] = 4 # for adding to existing dictionary
# x
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
# x['k1']  = 111 # it not allows duplicate keys so it over writes the value
# x
# {'k1': 111, 'k2': 2, 'k3': 3, 'k4': 4}
# x.update([('k5',5), # we can use update also to add a key and value to existing dictionary using tuples
#          ('k6',6)])
# x
# {'k1': 111, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6}
# x.update({'k7':7,'k8':8}) # we can use update also to add a key and value to existing dictionary using tuples with dictionary
# x
# {'k1': 111, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8}
# values()
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.The view object will reflect any changes done to the dictionary.
# Syntax : dictionary.values()
# help(dict.values)
# Help on method_descriptor:
# 
# values(...)
#     D.values() -> an object providing a view on D's values
# 
# x = {'k1':1,
#     'k2':2,
#     'k3':3}
# x
# {'k1': 1, 'k2': 2, 'k3': 3}
# z = x.values() # by using values it shows only the values in dictionary
# z
# dict_values([1, 2, 3])
# setdefault()
# The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value.
# Parameter
# keyname Required: The keyname of the item you want to return the value from
# value Optional: If the key exist, this parameter has no effect.If the key does not exist, this value becomes the key's valueDefault value None
# Syntax : dictionary.setdefault(keyname, value)
# help(dict.setdefault)
# Help on method_descriptor:
# 
# setdefault(self, key, default=None, /)
#     Insert key with a value of default if key is not in the dictionary.
#     
#     Return the value for key if key is in the dictionary, else default.
# 
# x = {'k1':1,
#     'k2':2,
#     'k3':3}
# x
# {'k1': 1, 'k2': 2, 'k3': 3}
# v = x.setdefault('k2', 6) # If the key exist, this parameter has no effect.
# 
# print(v)
# 2
# v
# 2
# x = {'k1':1,
#     'k2':2,
#     'k3':3}
# x
# {'k1': 1, 'k2': 2, 'k3': 3}
# k = x.setdefault('k') # if If the key does not exist, this value becomes the key's valueDefault value None.
# print(k)
# None

# In[ ]:


string methods
maketrans()
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
Parameter
x: Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y: Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z: Optional. A string describing which characters to remove from the original string.
Syntax : str.maketrans(x, y, z)
help(str.maketrans)
Help on built-in function maketrans:

maketrans(...)
    Return a translation table usable for str.translate().
    
    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y. If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.

t = "Hello goodevening!"

m = str.maketrans("H", "F")

print(t.translate(m))
Fello goodevening!
k = "Good night Vijay!"
x = "thc"
y = "kok"
z = "odnght"
L = str.maketrans(x, y, z)
print(k.translate(L))
G i kiu!

translate()
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
Use the maketrans() method to create a mapping table.
If a character is not specified in the dictionary/table, the character will not be replaced.
If you use a dictionary, you must use ascii codes instead of characters.
Parameter
table Required: Either a dictionary, or a mapping table describing how to perform the replace
Syntax : string.translate(table)
help(str.translate)
Help on method_descriptor:

translate(self, table, /)
    Replace each character in the string using the given translation table.
    
      table
        Translation table, which must be a mapping of Unicode ordinals to
        Unicode ordinals, strings, or None.
    
    The table must implement lookup/indexing via __getitem__, for instance a
    dictionary or list.  If this operation raises LookupError, the character is
    left untouched.  Characters mapped to None are deleted.

d = {67:  80,
    72: 70} #use a dictionary with ascii codes to replace 67 (C) with 80 (P) # 72 (H) with 70 (F).
k = "Hello Vijay!"
print(k.translate(d))
Fello Phintu!
t = 'how are you my friend'
x = 'ohw'
y = 'rea'
z = 'ufm'
k = str.maketrans(x,y,z)
print(t.translate(k))
era are yr y riend


conditional statement
if,elif,else
kranthimarks = int(input('marks scored; '))

if vijaymarks >= 85:
    print('first round')
elif vijaymarks >= 75:
    print('second round')
elif vijaymarks >=65:
    print('screening round')
else:
    print('study hard')
marks scored; 90
first round
vijaymarks = int(input('marks scored; '))

if Vijaymarks >= 85:
    print('first round')
elif Vijaymarks >= 75:
    print('second round')
elif Vijaymarks >=65:
    print('screening round')
else:
    print('study hard')
marks scored; 80
second round
vijaymarks = int(input('marks scored; '))

if Vijaymarks >= 85:
    print('first round')
elif vijaymarks >= 75:
    print('second round')
elif Vijaymarks >=65:
    print('screening round')
else:
    print('study hard')
marks scored; 70
screening round
Vijaymarks = int(input('marks scored; '))

if Vijaymarks >= 85:
    print('first round')
elif Vijaymarks >= 75:
    print('second round')
elif Vijaymarks >=65:
    print('screening round')
else:
    print('study hard')
marks scored; 60
study hard
Vijaymarks = int(input('marks scored; '))

if vijaymarks <= 60:
    print('study hard')
elif vijaymarks <= 70:
    print('screening round')
elif vijaymarks <= 80:
    print('second round')
else:
    print('first round')
marks scored; 45
study hard
Vijaymarks = int(input('marks scored; '))

if vijaymarks <= 60:
    print('study hard')
elif vijaymarks <= 70:
    print('screening round')
elif vijaymarks <= 80:
    print('second round')
else:
    print('first round')
marks scored; 61
screening round
vijaymarks = int(input('marks scored; '))

if vijaymarks <= 60:
    print('study hard')
elif vijaymarks <= 70:
    print('screening round')
elif vijaymarks <= 80:
    print('second round')
else:
    print('first round')
marks scored; 74
second round
vijaymarks = int(input('marks scored; '))

if vijaymarks <= 60:
    print('study hard')
elif vijaymarks <= 70:
    print('screening round')
elif vijaymarks <= 80:
    print('second round')
else:
    print('first round')
marks scored; 89
first round


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





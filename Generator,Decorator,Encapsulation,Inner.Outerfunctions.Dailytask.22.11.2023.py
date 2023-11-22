#!/usr/bin/env python
# coding: utf-8

# #Generator
# 
# In Python, a generator is a special type of iterable, similar to a list or a tuple, but it doesn't store all the values in memory at once. Instead, it generates values on-the-fly using a special kind of function called a generator function.
# 
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
# 
# -# Using the generator
# gen = simple_generator()
# 
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3
# -# print(next(gen))  # Uncommenting this line would raise StopIteration error since there are no more values
# 
# -# Alternatively, you can use a for loop to iterate over the generator
# for value in simple_generator():
#     print(1,2,3)
# -# Output:
# -# 1
# -# 2
# -# 3
# 
# In the example above, simple_generator is a generator function because it contains the yield keyword. When called, it returns a generator object. The values are generated one at a time using the next() function.
# 
# Generators are useful for iterating over large datasets efficiently because they generate values on demand and don't store the entire sequence in memory.

# #Decorator
# 
# In Python, a decorator is a design pattern and a syntactic shortcut that allows you to extend or modify the behavior of functions or methods without changing their code. Decorators are often used to add functionality to functions, such as logging, timing, or access control.
# 
# Here's a basic example of how a decorator works:
# 
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
# 
# @my_decorator
# def say_hello():
#     print("Hello!")
# 
# -# Calling the decorated function
# say_hello()
# 
# In this example, my_decorator is a decorator function that takes another function (func) as its argument and returns a new function (wrapper). The wrapper function contains code that is executed before and after the original function (func) is called.

# #Class and Objects
# 
# In Python, a class is a blueprint for creating objects, and an object is an instance of a class. Here are some short notes on classes and objects in Python:
# 
# Class Definition:
# 
# A class is defined using the class keyword.
# It encapsulates data (attributes) and functions (methods) that operate on the data.
# 
# class MyClass:
# -#### Attributes and methods go here
# 
# --------------------------------------------------------------------------------------------------------------------------------
# Object Instantiation:
# 
# Objects are created by instantiating a class.
# The __init__ method is a special method called the constructor, which is used for initializing the object's attributes.
# class MyClass:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
# 
# -# Creating an object
# -obj = MyClass(value1, value2)
# 
# -------------------------------------------------------------------------------------------------------------------------------
# Attributes:
# 
# Attributes are variables that store data within an object.
# They are accessed using dot notation (obj.attribute).
# 
# print(obj.attribute1)
# 
# --------------------------------------------------------------------------------------------------------------------------------
# Methods:
# 
# Methods are functions defined within a class that operate on the object's data.
# The first parameter of a method is conventionally named self and refers to the instance of the object.
# 
# class MyClass:
#     def my_method(self):
#         print("This is a method")
# 
# -# Creating an object
# obj = MyClass()
# obj.my_method()
# 
# --------------------------------------------------------------------------------------------------------------------------------
# Inheritance:
# 
# Inheritance allows a class to inherit attributes and methods from another class.
# The super() function is used to call a method from the parent class.
# 
# class ParentClass:
#     def parent_method(self):
#         print("Parent method")
# 
# class ChildClass(ParentClass):
#     def child_method(self):
#         super().parent_method()
#         print("Child method")
# 
# -# Creating an object of the child class
# obj = ChildClass()
# obj.child_method()
# 
# -------------------------------------------------------------------------------------------------------------------------------
# Encapsulation:
# 
# Encapsulation restricts access to certain attributes or methods, typically by using private and protected access modifiers.
# Private attributes/methods are denoted by a double underscore (__).
# 
# class MyClass:
#     def __init__(self):
#         self.__private_attribute = 42
# 
#     def get_private_attribute(self):
#         return self.__private_attribute
# --------------------------------------------------------------------------------------------------------------------------------
# Polymorphism:
# 
# Polymorphism allows objects to be treated as instances of their parent class.
# It enables different classes to be used interchangeably.
# 
# class Dog:
#     def speak(self):
#         return "Woof!"
# 
# class Cat:
#     def speak(self):
#         return "Meow!"
# 
# def animal_sound(animal):
#     print(animal.speak())
# 
# dog = Dog()
# cat = Cat()
# 
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!
# 
# --------------------------------------------------------------------------------------------------------------------------------

# In[4]:


#Sample Private Attribute

class Stu:
    def __init__(self, *marks):
        self.marks = marks
        self.passmark = 40
    def res(self):
        return 'Fail' if min(self.marks) < self.passmark else 'pass'


# In[5]:


x =Stu(*[10,20,30,50])


# In[6]:


x.res()


# In[9]:


x.__passmark = 1


# In[12]:


x.res()


# In[7]:


print(dir(x))


# ##Private Attribute
# 
# In Python, you can make an attribute private by prefixing its name with double underscores (__). This convention is used to indicate that the attribute is intended to be private and should not be accessed directly from outside the class. However, it's important to note that this is more of a naming convention than a strict access control mechanism; Python does not have true "private" members in the way some other languages do.
# 
# Here's an example:
# 
# class MyClass:
#     def __init__(self):
#         # Public attribute
#         self.public_attribute = 10
#         # Private attribute
#         self.__private_attribute = 20
# 
#     def get_private_attribute(self):
#         return self.__private_attribute
# 
# -# Creating an object
# obj = MyClass()
# 
# -# Accessing public attribute
# print(obj.public_attribute)  # Output: 10
# 
# -# Accessing private attribute directly would raise an AttributeError
# -# Uncommenting the following line would result in an error
# -# print(obj.__private_attribute)
# 
# -# Accessing private attribute through a method
# print(obj.get_private_attribute())  # Output: 20
# In this example, public_attribute is a public attribute that can be accessed directly, while __private_attribute is a private attribute. Attempting to access __private_attribute directly from outside the class would result in an AttributeError. To access the private attribute, a method (get_private_attribute) is provided, which is a common practice in Python to implement controlled access to private members.
# 
# It's worth noting that although the double underscore prefix provides a level of name mangling (changing the name to include the class name to make it harder to accidentally override in subclasses), it does not make the attribute truly private or protected. It's still technically possible to access it if you really want to. The use of a single underscore (e.g., _private_attribute) is often used to indicate that an attribute is intended to be protected or private, without the name 
# 

# #Class Method
# 
# In Python, a class method is a method that is bound to the class and not the instance of the class. Class methods are defined using the @classmethod decorator. They take the class itself as the first parameter, conventionally named cls.
# 
# Here's an example:
# 
# class MyClass:
#     class_variable = "I am a class variable"
# 
#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable
# 
#     def instance_method(self):
#         print(f"Instance method called with instance_variable: {self.instance_variable}")
# 
#     @classmethod
#     def class_method(cls):
#         print(f"Class method called with class_variable: {cls.class_variable}")
# 
# -# Creating an object
# obj = MyClass("instance_value")
# 
# -# Calling instance method
# obj.instance_method()
# 
# -# Calling class method
# MyClass.class_method()
# 
# In this example:
# 
# instance_method is a regular instance method. It is called on an instance of the class, and it has access to the instance's attributes.
# 
# class_method is a class method. It is defined using the @classmethod decorator. It takes the class (cls) as its first parameter and can access class-level variables.
# 
# Class methods are often used for tasks that involve the class itself rather than instances of the class. For example, they can be used to create class-level utility methods, initialize class-level variables, or perform other operations that are related to the class but don't depend on a specific instance.
# 
# It's important to note that class methods can be called on the class itself or on an instance of the class. When called on an instance, the class method still receives the class as its first parameter.

# In[19]:


def fooOuter(f):
    def fooInner():
        print('*'*5)
        f()
        print('*'*5)
    return fooInner()


# In[20]:


def abc():
    print('hello')


# In[21]:


fooOuter(abc)


# In[26]:


@fooOuter #Decorator   
def abc():
    print('12345')


# #Decorator
# 
# In Python, a decorator is a design pattern and a syntactic construct that allows you to extend or modify the behavior of functions or methods without changing their code. Decorators are often used to add functionality such as logging, timing, or access control to functions. Decorators are applied using the @decorator_name syntax.
# 
# Here's a simple example of a decorator:
# 
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
# 
# @my_decorator
# def say_hello():
#     print("Hello!")
# 
# -# Calling the decorated function
# say_hello()
# 
# In this example:
# 
# my_decorator is a decorator function that takes another function (func) as its argument and returns a new function (wrapper). The wrapper function contains code that is executed before and after the original function (func) is called.
# 
# @my_decorator is a shorthand way of applying the decorator to the say_hello function. It is equivalent to writing say_hello = my_decorator(say_hello).

# In[52]:


def fooOuter(f,*args,**kwargs):
    def fooInner(*args,**kwargs):
        print('*'*5)
        f(*args,**kwargs)
        print('*'*5)
    return fooInner


# In[53]:


@fooOuter #decorator
def abc(a,b,c):
    '''abc func call'''
    print(a+b+c)


# In[54]:


abc(1,2,3)


# In[ ]:


import functools


# In[31]:


from functools import wraps


# In[57]:


def fooOuter(f):
    '''outer'''
    @wraps(f)
    def fooInner():
        '''Inner'''
        print('*'*5)
        f()
        print('*'*5)
    return fooInner


# #Decorator sample
# 
# In Python, a decorator is a design pattern that allows you to extend or modify the behavior of functions or methods without modifying their actual code. Decorators are applied using the "@" symbol followed by the decorator name, placed above the function definition.
# 
# Here are some examples of decorators in Python:
# 
# Example 1: Simple decorator
# 
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
# 
# @my_decorator
# def say_hello():
#     print("Hello!")
# 
# -# Using the decorated function
# say_hello()
# Output:
# 
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# 

# #Wrapper function
# 
# In Python, a wrapper function is a function that "wraps around" another function or method. It is commonly used in the context of decorators, where the wrapper function is returned by the decorator to modify or extend the behavior of the original function. The wrapper function typically calls the original function and may perform additional actions before or after the call.
# 
# Here's a simple example of a wrapper function:
# 
# def my_wrapper(func):
#     def wrapper(*args, **kwargs):
#         print("Do something before calling the function")
#         result = func(*args, **kwargs)
#         print("Do something after calling the function")
#         return result
#     return wrapper
# 
# @my_wrapper
# def my_function():
#     print("Inside the function")
# 
# -# Using the decorated function
# my_function()
# 
# Output:
#     
# Do something before calling the function
# Inside the function
# Do something after calling the function
# In this example, my_wrapper is a decorator that takes a function (func) as its argument and returns a new function (wrapper). The wrapper function is the actual wrapper that is called instead of my_function when we use the @my_wrapper syntax.
# 
# The wrapper function takes any number of arguments (*args) and keyword arguments (**kwargs). It prints a message before calling the original function (func), then calls the original function, captures its result, prints another message after the call, and finally returns the result.

# #@ data class
# The @dataclass decorator in Python is part of the dataclasses module introduced in Python 3.7. It provides a convenient way to create classes that are primarily used to store data. With @dataclass, you can automatically generate special methods, such as __init__, __repr__, and __eq__, based on the class attributes. This can lead to more concise and readable code.
# 
# Here's a simple example to illustrate the use of @dataclass:
# 
# 
# from dataclasses import dataclass
# 
# @dataclass
# class Point:
#     x: int
#     y: int
# 
# In this example, the @dataclass decorator automatically adds the __init__, __repr__, and __eq__ methods to the Point class. Now, you can create instances of Point without explicitly defining these methods:
# 
# 
# -# Creating instances
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# 
# #- __repr__ method
# print(p1)  # Output: Point(x=1, y=2)
# 
# -# __eq__ method
# print(p1 == p2)  # Output: True

# #Use Cases for @dataclass:
# A dataclass in python is a specially structured class that is optimized for the storage and representation of data. Dataclasses have certain in-built functions to look after the representation of data as well as its storage.
# 
# Dataclasses in python require the dataclasses library that has the dataclass module inside it. A library is a collection of modules that provide pre-defined functionalities.
# 
# Libraries are made up of the code that is required to implement the module. Once we have imported the dataclasses library we will import the dataclass module from the library. After we have imported the dataclass module, we will use decorators to provide the properties of a dataclass to the new class that we create.
# 
# dataclasses are specifically used for the representation of data and its storage. Therefore the two most popular use cases of dataclasses are for printing a class and for equality checks.
# 

# #Inner function
# 
# Inner functions, also known as nested functions, are functions that you define inside other functions. In Python, this kind of function has direct access to variables and names defined in the enclosing function. Inner functions have many uses, most notably as closure factories and decorator functions.
# 
# 
# #Example
# def outer_func():
#      def inner_func():
#          print("Hello, World!")
#      inner_func()
# 
# 
# outer_func()
# Hello, World!
# 
# ---------------------------------------------------------------------------------------------------------------------------------
# #Outer function
# 
# outer function refers to a function that contains another function, known as an inner function. The outer function is typically responsible for some setup or configuration, and it may return the inner function or use it in some way. The inner function has access to the variables of the outer function, creating a closure.
# 
# #Example
# def outer_function(a):
#   def inner_function(b):
#     return a + b
#   return inner_function
# 
# result = outer_function(5)(3)
# print(result)

#!/usr/bin/env python
# coding: utf-8

# # Functions
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
# 
# # Calling the function with both arguments
# greet("VJ", "Hi")  # Output: "Hi, Alice!"
# 
# # Calling the function with only one argument
# greet("Vijay")  # Output: "Hello, Bob!"

# # Function Concatination
# def VJconcatinationofstring(s1,s2='',n=1):
#     print((s1+s2)*n)
# 
# VJconcatinationofstring('ha', s2='hurray')

# # Positional arguments
# Positional arguments are the most basic type of arguments in programming functions.
# They are the arguments passed to a function in a specific order, and their values are assigned to the corresponding parameters in the same order.
# The order in which you pass these arguments is important because the function matches them based on their position.
# 
# def add(a, b):
#     return a + b
# 
# result = add(5, 3)
# print(result)  # Output: 8

# # Keyword arguments
# Keyword arguments, also known as named arguments, are a way to pass arguments to a function by specifying the parameter name along with the value.
# This allows you to provide arguments to a function in any order, and it can make your code more readable and self-explanatory.
# 
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
# 
# # Calling the function with keyword arguments
# greet(name="Alice", greeting="Hi")  # Output: "Hi, Alice!"
# 
# # Calling the function with keyword arguments in a different order
# greet(greeting="Howdy", name="Bob")  # Output: "Howdy, Bob!"

# # Default arguments
# Default arguments, also known as default parameter values, allow you to define default values for parameters in a function. If a caller of the function doesn't provide a value for a parameter, the default value is used instead. This can make your functions more flexible and user-friendly, as it allows for optional arguments without requiring the caller to provide a value for every parameter.
# 
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
# 
# # Calling the function with both arguments
# greet("Alice", "Hi")  # Output: "Hi, Alice!"
# 
# # Calling the function with only one argument
# greet("Bob")  # Output: "Hello, Bob!"

#!/usr/bin/env python
# coding: utf-8

# Module------------------------------------------------------------------------------------------------------------------------------
# 
# module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Modules allow you to organize code logically into reusable units. You can use modules to break down a large program into smaller, manageable files, making your code more modular and easier to maintain.
# 
# #Package
# package is a way of organizing related modules into a single directory hierarchy. A package is a collection of Python modules in directories that have a special file called __init__.py. This file can be empty, but it's required to treat the directories as containing packages.
# 
# #Command Line
# Run command line scripts directly from the IPython console or the built-in terminal.
# 
# Open Spyder.
# 
# Write or open your Python script in the editor.
# 
# Open the IPython console (usually located at the bottom-right of the Spyder window).
# 
# IPython Console
# 
# Navigate to the directory where your script is located using the cd command.
# cd path/to/your/script
# 
# 
# cd path/to/your/script
# Run your script using the %run magic command.
# %run your_script.py
# 
# Replace your_script.py with the name of your Python script.

# #Scope of Variable
# 
#  the scope of a variable refers to the region of the code where the variable can be accessed or modified. Python has the following types of variable scopes:
# 
# Local Scope:
# 
# A variable defined inside a function has a local scope.
# It is only accessible within that function.
# It is created when the function is called and destroyed when the function exits.
# def my_function():
#     x = 10  # local variable
#     print(x)
# 
# my_function()
# 
# print(x)  # This would result in an error because x is not defined in the global scope.
# 
# --------------------------------------------------------------------------------------------------------------------------------
# Enclosing (Nonlocal) Scope:
# 
# An enclosing scope occurs in nested functions.
# It allows a variable to be nonlocal to an inner function but still accessible.
# Used with the nonlocal keyword.
# def outer_function():
#     y = 20  # outer_function's local variable
# 
#     def inner_function():
#         nonlocal y
#         y += 5  # y is nonlocal to inner_function
# 
#     inner_function()
#     print(y)  # Output: 25
# 
# outer_function()
# 
# --------------------------------------------------------------------------------------------------------------------------------
# Global Scope:
# 
# A variable defined at the top level of a script or module has a global scope.
# It is accessible throughout the entire script or module.
# Use the global keyword to indicate that a variable is global.
# z = 30  # global variable
# 
# def my_function():
#     global z
#     print(z)
# 
# my_function()  # Output: 30
# 
# -------------------------------------------------------------------------------------------------------------------------------
# Built-in Scope:
# 
# Python has a built-in scope that includes names like print, len, etc.
# These names are always accessible from any part of the code.
# print("Hello, built-in scope!")
# 
# Python follows the LEGB (Local, Enclosing, Global, Built-in) rule to resolve the scope of a variable. When a variable is referenced, Python searches for it in the following order: local scope, enclosing scope (if applicable), global scope, and finally the built-in scope.

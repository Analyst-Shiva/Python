#!/usr/bin/env python
# coding: utf-8

# call by value:
# When Immutable objects such as whole numbers, strings, etc are passed as arguments to the function call, the it can be considered as Call by Value.
# This is because when the values are modified within the function, then the changes do not get reflected outside the function.
# Primitive data types (such as integers, floats, characters) usually follow call by value.
# In call by value, a copy of the actual parameter's value is passed to the function.
# The function receives a copy of the value stored in the variable and works with that copy.
# Any changes made to the parameter within the function do not affect the original value in the calling code.
# def modify_value(num):
#     num += 10
#     print("Inside the function:", num)
# 
# value = 5
# modify_value(value)  # Passing the value by value
# print("Outside the function:", value)
# Inside the function: 15
# Outside the function: 5
# 
# ------------------------------------------------------------------
# Call by Reference:
# In call by reference, instead of passing a copy of the value, a reference or address (pointer) to the variable is passed to the function.
# This means the function can directly access and modify the original value in the calling code using the reference or pointer.
# Objects, arrays, and sometimes pointers to variables can be passed by reference.
# Changes made to the parameter within the function affect the original variable outside the function.
# Pass means to provide an argument to a function. By reference means that the argument you're passing to the function is a reference to a variable that already exists in memory rather than an independent copy of that variable.
# def modify_list(my_list):
#     my_list.append(4)
#     print("Inside the function:", my_list)
# 
# original_list = [1, 2, 3]
# modify_list(original_list)  # Passing the list by reference
# print("Outside the function:", original_list)
# Inside the function: [1, 2, 3, 4]
# Outside the function: [1, 2, 3, 4]
# 

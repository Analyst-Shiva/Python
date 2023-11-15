#!/usr/bin/env python
# coding: utf-8

# #Module
# 
# #How to create a module in Spyder
# 
# Spyder, which is an integrated development environment (IDE) for Python, creating a module is essentially the same as creating a Python script or file. A module in Python is simply a file containing Python definitions and statements.
# 
# Open Spyder:
# Start Spyder on your computer. If you don't have Spyder installed, you can install it using a package manager like conda or pip.
# 
# Create a New File:
# 
# Click on the "File" menu.
# Select "New File" or use the keyboard shortcut Ctrl + N (Cmd + N on macOS).
# Write Your Code:
# 
# Write the Python code that you want to include in your module.
# For example, let's create a simple module with a function:
# 
# -------------------------------------------------------------------------------------------------------------------------------# mymodule.py
# 
# def greet(name):
#     print(f"Hello, {name}!")
# 
#     Save the File:
# 
# Click on the "File" menu.
# Select "Save" or use the keyboard shortcut Ctrl + S (Cmd + S on macOS).
# Choose a location and enter a filename with the .py extension (e.g., mymodule.py).
# Run the Module (Optional):
# 
# You can run the module to check if everything is working as expected.
# Use the "Run" button or the keyboard shortcut F5.
# Use the Module in Another Script:
# 
# To use the module in another script, you can import it using the import statement.
# For example, in another script (e.g., main.py), you can use the greet function from mymodule
# 
# -------------------------------------------------------------------------------------------------------------------------------# main.py
# import mymodule
# 
# mymodule.greet("John")
# 
# When you run main.py, it will import and use the greet function from your mymodule module.

# #math module
# 
# Import the math Module:
# To use functions from the math module, you need to import it first.
# 
# 
# import math
# 
# -------------------------------------------------------------------------------------------------------------------------------# Basic arithmetic operations
# print(math.sqrt(25))  # Square root: 5.0
# print(math.pow(2, 3))  # Power: 8.0
# 
# -------------------------------------------------------------------------------------------------------------------------------# Trigonometric functions (input in radians)
# print(math.sin(math.radians(30)))  # Sine of 30 degrees: 0.5
# print(math.cos(math.radians(60)))  # Cosine of 60 degrees: 0.5
# 
# -------------------------------------------------------------------------------------------------------------------------------# Logarithmic functions
# print(math.log(16, 2))  # Log base 2 of 16: 4.
# 
# -------------------------------------------------------------------------------------------------------------------------------# Constants
# print(math.pi)  # Pi: 3.141592653589793
# print(math.e)   # Euler's number: 2.718281828459045
# 
# -------------------------------------------------------------------------------------------------------------------------------## triangle_module.py
# 
# def area(base, height):
#     """
#     Calculate the area of a triangle.
# 
#     Parameters:
#     - base: The length of the base of the triangle.
#     - height: The height of the triangle.
# 
#     Returns:
#     - The area of the triangle.
#     """
#     return 0.5 * base * height

# -# Physics modules
# -------------------------------------------------------------------------------------------------------------------------------Create a new file, for example, physics_formulas.py.
# 
# Write the following code in the file: # physics_formulas.py
# 
# import math
# 
# --------------------------------------------------------------------------------------------------------------------------------
# def velocity(initial_velocity, acceleration, time):
#     """
#     Calculate the final velocity using the kinematic equation: v = u + at.
# 
#     Parameters:
#     - initial_velocity: Initial velocity.
#     - acceleration: Acceleration.
#     - time: Time.
# 
#     Returns:
#     - Final velocity.
#     """
#     return initial_velocity + acceleration * time
# --------------------------------------------------------------------------------------------------------------------------------
# def force(mass, acceleration):
#     """
#     Calculate force using Newton's second law: F = ma.
# 
#     Parameters:
#     - mass: Mass of the object.
#     - acceleration: Acceleration.
# 
#     Returns:
#     - Force.
#     """
#     return mass * acceleration
# --------------------------------------------------------------------------------------------------------------------------------
# def kinetic_energy(mass, velocity):
#     """
#     Calculate kinetic energy using the formula: KE = 0.5 * m * v^2.
# 
#     Parameters:
#     - mass: Mass of the object.
#     - velocity: Velocity of the object.
# 
#     Returns:
#     - Kinetic energy.
#     """
#     return 0.5 * mass * velocity**2
# --------------------------------------------------------------------------------------------------------------------------------
# def gravitational_force(mass1, mass2, distance):
#     """
#     Calculate gravitational force using Newton's law of gravitation: F = G * (m1 * m2) / r^2.
# 
#     Parameters:
#     - mass1: Mass of the first object.
#     - mass2: Mass of the second object.
#     - distance: Distance between the centers of the masses.
# 
#     Returns:
#     - Gravitational force.
#     """
#     gravitational_constant = 6.67430e-11
#     return gravitational_constant * (mass1 * mass2) / distance**2
# --------------------------------------------------------------------------------------------------------------------------------
# def work_done(force, distance, angle=0):
#     """
#     Calculate work done using the formula: W = F * d * cos(theta).
# 
#     Parameters:
#     - force: Force applied.
#     - distance: Distance over which the force is applied.
#     - angle: Angle between the force and the direction of motion (default is 0).
# 
#     Returns:
#     - Work done.
#     """
#     return force * distance * math.cos(math.radians(angle))
# -------------------------------------------------------------------------------------------------------------------------------
# save the file
# 
# use the specific function required.

# #Packages
# 
# package is a way of organizing related modules into a single directory hierarchy. It provides a way of grouping related functionality together. A package is essentially a directory that contains a special file called __init__.py, which can be empty or can contain Python code. This file indicates that the directory should be treated as a package.
# 
# 
# Creating a Package:
# To create a package, you need to organize your modules into a directory and place an __init__.py file inside that directory. 

#!/usr/bin/env python
# coding: utf-8

# Class
# In object-oriented programming (OOP), a class is a blueprint for creating objects, and an object is an instance of a class. OOP is a programming paradigm that uses objects, which can contain data in the form of fields (often known as attributes or properties) and code, in the form of procedures (often known as methods). Classes are used to define the properties and behaviors that objects of the class should have.
# 
# Here's a basic explanation of classes and objects in Python, a popular programming language that supports OOP:
# 
# class MyClass:
#     # Class variable
#     class_variable = "I am a class variable"
# 
#     # Constructor method (called when an object is created)
#     def __init__(self, attribute1, attribute2):
#         # Instance variables
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
# 
#     # Instance method
#     def display_attributes(self):
#         print(f"Attribute 1: {self.attribute1}")
#         print(f"Attribute 2: {self.attribute2}")
# 
#     # Class method (operates on the class and its class variables)
#     @classmethod
#     def display_class_variable(cls):
#         print(f"Class Variable: {cls.class_variable}")
# 
# -# Creating objects (instances) of the class
# object1 = MyClass("Value 1", "Value 2")
# object2 = MyClass("Another Value 1", "Another Value 2")
# 
# -# Accessing instance variables and calling instance methods
# object1.display_attributes()
# 
# -# Accessing class variable using class method
# MyClass.display_class_variable()
# 
# In this example:
# 
# MyClass is the class.
# object1 and object2 are instances of the MyClass class.
# attribute1 and attribute2 are instance variables, and class_variable is a class variable.
# display_attributes is an instance method that can be called on objects.
# display_class_variable is a class method that can be called on the class itself.
# Remember that this is a simple example, and OOP can involve more advanced concepts such as inheritance, polymorphism, and encapsulation, which allow for more sophisticated and modular code design.

# #Objects
# 
# In Python, everything is an object. When we say "everything," we mean that even basic data types like integers, floats, strings, and functions are objects. An object in Python is a collection of data (variables) and methods (functions) that operate on the data. Objects are instances of classes, and classes define the blueprint for the objects.
# 
# Here are some examples of objects in Python:
# 
# 1. Integer Object:
# -# Integer object
# x = 5
# print(type(x))  # <class 'int'>
# 
# 2. String Object:
# -# String object
# message = "Hello, World!"
# print(type(message))  # <class 'str'>
# 
# 3. List Object:
# -# List object
# my_list = [1, 2, 3, 4, 5]
# print(type(my_list))  # <class 'list'>
# 
# 4. Function Object:
# -# Function object
# def my_function():
#     print("This is a function")
# 
# print(type(my_function))  # <class 'function'>
# 
# 
# 5. Custom Class Object:
# -# Custom class and object
# class MyClass:
#     def __init__(self, attribute):
#         self.attribute = attribute
# 
# my_object = MyClass("Some value")
# print(type(my_object))  # <class '__main__.MyClass'>
# In the last example, MyClass is a custom class, and my_object is an instance of that class. This demonstrates how you can create your own objects by defining classes.
# 
# Understanding that everything in Python is an object is important for grasping the object-oriented nature of the language. Objects in Python can have attributes (data) and methods (functions), and they can be manipulated, passed around, and used in a variety of ways within the language.

# In[1]:


#Sample 1

class Student:
    def __init__(self,fname,lname,gender,dob):
        self.name = fname
        self.name = lname
        self.name = fname+' '+lname
        self.dob = dob
        self.gender = gender
        self.email = fname+lname[:2]+dob[-2:]+'@stu.com'  


# In[2]:


stu1 = Student('Ram', 'Koti', 'Male', '01-01-1888')


# In[3]:


stu1.email


# In[4]:


#Sample 2

class Student:
    def __init__(self,fname,lname,gender,dob):
        self.name = fname
        self.name = lname
        self.name = fname+' '+lname
        self.dob = dob
        self.gender = gender
        self.email = fname+lname[:2]+dob[-2:]+'@stu.com'  
        self.fun = self.xyz()
    def xyz(self):
        return 'abcdef'


# In[5]:


stu1 = Student('ram', 'koti','male','01-01-1888')


# In[6]:


stu1.email


# In[ ]:


#Sample 3 #Include Marks and Percentage

class Student:
    def __init__(self, fname, lname, gender, dob, marks):
        self.first_name = fname
        self.last_name = lname
        self.full_name = fname + ' ' + lname
        self.dob = dob
        self.gender = gender
        self.email = fname + lname[:2] + dob[-2:] + '@stu.com'
        self.marks = marks

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

# Example usage
student1 = Student("John", "Doe", "Male", "01012000", [90, 85, 75, 95, 88])
student2 = Student("Jane", "Smith", "Female", "02022001", [78, 92, 88, 85, 90])

# Accessing attributes and calculating percentage
print(f"{student1.full_name}'s percentage: {student1.calculate_percentage():.2f}%")
print(f"{student2.full_name}'s percentage: {student2.calculate_percentage():.2f}%")

The Student class now has a new attribute marks, which is a list representing the marks obtained in various subjects.
The calculate_percentage method calculates the percentage based on the total marks and the number of subjects. It then returns the calculated percentage.
You can now create instances of the Student class with marks information and calculate the percentage for each student.


# In[15]:


#Sample 4

class Student:
    def __init__(self, fname, lname, gender, dob, *marks):
        self.first_name = fname
        self.last_name = lname
        self.full_name = fname + ' ' + lname
        self.dob = dob
        self.gender = gender
        self.email = fname + lname[:2] + dob[-2:] + '@stu.com'
        self.marks = marks
        self.avg = self.result()[0]
        self.result = self.result()[1]
    def result(self):
        avg = sum(self.marks)/len(self.marks)
        if min(self.marks) <40:
            return avg, 'Fail'
        elif avg <60:
            return avg, 'SecondClass'
        elif avg < 80:
            return avg, 'FirstClass'
        else:
            return avg, 'FCWD'


# In[22]:


stu1 = Student('ram', 'koti','male','01-01-1888', *[39,90,90,90,90])


# In[19]:


stu1.avg


# #Class and Objects with an example:
# 
# In Python, a class is a blueprint for creating objects, and an object is an instance of a class. Classes define the properties (attributes) and behaviors (methods) that objects of the class should have. Here's a simple example of a class and objects in Python:
# 
# class Dog:
#     # Class attribute
#     species = "Canis familiaris"
# 
#     # Initializer / Instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"
# 
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
# 
# -# Creating instances (objects) of the Dog class
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Milo", 2)
# 
# -# Accessing attributes and calling methods
# print(f"{dog1.name} is a {dog1.species}")
# print(dog2.description())
# print(dog1.speak("Woof"))
# 
# -# Output:
# -# Buddy is a Canis familiaris
# -# Milo is 2 years old
# -# Buddy says Woof
# 
# 
# In this example:
#     
# We define a Dog class with a class attribute species, an initializer (__init__) method to set instance attributes (name and age), and two instance methods (description and speak).
# We create two instances of the Dog class, dog1 and dog2, each with its own set of attributes.
# We access the attributes and call methods on the instances to retrieve information about them.
# This is a basic example, but it demonstrates the concept of classes and objects in Python. Classes allow you to encapsulate data and behavior into reusable components, making your code more organized and modular.

# #Class method and #Instance method
# 
# In Python, class methods and instance methods are two types of methods associated with classes.
# 
# Instance Method:
# 
# An instance method is a method that operates on an instance of the class.
# It takes self as its first parameter, which refers to the instance calling the method.
# Instance methods can access and modify the attributes of the instance.
# 
# Example:
# 
# 
# class MyClass:
#     def __init__(self, value):
#         self.value = value
# 
#     def print_value(self):
#         print(self.value)
# 
# obj = MyClass(42)
# obj.print_value()  # Output: 42
# 
# -------------------------------------------------------------------------------------------------------------------------------
# Class Method:
# 
# A class method is a method that operates on the class itself rather than on instances of the class.
# It takes cls as its first parameter, which refers to the class.
# Class methods can access and modify class-level attributes.
# 
# Example:
# 
# 
# class MyClass:
#     class_variable = 10
# 
#     def __init__(self, value):
#         self.value = value
# 
#     @classmethod
#     def print_class_variable(cls):
#         print(cls.class_variable)
# 
# MyClass.print_class_variable()  # Output: 10
# In the example above, @classmethod is a decorator that indicates that the following method is a class method. It takes cls (conventionally named) as its first parameter.
# 
# Here's a more complete example with both instance and class methods:
# 
# class MyClass:
#     class_variable = 10
# 
#     def __init__(self, value):
#         self.value = value
# 
#     def instance_method(self):
#         print(f"Instance method called with value: {self.value}")
# 
#     @classmethod
#     def class_method(cls):
#         print(f"Class method called with class variable: {cls.class_variable}")
# 
# -# Instance method
# obj = MyClass(42)
# obj.instance_method()
# 
# -# Class method
# MyClass.class_method()
# In summary, instance methods are associated with instances and can access and modify instance-specific attributes, while class methods are associated with the class and can access and modify class-level attributes.

# In[23]:


#Instance Attributes are object level attributes, these may or may not have same avalues across all OBJECTS.


# In[54]:


class Stu:
    def __init__(self, *marks):
        self.marks = marks
        self.passmark = 40
    def res(self):
        return 'Fail' if min(self.marks) < self.passmark else 'pass'


# In[55]:


x =Stu(*[10,20,30,50])


# In[56]:


x.res()


# In[64]:


class FooClass():
    def __init__ (self,*marks):
        self.passmark = 40
        self.marks = marks
    def result(self):
        return 'Fail' if min(self.marks)< self.passmark else 'Success'
    


# In[65]:


x = FooClass (*[32,50,45])


# In[66]:


x.result()


# In[67]:


x.passmark


# In[69]:


#static Attribute
#Class-level attributes are shared among all instances of a class, and they are accessed using the class name rather than an instance of the class.

class FooClass:
    passmark = 40
    
    def __init__(self,*marks):
        self.marks = marks
    def result(self):
        return 'Fail' if min(self.marks)< self.passmark else 'succcess'


# In[70]:


x = FooClass(*[23,56])


# In[71]:


x.result()


# In[72]:


x.passmark = 1


# In[73]:


x.passmark


# In[74]:


x.result()


# In[75]:


#Fibonacci

def fibonacci(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    
    return fib_series

# Get the first 10 values of the Fibonacci series
fibonacci_values = fibonacci(10)

print("Fibonacci Series (first 10 values):", fibonacci_values)


#In this example:

#The fibonacci function generates the Fibonacci series up to n values.
#The function starts with the initial values [0, 1] and iteratively calculates the next values by adding the last two values in the series.
#The result is a list containing the first 10 values of the Fibonacci series.


# In[76]:


#Climb Staircase

#Python function to calculate the number of ways to climb a staircase, where you can climb either 1 or 2 steps at a time, you can use a recursive approach or dynamic programming. Here, I'll provide an example using a recursive function:

def climb_stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # The number of ways to climb n stairs is the sum of the ways to climb (n-1) and (n-2) stairs
        return climb_stairs(n - 1) + climb_stairs(n - 2)

# Example usage
num_ways = climb_stairs(5)
print(f"Number of ways to climb 5 stairs: {num_ways}")


#In this example:

#The climb_stairs function is a recursive function that calculates the number of ways to climb a staircase with n steps.
#The base cases handle situations where there are 0, 1, or 2 steps, as those are the trivial cases.
#For n greater than 2, the function recursively calculates the number of ways to climb (n-1) and (n-2) stairs and returns their sum.
#However, note that the recursive solution can be inefficient for large values of n due to redundant calculations. In such cases, a dynamic programming approach with memoization or iteration might be more su


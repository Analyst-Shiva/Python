#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Construct Overload

class OverloadedClass:
    def overloaded_method(self, *args):
        if len(args) == 1:
            self.method_with_one_argument(args[0])
        elif len(args) == 2:
            self.method_with_two_arguments(args[0], args[1])
        else:
            print("Unsupported number of arguments")

    def method_with_one_argument(self, arg1):
        print("Method with one argument:", arg1)

    def method_with_two_arguments(self, arg1, arg2):
        print("Method with two arguments:", arg1, arg2)

# Create an instance of the class
obj = OverloadedClass()

# Call the overloaded method with different argument counts
obj.overloaded_method(10)
obj.overloaded_method(20, 30)
obj.overloaded_method(40, 50, 60)


# In[19]:


#Construct Overload

class MyClass:

    def __init__(self, a=None, b=None, fname=None, lname=None):
        if a is not None and b is not None:
            # Case for int, int
            self._init_int(a, b)
        elif fname is not None and lname is not None:
            # Case for str, str
            self._init_str(fname, lname)
        else:
            raise TypeError("Invalid argument types for init")

    def foo(self, x, y=None, m=None, n=None):
        if y is not None:
            # Case for int, int
            return self._foo_int(x, y)
        elif m is not None and n is not None:
            # Case for set, set
            return self._foo_set(m, n)
        else:
            raise TypeError("Invalid argument types for foo")

    def _foo_int(self, x, y):
        return x * y

    def _foo_set(self, m, n):
        return m.union(n)

    def _init_int(self, a, b):
        self.x = a * b

    def _init_str(self, fname, lname):
        self.name = fname + lname


# Example usage:
# Using init method (automatically called)
obj1 = MyClass(a=2, b=3)
print(obj1.x)  # Output: 6

obj2 = MyClass(fname="THE", lname="Vijay")
print(obj2.name)  # Output: THEVijay


# In[ ]:


# Method Override

#In object-oriented programming, method overriding is a concept where a subclass provides a specific implementation for a method that is already defined in its superclass. The overridden method in the subclass has the same signature (name, return type, and parameters) as the method in the superclass. This allows the subclass to provide its own implementation of the method while maintaining a consistent interface with the superclass.

#Here's an example in Python:

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the overridden method
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
-------------------------------------------------------------------------------------------------------------------------------
In this example, Dog and Cat are subclasses of the Animal class. Both Dog and Cat override the make_sound method defined in the Animal class with their own implementations. When you call make_sound on instances of Dog or Cat, the overridden method in the respective subclass is executed.

Key points about method overriding:

Inheritance: Method overriding is closely related to inheritance, as it involves providing a specialized implementation in a subclass for a method that is inherited from a superclass.

Signature Match: The overridden method in the subclass must have the same method signature (name, return type, and parameters) as the method in the superclass.

Polymorphism: Method overriding is a form of polymorphism, where the same method name is used in different classes, and the appropriate method is called based on the type of the object.

super() Function: In some cases, you might want to call the overridden method in the superclass from the subclass. You can use the super() function for this purpose.
-------------------------------------------------------------------------------------------------------------------------------
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    
    def make_sound(self):
        super().make_sound()  # Call the overridden method in the superclass
        print("Woof!")
Method overriding is a powerful mechanism for building flexible and extensible code in object-oriented programming. It allows you to create a common interface in a superclass while enabling subclasses to provide their own specialized behavior.
--------------------------------------------------------------------------------------------------------------------------------


# In[20]:


# Method Override sample 1

class BaseClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo(self):
        print('Hello from BaseClass')


class FooClass(BaseClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def foo(self):
        super().foo()
        print('Hello from FooClass')

# Example usage:
obj = FooClass(a=10, b=20, c=30)
obj.foo()


# In[3]:


#Abstract

#abstract methods are methods declared in an abstract class but do not provide an implementation. Abstract classes are classes that cannot be instantiated and are meant to be subclassed. Abstract methods serve as a way to define a common interface that must be implemented by any concrete (non-abstract) subclass.

#Here's an example using the abc module in Python to create an abstract class with an abstract method:

from abc import ABC, abstractmethod

class Shape(ABC):  # Inheriting from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Uncommenting the following line will result in an error, as you cannot instantiate an abstract class.
# shape = Shape()

# Create instances of concrete subclasses
square = Square(5)
circle = Circle(3)

# Call the area method on instances of concrete subclasses
print("Square Area:", square.area())  # Output: 25
print("Circle Area:", circle.area())  # Output: 28.26
#In this example:

#Shape is an abstract class that inherits from ABC (Abstract Base Class). The area method in the Shape class is declared as an abstract method using the @abstractmethod decorator.

#Square and Circle are concrete subclasses of the abstract class Shape. They provide their own implementations of the area method.

#Attempting to create an instance of the abstract class Shape will result in an error since abstract classes cannot be instantiated.

#Instances of the concrete subclasses Square and Circle can be created, and their area methods can be called.

#The use of abstract classes and abstract methods helps enforce a common interface across related classes, providing a way to ensure that certain methods must be implemented by any concrete subclass. This contributes to code design, maintainability, and the prevention of incomplete or incorrect implementations.


# In[21]:


#Abstract sample 1

from abc import ABC, abstractmethod

class Ben10(ABC):

    @abstractmethod
    def omiTransformation(self):
        '''Abstract method for transformation'''
        pass

class FourArms(Ben10):
    def omiTransformation(self):
        '''Implementation of transformation'''
        print('FourArms Transformation Done')

# Example usage:
x = FourArms()
x.omiTransformation()


# In[7]:


# Polymorphism Example

# Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different types to be treated as objects of a common base type. This concept enables a single interface to represent different types of objects, making the code more flexible, reusable, and extensible.

# There are two main types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.

# 1. Compile-Time Polymorphism:
# Compile-time polymorphism is also known as method overloading. It occurs when there are multiple methods in the same class with the same name but different parameter lists.

# Example in Python:

class MathOperations:
    def add(self, x, y):
        return x + y

    def add_three(self, x, y, z):
        return x + y + z

# Create an instance of the class
math_obj = MathOperations()

# Call the overloaded methods
result1 = math_obj.add(2, 3)
result2 = math_obj.add_three(2, 3, 4)

print("Result 1:", result1)  # Output: 5
print("Result 2:", result2)  # Output: 9

# In this example, the add method is overloaded with two different parameter lists. Unlike some other languages, Python does not support true method overloading. Each method name must be unique within the class.

# 2. Runtime Polymorphism:
# Runtime polymorphism is achieved through method overriding, a concept closely tied to inheritance. It allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

# Example in Python:

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the overridden method
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

# In this example, both Dog and Cat classes inherit from the Animal class and provide their own implementations of the make_sound method. The type of the object determines which version of the method is called at runtime.

# Benefits


# In[8]:


#Method Overloading and Overriding

#Method Overloading:
#Method overloading refers to defining multiple methods in the same class with the same name but with different parameters. Python does not support traditional method overloading as some other languages do, where you can have multiple methods with the same name but different parameter lists. However, you can achieve a form of method overloading in Python using default values and variable-length arguments.

#Example:
class MathOperations:
    def add(self, x, y=0, z=0):
        return x + y + z

# Create an instance of the class
math_obj = MathOperations()

# Call the overloaded methods
result1 = math_obj.add(2)
result2 = math_obj.add(2, 3)
result3 = math_obj.add(2, 3, 4)

print("Result 1:", result1)  # Output: 2
print("Result 2:", result2)  # Output: 5
print("Result 3:", result3)  # Output: 9
#In this example, the add method is "overloaded" to accept different numbers of arguments. If only one argument is provided, it assumes default values for the others.

#Method Overriding:
#Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. It is a fundamental concept in inheritance and allows a subclass to provide its own version of a method while maintaining the same method signature.

#Example:
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the overridden method
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
#In this example, both Dog and Cat classes inherit from the Animal class and provide their own implementations of the make_sound method. The make_sound method is overridden in the subclasses, allowing each class to have its unique behavior.

#Key Points:
#Method overloading in Python is achieved through default values and variable-length arguments.
#Python supports method overriding through inheritance, allowing subclasses to provide their own implementations of methods defined in the superclass.
#Method overriding allows for polymorphism, where objects of different types can be treated as objects of a common base type.
#These concepts enhance the flexibility and extensibility of your code, allowing you to create more modular and adaptable software systems in Python.


# In[9]:


#Duck Typing

#Duck typing is a concept in programming languages, including Python, that focuses on the behavior of an object rather than its type. The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In the context of programming, this means that the type or class of an object is determined by its behavior rather than its explicit declaration.

#In a language that uses duck typing, the suitability of an object for a particular purpose is determined by the presence of certain methods or properties rather than by its inheritance or explicit type. If an object supports the methods or attributes required for a specific operation, it is considered compatible, regardless of its actual type.

#Here's a simple example in Python to illustrate duck typing:


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    return animal.speak()

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# All of them can be passed to the function
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(duck))  # Output: Quack!
#In this example, the animal_sound function takes an argument animal and calls its speak method. The function doesn't care about the specific type of the object passed to it; it only expects that the object has a speak method. This is an example of duck typing, as the compatibility of the object with the function is based on its behavior (having a speak method) rather than its explicit type.

#Duck typing promotes flexibility and code reusability, allowing different classes to be used interchangeably if they exhibit the required behavior, even if they are not explicitly related through inheritance or a common interface.


# In[22]:


#Duck typing sample1

class Duck:
    def quacks(self):
        print('quack!')
    def fly(self):
        print('flap-flap')

class DogDuck:
    def quacks(self):
        print('Bak!')
    def fly(self):
        print('Zooooo')

def foo(x):
    x.quacks()

# Example usage:
duck_instance = Duck()
dog_duck_instance = DogDuck()

foo(duck_instance)  # Output: quack!
foo(dog_duck_instance)  # Output: Bak!


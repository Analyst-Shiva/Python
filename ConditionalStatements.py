#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python program that asks the user for their age and prints "You are an adult" if the age is 18 or older, otherwise prints "You are a minor'.
age=int(input('enter a age:'))
if age >=18: # this condition check  age great then 18
    print('You are an adult')
else:
    print('You are a minor')


# In[4]:


#2.Write a program that takes a numerical grade (out of 100) as input and prints the corresponding letter grade according to the following scale:
90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F


marks=float(input('enter your marks:'))
if marks in range(0,101):
    if marks in range(90,100):
        print("Grade A ") 
    elif marks in range(80,89):
        print('Grade B')
    elif marks in range(70,79):
        print('Grade C')
    elif marks in range(60,69):
        print('Grade D')
    elif marks<=60:
        print('Fail')
else:
    print('please enter invalid input')


# In[6]:


#3.Write a program that calculates the Body Mass Index (BMI) of a person. The user should input their weight in kilograms and height in meters. The program should then print whether the person is underweight, normal weight, overweight, or obese

weight=float(input('enter weight:'))
height=float(input('enter height:'))
bmi=weight/(height**2)
print(f'The Weight, Height, and bmi of  body  {weight},{height}, are {bmi}')
if weight<=20.5:
    print('under weight')
elif 20.5 <= bmi < 40.9:
    print('normal weight')
elif 50<= bmi < 70.5:
    print('over weight')
else:
    print('obese')


# In[7]:


#4.Write a program that asks the user for three numbers and prints the maximum of the three.

x=float(input('enter first number:'))
y=float(input('enter second number'))
z=float(input('enter third number:'))
if x>=y and x>=z:
    print('x is maximum')
elif y>=x and y>=z:
    print('y is maximum')
else:
    print('z is maximum')


# In[8]:


#5.Write a program that asks the user for a temperature (in Celsius) and prints "It's freezing" if the temperature is below 0, "It's cool" if it's between 0 and 10, "It's warm" if it's between 10 and 20, and "It's hot" if it's above 20

temp=float(input('enter Temperature in celsius:'))
if temp<=0:
    print("it's freezing")
elif temp in range(0,10):
    print("it's cool" )
elif temp in range(10,20):
    print("it's warm")
elif temp >20:
    print("it's hot")


# In[9]:


#5.Write a program that asks the user for a number (1-7) and prints the corresponding day of the week.

day=int(input('enter a number in blw (1-7): '))
if day in range(1,7):
    if day ==1:
        print('sunday')
    elif day==2:
        print('monday')
    elif day==3:
        print('tuesday')
    elif day==4:
        print('wensday')
    elif day==5:
        print("thursday")
    elif day==6:
        print('friday')
    elif  day==7:
        print('saturday')
        
else:
    print('enter valid number')


# In[12]:


#6.Write a program that asks the user for a number and prints "In range" if the number is between 10 and 20 (inclusive), and "Out of range" otherwise.

num=int(input('enter a number:'))
if num in range(10,21): # check weather num in range(10,20) inclusive
    print('In range')
else:
    print("out of range")


# In[14]:


#7.Write a program that asks the user for an integer and prints whether it's even or odd.

n=int(input("Enter a integer number:"))
if n%2==0:
    print("It is even number")
else:
    print("it is odd number")


# In[6]:


#8.Write a Python program to add 'ing' at the end of a given string (string length should be equal to or more than 3). If the given string already ends with 'ing' then add 'ly' instead.If the string length of the given string is less than 3, leave it unchanged.

str=input('enter a  word:')
if len(str)==2:
    print("str")
elif str.endswith('ing'):
    print((str).replace('ing','ly'))
else:
    print((str)+('ing'))

    str=input('enter a  word:')
if len(str)==2:
    print("str")
elif str.endswith('ing'):
    print((str).replace('ing','ly'))
else:
    print((str)+('ing'))


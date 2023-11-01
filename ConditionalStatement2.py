#!/usr/bin/env python
# coding: utf-8

# 1) Create rock-paper-scissors by using the if condition.
# a,b = input('player-I:').lower(),input('player-II:').lower() # players playing rock-paper-scissors.
# if a == 'r': # a is equal to 'r'
#     if b == 'P': # b is equal to 'p'
#         print('b wins') # print will be b wins
#     elif b == 's': # if b equal to 's'
#         print('a wins') # it print a wins
# else: # else will be print tie
#     print('tie') 
# player-I:r
# player-II:s
# a wins
# a,b = input('player-I:').lower(),input('player-II:').lower() # players playing rock-paper-scissors.
# if a == 'r': # a is equal to 'r'
#     if b == 'P':  # b is equal to 'p'
#         print('b wins') # print will be b wins
#     elif b == 's': # if b equal to 's'
#         print('a wins') # it print a wins
# else: # else will be print tie
#     print('tie')
# player-I:p
# player-II:s
# tie
# a,b = input('player-I:').lower(),input('player-II:').lower() # players playing rock-paper-scissors.
# if a == 'r': # a is equal to 'r'
#     if b == 's': # b is equal to 'p'
#         print('b wins') # print will be b wins
#     elif b == 'p': # if b equal to 'p'
#         print('a wins') # it print a wins
# else: # else will be print tie
#     print('tie')
# player-I:r
# player-II:s
# b wins

# #2) Create a dynamic calculator which asks for numbers and operator and return the answers,
# Example
# Input: Type first number: 10",
# Type any of this (+, -, , /, %, ): ,
# Assignment-2 ,
# Type second number: 19,
# Output:Answer is 190
# first_number = float(input("first number: ")) # user input for first numbers 
# operator = input("used operators (+, -, *, /, %, **): ") # user input for operator
# second_number = float(input("second number: "))# user input for second numbers
# 
# #Perform the calculation based on the operator and print the result
# if operator == '+':  # operator is adding
#     result = first_number + second_number
# elif operator == '-': # operator is subtracting
#     result = first_number - second_number
# elif operator == '*': # operator is multiplication
#     result = first_number * second_number
# elif operator == '/': # operator is dividing
#     result = first_number / second_number
# elif operator == '%': # operator is percentage
#     result = first_number % second_number
# elif operator == '**': # operator is double multiplication
#     result = first_number ** second_number
# else:
#     result = "Invalid operator entered."
# print("Answer is", result) # Print the result
# first number: 5.8
# used operators (+, -, *, /, %, **): **
# second number: 4.1
# Answer is 1349.1330257246032
# first_number = float(input("first number: ")) # user input for first numbers 
# operator = input("used operators (+, -, *, /, %, **): ") # user input for operator
# second_number = float(input("second number: "))# user input for second numbers
# 
# #Perform the calculation based on the operator and print the result
# if operator == '+':  # operator is adding
#     result = first_number + second_number
# elif operator == '-': # operator is subtracting
#     result = first_number - second_number
# elif operator == '*': # operator is multiplication
#     result = first_number * second_number
# elif operator == '/': # operator is dividing
#     result = first_number / second_number
# elif operator == '%': # operator is percentage
#     result = first_number % second_number
# elif operator == '**': # operator is double multiplication
#     result = first_number ** second_number
# else:
#     result = "Invalid operator entered."
# print("Answer is", result) # Print the result
# first number: 99
# used operators (+, -, *, /, %, **): %
# second number: 66
# Answer is 33.0
# first_number = float(input("first number: ")) # user input for first numbers 
# operator = input("used operators (+, -, *, /, %, **): ") # user input for operator
# second_number = float(input("second number: "))# user input for second numbers
# 
# #Perform the calculation based on the operator and print the result
# if operator == '+':  # operator is adding
#     result = first_number + second_number
# elif operator == '-': # operator is subtracting
#     result = first_number - second_number
# elif operator == '*': # operator is multiplication
#     result = first_number * second_number
# elif operator == '/': # operator is dividing
#     result = first_number / second_number
# elif operator == '%': # operator is percentage
#     result = first_number % second_number
# elif operator == '**': # operator is double multiplication
#     result = first_number ** second_number
# else:
#     result = "Invalid operator entered."
# print("Answer is", result) # Print the result
# first number: 88.8
# used operators (+, -, *, /, %, **): -*
# second number: 52
# Answer is Invalid operator entered.

# 3) Manoj Kumar has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Manoj Kumar.Person Relation,Shiva father ,Letha mother, Tarun brother,Kavitha sister ,,Strange Coder.
# person_name = input("Enter the person's name: ") # user input for the person's name
# 
# if person_name == "Shiva": # knowing the relationship based on the person's name to manoj
#     relation = "father" # shiva is father of manoj
# elif person_name == "Letha": # letha is mother of manoj
#     relation = "mother"
# elif person_name == "Tarun": # tarun is brother of manoj
#     relation = "brother"
# elif person_name == "Kavitha":# kavitha is sister of manoj
#     relation = "sister"
# elif person_name == "Strange Coder": # strange coder will be friend of manoj
#     relation = "friend"
# else: # else will be the unknown relation
#     relation = "relation unknown"
# print("The relationship of", person_name, "to Manoj Kumar is:", relation)
# Enter the person's name: kranthi
# The relationship of kranthi to Manoj Kumar is: relation unknown
# person_name = input("Enter the person's name: ") # user input for the person's name
# 
# if person_name == "Shiva": # knowing the relationship based on the person's name to manoj
#     relation = "father" # shiva is father of manoj
# elif person_name == "Letha": # letha is mother of manoj
#     relation = "mother"
# elif person_name == "Tarun": # tarun is brother of manoj
#     relation = "brother"
# elif person_name == "Kavitha":# kavitha is sister of manoj
#     relation = "sister"
# elif person_name == "Strange Coder": # strange coder will be friend of manoj
#     relation = "friend"
# else: # else will be the unknown relation
#     relation = "relation unknown"
# print("The relationship of", person_name, "to Manoj Kumar is:", relation)
# Enter the person's name: Letha
# The relationship of Letha to Manoj Kumar is: mother

# 4) Write a python program that takes in a word and determines whether or not it is plural. A plural word is one that ends with “s”
# word = input("Enter a word: ") # user input for the word
# 
# plural = word.endswith('s') # by using .endswith to find word ends with's'
# 
# if plural: # knowing the appropriate message based on the plural status
#     message = "The word '{}' is plural.".format(word) # by using .format for word
# else: # else will find not plural
#     message = "The word '{}' is not plural.".format(word)
# 
# print(message) # Print the result of word
# Enter a word: kranthi
# The word 'kranthi' is not plural.
# word = input("Enter a word: ") # user input for the word
# 
# plural = word.endswith('s') # by using .endswith to find word ends with's'
# 
# if plural: # knowing the appropriate message based on the plural status
#     message = "The word '{}' is plural.".format(word) # by using .format for word
# else: # else will find not plural
#     message = "The word '{}' is not plural.".format(word)
# 
# print(message) # Print the result of word
# Enter a word: happiness
# The word 'happiness' is plural.

# 5) A company decided to give a bonus of 5% to employees if his/her year of service is more than 5 years.Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter your salary: ")) # user input for salary 
# years_of_service = int(input("Enter your years of service: ")) # user input for years of service
# 
# bonus_percentage = 5  # 5% bonus for employees with more than 5 years of service
# 
# if years_of_service > 5: # Check if years of service is more than 5 to calculate the bonus
#     bonus_amount = (bonus_percentage / 100) * salary
#     print("Congratulations! You qualify for a", bonus_percentage, "% bonus.") # print who qualify for bonus percentage
#     print("Net bonus amount:", bonus_amount) # print bonus amount 
# else: # else you are not qualify for bonus
#     print("Sorry, you do not qualify for the bonus.")
# Enter your salary: 45000
# Enter your years of service: 9
# Congratulations! You qualify for a 5 % bonus.
# Net bonus amount: 2250.0
# salary = float(input("Enter your salary: ")) # user input for salary 
# years_of_service = int(input("Enter your years of service: ")) # user input for years of service
# 
# bonus_percentage = 5  # 5% bonus for employees with more than 5 years of service
# 
# if years_of_service > 5: # Check if years of service is more than 5 to calculate the bonus
#     bonus_amount = (bonus_percentage / 100) * salary
#     print("Congratulations! You qualify for a", bonus_percentage, "% bonus.") # print who qualify for bonus percentage
#     print("Net bonus amount:", bonus_amount) # print bonus amount 
# else: # else you are not qualify for bonus
#     print("Sorry, you do not qualify for the bonus.")
# Enter your salary: 60000
# Enter your years of service: 4
# Sorry, you do not qualify for the bonus.

# 6) Take values of length and breadth of a rectangle from the user and check if it is square or not.
# length = float(input("Enter the length of the rectangle: ")) # user input for length of the rectangle
# breadth = float(input("Enter the breadth of the rectangle: ")) # user input for breadth of the rectangle
# 
# if length == breadth: # Check if it's a square or rectangle
#     print("It's a square.") # print its a square are not
# else: # print it is rectangle when it is not square 
#     print("It's a rectangle.")
# Enter the length of the rectangle: 32
# Enter the breadth of the rectangle: 14
# It's a rectangle.
# length = float(input("Enter the length of the rectangle: ")) # user input for length of the rectangle
# breadth = float(input("Enter the breadth of the rectangle: ")) # user input for breadth of the rectangle
# 
# if length == breadth: # Check if it's a square or rectangle
#     print("It's a square.") # print its a square are not
# else: # print it is rectangle when it is not square 
#     print("It's a rectangle.")
# Enter the length of the rectangle: 16
# Enter the breadth of the rectangle: 16
# It's a square.

# #7) Accept any city from the user and display the momentum of the city
# Hyderabad : “charminar”
# “Delhi” : “red fort
# “Agra : Taj mahal
# If the city name is not given correctly, give him a warning message.
# monuments = {                       # Dictionary containing city-monument 
#     "Hyderabad": "Charminar",
#     "Delhi": "Red Fort",
#     "Agra": "Taj Mahal"
# }
# city = input("Enter the name of the city: ") #  input for the city entered by user
# 
# if city in monuments: # Check if the city is in the dictionary, and display the corresponding monument of user entered
#     monument = monuments[city] # it shows the monument equal to monumentscity
#     print("The monument of", city, "is:", monument) # print the monumentcity
# else: # else will print warning if entered city not in dictionary used given city
#     print("Warning: Monument information not available for the given city.")
# Enter the name of the city: Hyderabad
# The monument of Hyderabad is: Charminar
# monuments = {                       # Dictionary containing city-monument 
#     "Hyderabad": "Charminar",
#     "Delhi": "Red Fort",
#     "Agra": "Taj Mahal"
# }
# city = input("Enter the name of the city: ") #  input for the city entered by user
# 
# if city in monuments: # Check if the city is in the dictionary, and display the corresponding monument of user entered
#     monument = monuments[city] # it shows the monument equal to monumentscity
#     print("The monument of", city, "is:", monument) # print the monumentcity
# else: # else will print warning if entered city not in dictionary used given city
#     print("Warning: Monument information not available for the given city.")
# Enter the name of the city: mumbai
# Warning: Monument information not available for the given city.

# 8) Write a program to check whether a person is eligible for voting or not (voting age>=18)
# age = int(input("Enter your age: ")) # user input for  age
# 
# if age >= 18: # Check if the person is eligible for voting # for voting age should be >= 18 
#     print("You are eligible for voting.")  # print the eligible candidates
# else: # else will give not eligible 
#     print("You are not eligible for voting yet.")
# Enter your age: 22
# You are eligible for voting.
# age = int(input("Enter your age: ")) # user input for  age
# 
# if age >= 18: # Check if the person is eligible for voting # for voting age should be >= 18 
#     print("You are eligible for voting.")  # print the eligible candidates
# else: # else will give not eligible 
#     print("You are not eligible for voting yet.")
# Enter your age: 16
# You are not eligible for voting yet.

# 9) Accept three sides of the triangle and check whether the triangle is possible or not.(Triangle is possible only when the sum of any two sides is greater than 3rd side)
# side1 = float(input("Enter the length of the first side: ")) # user input for first side of the triangle
# side2 = float(input("Enter the length of the second side: ")) # user input for second side of the triangle
# side3 = float(input("Enter the length of the third side: ")) # user input for third side of the triangle
# 
# #Checking the triangle is possible based on the given condition
# if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
#     print("Triangle is possible with the given sides.") # print the possible triangle
# else: # else will give not possible triangle
#     print("Triangle is not possible with the given sides.")
# Enter the length of the first side: 15
# Enter the length of the second side: 8
# Enter the length of the third side: 12
# Triangle is possible with the given sides.
# side1 = float(input("Enter the length of the first side: ")) # user input for first side of the triangle
# side2 = float(input("Enter the length of the second side: ")) # user input for second side of the triangle
# side3 = float(input("Enter the length of the third side: ")) # user input for third side of the triangle
# 
# #Checking the triangle is possible based on the given condition
# if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
#     print("Triangle is possible with the given sides.") # print the possible triangle
# else: # else will give not possible triangle
#     print("Triangle is not possible with the given sides.")
# Enter the length of the first side: 14
# Enter the length of the second side: 14

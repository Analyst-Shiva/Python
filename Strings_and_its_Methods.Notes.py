#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Strings definition,Information.

Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

ExampleGet your own Python Server
print("Hello")
print('Hello')
--------------------------------------------------------------------------------------------------------------------------------
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Example
a = "Hello"
print(a)
--------------------------------------------------------------------------------------------------------------------------------
Multiline Strings
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
--------------------------------------------------------------------------------------------------------------------------------
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
--------------------------------------------------------------------------------------------------------------------------------
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

Example
Loop through the letters in the word "banana":

for x in "banana":
print(x)
--------------------------------------------------------------------------------------------------------------------------------
String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
--------------------------------------------------------------------------------------------------------------------------------
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.

Example
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
--------------------------------------------------------------------------------------------------------------------------------
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
--------------------------------------------------------------------------------------------------------------------------------
Slicing Strings
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

ExampleGet your own Python Server
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
--------------------------------------------------------------------------------------------------------------------------------
Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])
--------------------------------------------------------------------------------------------------------------------------------
String Concatenation
To concatenate, or combine, two strings you can use the + operator.

ExampleGet your own Python Server
Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)


# In[2]:


#string methods

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning


# In[14]:


# Addition  

Definition and Usage
The add() method adds an element to the set.

If the element already exists, the add() method does not add the element.

Syntax
set.add(elmnt)

Parameter Values

Parameter	Description
elmnt	Required. The element to add to the set

a = 'old'
c = a + b
print(c)


# In[3]:


#Capitalization 

Definition and Usage
The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

Syntax
string.capitalize()

Parameter Values
No parameters

txt = "hello, and welcome to my world."  
x = txt.capitalize()

print (x)


# In[2]:


#casefold
    
Definition and Usage
The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

Syntax
string.casefold()

Parameter Values
No parameters

txt = "Hello, And Welcome To My World!" 
                                         
x = txt.casefold()

print(x)


# In[17]:


# center

Definition and Usage
The center() method will center align the string, using a specified character (space is default) as the fill character.

Syntax
string.center(length, character)

Parameter Values
Parameter	Description

length	Required. The length of the returned string

character	Optional. The character to fill the missing space on each side. Default is " " (space)

txt = "banana" 

x = txt.center(20)

print(x)


# In[18]:


#count

Definition and Usage
The count() method returns the number of elements with the specified value.

Syntax
list.count(value)

Parameter Values
Parameter	Description

value	Required. Any type (string, number, list, tuple, etc.). The value to search for.
fruits = ['apple', 'banana', 'cherry'] 

x = fruits.count("cherry")

print(x)


# In[19]:


#encode

Definition and Usage
The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

Syntax
string.encode(encoding=encoding, errors=errors)

Parameter Values

Parameter	Description
encoding	Optional. A String specifying the encoding to use. Default is UTF-8
errors	Optional. A String specifying the error method. Legal values are:
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character

txt = "My name is Vijay" 

x = txt.encode()

print(x)


# In[20]:


#endswith

Definition and Usage
The endswith() method returns True if the string ends with the specified value, otherwise False.

Syntax
string.endswith(value, start, end)

Parameter Values

Parameter	Description
value	Required. The value to check if the string ends with
start	Optional. An Integer specifying at which position to start the search
end	Optional. An Integer specifying at which position to end the search

txt = "Hello, welcome to my world."
x = txt.endswith(".")

print(x)


# In[21]:


#expandtabs

Definition and Usage
The expandtabs() method sets the tab size to the specified number of whitespaces.

Syntax
string.expandtabs(tabsize)

Parameter Values

Parameter	Description
tabsize	Optional. A number specifying the tabsize. Default tabsize is 8
txt = "H\te\tl\tl\to" 

x =  txt.expandtabs(2)

print(x)


# In[22]:


#find
   
Definition and Usage
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

Syntax
string.find(value, start, end)

Parameter Values

Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


# In[23]:


#format
   
Definition and Usage
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

Syntax
string.format(value1, value2...)

Parameter Values

Parameter	Description
value1, value2...	Required. One or more values that should be formatted and inserted in the string.

The values are either a list of values separated by commas, a key=value list, or a combination of both.

The values can be of any data type.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[24]:


#formatmap

Definition and Usage
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

Syntax
map(function, iterables)

Parameter Values

Parameter	Description
function	Required. The function to execute for each item
iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

point = {'x':4,'y':-5}  #formatmap
print('{x} {y}'.format(**point))


# In[25]:


#Index

Definition and Usage
The index() method returns the position at the first occurrence of the specified value.

Syntax
list.index(elmnt)

Parameter Values

Parameter	Description
elmnt	Required. Any type (string, number, list, etc.). The element to search for

txt = "Hello, welcome to my world." #Index

x = txt.index("welcome")

print(x)


# In[26]:


#isalnum

Definition and Usage
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

Example of characters that are not alphanumeric: (space)!#%&? etc.

Syntax
string.isalnum()

Parameter Values
No parameters.

txt = "Company12" #isalnum

x = txt.isalnum()

print(x)


# In[27]:


#isalpha

Definition and Usage
The isalpha() method returns True if all the characters are alphabet letters (a-z).

Example of characters that are not alphabet letters: (space)!#%&? etc.

Syntax
string.isalpha()

Parameter Values
No parameters.
txt = "CompanyX" #isalpha

x = txt.isalpha()

print(x)


# In[28]:


#isascii

Definition and Usage
The isascii() method returns True if all the characters are ascii characters  (a-z).

Check our ASCII Reference.

Syntax
string.isascii()

Parameter Values
No parameters.

txt = "Company123" 

x = txt.isascii()

print(x)


# In[29]:


#isdecimal

Definition and Usage
The isdecimal() method returns True if all the characters are decimals (0-9).

This method can also be used on unicode objects. See example below.

Syntax
string.isdecimal()

Parameter Values
No parameters.

txt = "1234"  #isdecimal

x = txt.isdecimal()

print(x)


# In[30]:


#isdigit
    
Definition and Usage
The isdigit() method returns True if all the characters are digits, otherwise False.

Exponents, like ², are also considered to be a digit.

Syntax
string.isdigit()

Parameter Values
No parameters.    

txt = "50800" #isdigit

x = txt.isdigit()

print(x)


# In[31]:


#isidentifier

Definition and Usage
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

Syntax
string.isidentifier()

Parameter Values
No parameters.

txt = "Demo" 

x = txt.isidentifier()

print(x)


# In[32]:


#islower
   
Definition and Usage
The islower() method returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

Syntax
string.islower()

Parameter Values
No parameters.

txt = "hello world!"

x = txt.islower()

print(x)


# In[33]:


#isnumeric

Definition and Usage
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

Syntax
string.isnumeric()

Parameter Values
No parameters.

txt = "565543" 

x = txt.isnumeric()

print(x)


# In[34]:


#isprintable
    
Definition and Usage
The isprintable() method returns True if all the characters are printable, otherwise False.

Example of none printable character can be carriage return and line feed.

Syntax
string.isprintable()

Parameter Values
No parameters.

txt = "Hello! Are you #1?" #isprintable

x = txt.isprintable()

print(x)


# In[1]:


#isspace

Definition and Usage
The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

Syntax
string.isspace()

Parameter Values
No parameters.

txt = "   " #isspace

x = txt.isspace()

print(x)


# In[2]:


#istitle
    
Definition and Usage
The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

Symbols and numbers are ignored.

Syntax
string.istitle()

Parameter Values
No parameters.

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


# In[3]:


#isupper

Definition and Usage
The isupper() method returns True if all the characters are in upper case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

Syntax
string.isupper()

Parameter Values
No parameters.

txt = "THIS IS NOW!" 

x = txt.isupper()

print(x)


# In[4]:


#join

Definition and Usage
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.

Syntax
string.join(iterable)

Parameter Values

Parameter	Description
iterable	Required. Any iterable object where all the returned values are strings

myTuple = ("John", "Peter", "Vicky") 

x = "#".join(myTuple)

print(x)


# In[7]:


#isljust

Definition and Usage
The ljust() method will left align the string, using a specified character (space is default) as the fill character.

Syntax
string.ljust(length, character)

Parameter Values

Parameter	Description
length	Required. The length of the returned string
character	Optional. A character to fill the missing space (to the right of the string). Default is " " (space).

txt = "Apple" 

x = txt.ljust(20)

print(x, "is my favorite fruit.")


# In[6]:


#lower

Definition and Usage
The lower() method returns a string where all characters are lower case.

Symbols and Numbers are ignored.

Syntax
string.lower()

Parameter Values
No parameters   
   
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)


# In[8]:


#lstrip

Definition and Usage
The lstrip() method removes any leading characters (space is the default leading character to remove)

Syntax
string.lstrip(characters)

Parameter Values

Parameter	Description
characters	Optional. A set of characters to remove as leading characters

txt = "     Apple     " 

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


# In[9]:


#maketrans
   
Definition and Usage
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

Syntax
str.maketrans(x, y, z)

Parameter Values

Parameter	Description
x	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z	Optional. A string describing which characters to remove from the original string.
   
txt = "Hello Vijay!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))


# In[11]:


#partition

Definition and Usage
The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

Note: This method searches for the first occurrence of the specified string.

Syntax
string.partition(value)

Parameter Values

Parameter	Description
value	Required. The string to search for

txt = "I could eat Apples all day" 

x = txt.partition("Apples")

print(x)


# In[12]:


#removeprefix

Definition and Usage
The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

Note: This method searches for the first occurrence of the specified string.

Syntax
string.removeprefix(value)

Parameter Values

Parameter	Description
value	Required. The string to search for

invoice_filenames = ("INV_123.pdf", "INV_234.pdf", "INV_345.pdf") 

for invoice_filename in invoice_filenames:
    print(invoice_filename.removeprefix("INV_"))


# In[13]:


#removesuffix

Definition and Usage
The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

Note: This method searches for the first occurrence of the specified string.

Syntax
string.removeprefix(value)

Parameter Values

Parameter	Description
value	Required. The string to search for
var = 'Explicit is better than implicit.' 
var1 = var.removesuffix('.')

print ("original string:", var)
print ("suffix removed:", var1)


# In[15]:


#replace

Definition and Usage
The replace() method replaces a specified phrase with another specified phrase.

Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

Syntax
string.replace(oldvalue, newvalue, count)

Parameter Values

Parameter	Description
oldvalue	Required. The string to search for
newvalue	Required. The string to replace the old value with
count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

txt = "I like apples" 

x = txt.replace("oranges", "apples")

print(x)


# In[16]:


#rfind

Definition and Usage
The rfind() method finds the last occurrence of the specified value.

The rfind() method returns -1 if the value is not found.

The rfind() method is almost the same as the rindex() method. See example below.

Syntax
string.rfind(value, start, end)

Parameter Values

Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string
txt = "My word, your word." 

x = txt.rfind("word")

print(x)


# In[17]:


#rindex
   
Definition and Usage
The rindex() method finds the last occurrence of the specified value.

The rindex() method raises an exception if the value is not found.

The rindex() method is almost the same as the rfind() method. See example below.

Syntax
string.rindex(value, start, end)

Parameter Values

Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string
   
txt = "My word, your word."

x = txt.rindex("word")

print(x)


# In[18]:


#rjust

Definition and Usage
The rjust() method will right align the string, using a specified character (space is default) as the fill character.

Syntax
string.rjust(length, character)

Parameter Values

Parameter	Description
length	Required. The length of the returned string
character	Optional. A character to fill the missing space (to the left of the string). Default is " " (space).

txt = "Apple" 

x = txt.rjust(20)

print(x, "is my favorite fruit.")


# In[19]:


#rpartition

Definition and Usage
The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

Syntax
string.rpartition(value)

Parameter Values

Parameter	Description
value	Required. The string to search for

txt = "I could eat appes all day, apples are my favorite fruit" 

x = txt.rpartition("apples")

print(x)


# In[20]:


#rsplit

Definition and Usage
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.rsplit(separator, maxsplit)

Parameter Values

Parameter	Description
separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "apple, orange, cherry" 

x = txt.rsplit(", ")

print(x)


# In[21]:


#rstrip
    

Definition and Usage
The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

Syntax
string.rstrip(characters)

Parameter Values

Parameter	Description
characters	Optional. A set of characters to remove as trailing characters
txt = "     orange     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


# In[23]:


#rsplit

Definition and Usage
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.rsplit(separator, maxsplit)

Parameter Values

Parameter	Description
separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "apple, orange, cherry" 

x = txt.rsplit(", ")

print(x)


# In[24]:


#split

Definition and Usage
The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.split(separator, maxsplit)

Parameter Values

Parameter	Description
separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "welcome to the jungle" 

x = txt.split()

print(x)


# In[25]:


#splitlines

Definition and Usage
The splitlines() method splits a string into a list. The splitting is done at line breaks.

Syntax
string.splitlines(keeplinebreaks)

Parameter Values

Parameter	Description
keeplinebreaks	Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False
txt = "Thank you for the music\nWelcome to the jungle" 

x = txt.splitlines()

print(x)


# In[26]:


#startswith


Definition and Usage
The startswith() method returns True if the string starts with the specified value, otherwise False.

Syntax
string.startswith(value, start, end)

Parameter Values

Parameter	Description
value	Required. The value to check if the string starts with
start	Optional. An Integer specifying at which position to start the search
end	Optional. An Integer specifying at which position to end the search
txt = "Hello, welcome to my world." 

x = txt.startswith("Hello")

print(x)


# In[27]:


#strip

Definition and Usage
The strip() method removes any leading, and trailing whitespaces.

Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.

Syntax
string.strip(characters)

Parameter Values

Parameter	Description
characters	Optional. A set of characters to remove as leading/trailing characters
txt = "     Apple     " 

x = txt.strip()

print("of all fruits", x, "is my favorite")


# In[28]:


#swapcase

Definition and Usage
The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

Syntax
string.swapcase()

Parameter Values
No parameters.
x = 5  
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


# In[29]:


#title
   
Definition and Usage
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

If the word contains a number or a symbol, the first letter after that will be converted to upper case.

Syntax
string.title()

Parameter Values
No parameters.
  
txt = "Welcome to my world Vijay"

x = txt.title()

print(x)


# In[31]:


#upper

Definition and Usage
The upper() method returns a string where all characters are in upper case.

Symbols and Numbers are ignored.

Syntax
string.upper()

Parameter Values
No parameters
txt = "Hello my friends" 

x = txt.upper()

print(x)


# In[32]:


#zfill

Definition and Usage
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.

Syntax
string.zfill(len)

Parameter Values

Parameter	Description
len	Required. A number specifying the desired length of the string
txt = "50" 

x = txt.zfill(10)

print(x)


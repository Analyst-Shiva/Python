#!/usr/bin/env python
# coding: utf-8

# ###1.## what will be the output of the following  python program

# In[1]:


def foo(x):
    x[0]=['def']
    x[1]=['abc']
    return id(x)
q=['abc','def']
print(id(q)==foo(q))


# The function foo changes the contents of the input list q. id(q) gives the identity of the original list. When you call foo(q), it gives the identity of the modified list inside the function. The print statement checks if these two identities are the same. Since the modified list is still called 'q', the output is True.

# ###2.## what will be the output of the following  python code?

# In[2]:


def fun():
    try:
        return 1
    finally:
        return 2
k= fun()
print(k)  


# #The fun function has a try block returning 1. It also has a finally block that always executes and returns 2.

# ###3.## what will be the output  of the following code snippet?

# In[3]:


def func():
    global value
    value = 'Local'
value = 'Global'
func()
print(value)


# #The func function, when called, changes the global variable value to 'Local' from its initial value of 'Global'. The last print statement outputs the current value.

# ### 4.  ___________ exceptions are raised as result of an error in opening a particular file

# #The FileNotFoundError is raised when the specified file cannot be found at the given path.

# #IOError was a commonly used exception in older Python versions, but it has been deprecated in Python 3.3 and later. In Python 3, specific exceptions related to I/O operations have been introduced, and IOError has been replaced by these more specific exceptions.

# ### 5. In python we do not specify types ,it is directly interpert by the complier, so consider the following operation to be performed

# a) x =13/2 
# 
# b) x=int(13/2)
# 
# c) x= 13%2
# 
# D) All Of  the mentioned

# - a) x = 13/2: This performs floating-point division and assigns the result to x.
# 
# - b) x = int(13/2): This performs floating-point division, then converts the result to an integer using the int() function before assigning to x.
# 
# - c) x = 13%2: This performs the modulo operation, calculating the remainder of the division of 13 by 2 and assigns

# In[4]:


13//2


# In[5]:


int(13//2)


# In[6]:


13%2


# ### D) All Of the mentioned is the right one.

# ### 6.what willl be the out put of the follwing Python code?

# In[7]:


#t[5]


# #The code provided is incomplete and lacks essential context, including the declaration and initialization of the variable t. Without this information, it is impossible to determine the output or identify any issues in the code.

# a)IndexError
# 
# b)NameError
# 
# c)TypeError
# 
# d)SyntactialError

# ### 7. A while loop in python is used for what type of iteration

# a) indefinite
# 
# b) discriminant
# 
# c) definite
# 
# d) indeterminate

# #In Python, a while loop is employed for indefinite iteration. The loop persists in execution as long as a specified condition remains True.

# ### 8. What will be the output of the following python code?

# In[8]:


x = "abcdef"
while i in x:
    print(i, end=" ")


# #The code snippet will trigger a NameError due to the absence of a declaration or initialization for the variable i before its usage in the loop condition. The code attempts to iterate over the variable i within the string x without prior definition, leading to the mentioned error.

# ### 9. what is main advantage of using decorators in python?

# a) they make code more complex
# 
# b) they simplify the syntax of the decorated function
# 
# c) they reduce the performance of the code
# 
# d) they provide additional security features
# 
# 

# #Python decorators offer a powerful way to enhance functions or methods, providing benefits like code reusability, improved readability, separation of concerns, code extension without modification, adhering to the DRY principle, supporting Aspect-Oriented Programming (AOP), and simplifying the decorated function's syntax.

# ### 10. if return statement is not used inside the function , the function will return
# 
# 
# a)None
# 
# b)0
# 
# c)Null
# 
# d)Arbitary value

# #In Python, when a function does not contain a return statement, it implicitly returns None upon reaching the end of its code block. The value None signifies the absence of a value or a null value in Python.

# ### None

# ### 11.what is called when function is defined inside a class?
# 
# a) class
# 
# b) Function
# 
# c)method
# 
# d)Module

# #In Python, a function defined within a class is called a "method." Methods are functions associated with an object, allowing them to access the object's data (attributes). The syntax for defining a method is akin to defining a function but within the class definition.

# ### 12. which operator is used in python to import modules from a package?
# 
# a)•
# 
# b)*
# 
# c)->
# 
# d)&

# ###In Python, the dot (.) operator is employed to import modules from a package. When dealing with a package (essentially a directory with a special init.py file), you use dot notation to indicate the path when importing a module from within that package.

# ### 13.

# In[ ]:


def getMonth(m):
    if m < 1 or m>12:
        raise ValueError("Invalid")
    print(m)
getMonth(6)


# ###The getMonth function takes a month parameter (m). It checks if the month is invalid (less than 1 or greater than 12), and if so, it raises a ValueError with the message "Invalid." If the month is valid, it prints the month value. The function is then called with the argument 6.

# ### 14. In python programing language , syntax error is detected  by ________at_______

# a) interpreter / compile time
# 
# b) Runtime /interpreter
# 
# c)interpreter/Run time
# 
# d)compile time /Run time
# 
# ###Syntax errors in Python are spotted by the interpreter during compilation, which happens before executing the code. Therefore, syntax errors are detected by the interpreter at compile time.

# ### 15

# In[ ]:


class Book:
    def __init__(self,author):
        self.author = author
book1 = Book('V.M.Shah')
book2 = book1


# ###A class named Book is defined with a constructor method __init__ taking self and author parameters. It initializes the instance's author attribute. An instance, book1, is created with the author 'V.M.Shah' and assigned to book1. book2 is then assigned the same instance as book1. Both variables, book1 and book2, reference the same Book class instance. Changes made through one variable will affect the other.

# In[ ]:


id(book1)


# In[ ]:


id(book2)


# ### This code succinctly creates two variables (book1 and book2) pointing to the same Book class instance, sharing the same object in memory.

# ### Module - Data Analysis

# In[ ]:


import pandas as pd
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03','2024-01-10','2024-01-09','2024-01-08'],
    'Category': ['Beverage', 'Food', 'Beverage','Beverage','Beverage','Food'],
    'Product': ['Cappuccino', 'Croissant', 'Espresso','Latte','Latte','Muffin'],
    'Customer_id': ['C004','C002','C001','C001','C003','C002'],
    'Quantity': [1, 2, 2,3,1,1],
    'UnitPrice': [3, 2,2,3.5,3.5,2.5]}

df = pd.DataFrame(data)
df


# ### 16.How to create a new column "Revenue" which has value equal to the Quantity * UnitPrice" of the current row?

# In[ ]:


df['Revenue'] = df['Quantity'] * df['UnitPrice']


# #This code line adds a "Revenue" column to the DataFrame df. It calculates values by multiplying the "Quantity" and "UnitPrice" columns for each row. The line df['Revenue'] = df['Quantity'] * df['UnitPrice'] succinctly performs the element-wise multiplication and assigns the result to the new "Revenue" column.

# In[ ]:


df


# ### 17.What is the syntax to find Categorical wise revenue?

# In[ ]:


df.groupby('Category')['Revenue'].sum()


# #df.groupby('Category')['Revenue'].sum() succinctly groups the DataFrame by the 'Category' column and calculates the sum of the 'Revenue' column for each category group.

# ### 18.Tofind the average quantity wrt to date and product ,what is the correct syntax?

# In[ ]:


df.groupby(['Date', 'Product'])['Quantity'].mean()


# ###df.groupby(['Date', 'Product'])['Quantity'].mean() succinctly groups the DataFrame by the 'Date' and 'Product' columns and calculates the mean (average) of the 'Quantity' column for each unique combination of date and product.

# ### 19.Categorical wise revenue for Beverage and food respectively are

# In[ ]:


df['Revenue'] = df['Quantity'] * df['UnitPrice']


# ###The code accesses the "Quantity" and "UnitPrice" columns of the DataFrame using df['Quantity'] and df['UnitPrice'], respectively. Then, it performs element-wise multiplication of these columns with df['Quantity'] * df['UnitPrice'], creating a new Series. Finally, this new Series is assigned to a new column named "Revenue" in the DataFrame using df['Revenue'] = df['Quantity'] * df['UnitPrice'].

# In[ ]:


beverage_rev = df[df['Category'] == 'Beverage']['Revenue'].sum()
beverage_rev


# ###df[df['Category'] == 'Beverage']['Revenue'].sum() filters the DataFrame to include only rows where the 'Category' is 'Beverage', selects the 'Revenue' column from the filtered data, and calculates the sum of the 'Revenue' column for the filtered data.

# In[ ]:


food_rev = df[df['Category'] == 'Food']['Revenue'].sum()
food_rev


# ###df[df['Category'] == 'Food']['Revenue'].sum() filters the DataFrame to include only rows where the 'Category' is 'Food', selects the 'Revenue' column from the filtered data, and calculates the sum of the 'Revenue' column for the filtered data.

# ### 20. Using transform ,what is the syntax to create a column which has a unitprice difference wrt its category  mean?

# In[ ]:


df.groupby('Category')['UnitPrice'].transform(lambda x: x - x.mean())


# ####df.groupby('Category')['UnitPrice'].transform(lambda x: x - x.mean()) groups the DataFrame by the 'Category' column, selects the 'UnitPrice' column for further operations, and applies a transformation. The transformation subtracts the mean of the 'UnitPrice' column within each category from each value in the 'UnitPrice' column. This results in a new column showing the unit price difference for each row relative to its category mean. The provided output indicates the values of this new column for the first six rows of the DataFrame.

# ### 21. What is the correct syntax to get data wrt 'Monday'?

# In[ ]:


df['Date'] = pd.to_datetime(df['Date'])


# In[ ]:


df.groupby(df.Date.dt.day_name()).get_group('Monday')


# ###pd.to_datetime(df['Date']) converts the 'Date' column to a datetime format if it's not already.
# 
# ###df['Date'].dt.day_name() == 'Monday' extracts the day name from the 'Date' column using the dt accessor and checks if it is equal to 'Monday', resulting in a boolean mask.
# 
# ###df[df['Date'].dt.day_name() == 'Monday'] utilizes the boolean mask to filter the DataFrame, keeping only the rows where the day is 'Monday'.

# ### 22. which of the following statement is/are True?

# a) apply() can be applied on rows
# 
# b) Apply function can't be applied on rows
# 
# c)Apply applies the function on the entire series at a time
# 
# d)Apply applies the function one cell at a time

# ###The apply function in pandas applies the provided function along the axis of the DataFrame or Series. By default, it applies the function to each column. You can specify axis=1 to apply the function to each row.

# ### 23. Which of the following statement is/are True ?

# a) Map applies the functionality on the entire DataFrame
# 
# b)Applymap applies the functionality on series  be it row or a column
# 
# c) Apply and map are vectorized applications
# 
# d) None of the above

# ###a) While the statement mentions that map applies a function element-wise on a Series, it correctly acknowledges that apply can apply a function to the entire DataFrame or along a specific axis (row-wise or column-wise).
# 
# ###b) The statement is incorrect. applymap applies a function element-wise on the entire DataFrame, not just on a Series.
# 
# ###c) This statement is accurate. Both apply and map are vectorized operations, operating on entire arrays (columns or Series) at once, rather than iterating through individual elements.

# In[ ]:


data = {
    'Date': ['2024-01-10', '2024-01-11', '2024-01-10','2024-01-12','2024-01-11','2024-01-12'],
    'Region': ['North', 'South', 'East','West','North','East'],
    'Salesperson': ['Ajay', 'Balu', 'Chirag','Ajay','Balu','Chiraj'],
    'Product': ['Notebook', 'Pen', 'Notebook','Pen','Binder','Binder'],
    'Quantity': [5, 10, 7,15,20,10],
    'UnitPrice': [12, 3, 12,3,5,5]
}

df1= pd.DataFrame(data)

df1


# ### 24. what is the syntax to create a pivot table with index as North  and south and columns as product where values are sun of Quantities sold?

# In[ ]:


df1[df1['Region'].isin(['North', 'South'])].pivot_table(index='Product', columns='Region', values='Quantity', aggfunc='sum')


# ###values='Quantity': Specifies the column for aggregation, with values summed in this case.
# 
# ###index='Region': Sets the 'Region' column as the pivot table index.
# 
# ###columns='Product': Establishes the 'Product' column as the pivot table columns.
# 
# ###aggfunc='sum': Specifies the aggregation function, which is 'sum' in this instance.

# ### 25.Which of the following  statement is /are True?
# a) .iloc method includes include the last element when used for slicing
# 
# b).loc mrthod doesnot includes the last element when used fo slicing
# 
# c)We can use .loc method and pass default integer index of row when slicing 
# 
# d)None of above

# ###a) .iloc is integer-location based indexing and includes the last element in the specified range when used for slicing.
# 
# ###b) .loc is label-based indexing and includes the start but excludes the end when used for slicing.
# 
# ###c) Not entirely accurate: When using .loc for slicing, you typically provide labels, not default integer index values. If integer values are passed, they will be interpreted as labels, not default integer positions.

# ### 26. using a pivot table is it possible to create a multi index dataframe ,if so what is  the syntax to have a multi index of data and Region  with total Product sold as value

# In[ ]:


df.pivot_table(index=['Date', 'Region'],columns='Product',values='Quantity',aggfunc='sum')


# ###index=['Date', 'Region']: Specifies that the 'Date' and 'Region' columns will form the multi-index for the rows of the pivot table, indexing based on unique combinations of 'Date' and 'Region'.
# 
# ###columns='Product': Sets the 'Product' column as the columns of the pivot table, where each unique value in 'Product' becomes a column.
# 
# ###values='Quantity': Specifies that values in the pivot table will be taken from the 'Quantity' column of the original DataFrame.
# 
# ###aggfunc='sum': Specifies the aggregation function to be applied; in this case, it's 'sum', meaning values for each 'Date', 'Region', and 'Product' combination will be summed.

# ### 27. what does the margins parameter in the pivot_table() function allowyou to include in the pivot table?

# a) Additional margins and subtotals for rows and columns
# 
# b) A list of column name to exclude from to pivot table
# 
# c) The number of rows and columns to skip at the beginning of the pivot table
# 
# d)The maximum number of rows and columns to display in the pivot table

# ###The pivot_table() function in pandas has a margins parameter that, when set to True, includes additional margins and subtotals for rows and columns in the pivot table. Adding margins provides totals for both rows and columns, offering a comprehensive overview of the data and insights into various combinations.

# In[ ]:


import numpy as np


# In[ ]:


data = {
    'Fruits': ['apple', 'banana', 'apple', 'apple', 'banana', 'apple', 'kiwi',
               'kiwi', 'banana', 'apple', 'kiwi', 'apple', 'banana', 'grape',
               'apple', 'banana', 'apple', 'apple', 'apple'],
    'Price': [np.nan, np.nan, 205, 200, 40, 210, 300, 320, np.nan, 180, 350,np.nan, 35, np.nan, 215, 40, np.nan, np.nan, np.nan]
}

df2 = pd.DataFrame(data)


# In[ ]:


df2


# ### 28 . if we choose to impute missing value in  Price  col by chaining ffill() and bfill() while limiting the imputation to 1,1 respectively ,how many missing values will be left post imputation

# In[ ]:


df2['Price'] = df2['Price'].ffill(limit=1).bfill(limit=1)


# ###The code addresses missing values in the 'Price' column of DataFrame df2.
# 
# ###ffill(limit=1): Forward fills missing values with a limit of 1, meaning only the first missing value in a sequence is imputed.
# 
# ###bfill(limit=1): Backward fills any remaining missing values with a limit of 1, restricting imputation to only the first missing value in a sequence.

# In[ ]:


x = df2['Price'].isnull().sum()
x


# ###df2['Price'].isnull().sum() checks for missing values in the 'Price' column of DataFrame df2. It returns the total count of missing values in a simplified manner.

# ### 29.What kind of missing values handling technique is appropriate for df2?

# a) Imputing Price col with Price's mean
# 
# b) Imputing Price col with Price's median
# 
# c)Imputing Price col with  individual friuts'Price median
# 
# d)Dropping missing values

# ###Imputing the 'Price' column with the median of individual fruits' prices provides a robust estimation of central tendency, less affected by outliers or skewed distributions.

# ### 30. If we choose to impute missing values in Price col by with individual Fruits'Price's mean ,how many missing values will be post imputation

# In[ ]:


df2['Price'] = df2.groupby('Fruits')['Price'].transform(lambda x: x.fillna(x.mean()))


# ###df2['Price'] = df2.groupby('Fruits')['Price'].transform(lambda x: x.fillna(x.mean())) groups DataFrame df2 by the 'Fruits' column and selects the 'Price' column. For each group, it fills missing values in the 'Price' column with the mean of non-missing values within that group. The result is assigned back to the 'Price' column, effectively imputing missing values with the mean of each fruit's prices.

# In[ ]:


df2['Price'].isnull().sum()


# ###df2['Price'].isnull().sum() creates a boolean mask indicating missing values in the 'Price' column, and then calculates the sum of True values, providing a count of missing values in a concise manner.

# ### 31.if  a=pd.Series([np.nan,1,2,np.nan,np.nan,np.nan,np.nan,4,5,7]) what  will be  the output of a.interpolate

# In[ ]:


a=pd.Series([np.nan,1,2,np.nan,np.nan,np.nan,np.nan,4,5,7])


# In[ ]:


a.interpolate()


# ###a.interpolate() applies linear interpolation to fill NaN values in the Series 'a', producing a new Series where missing values are replaced based on linear interpolation between neighboring non-NaN values. The missing value at index 0 is not filled due to the absence of preceding values for interpolation.

# ### 32.what is the use of the normalization parameter in the crosstab method of pandas?

# a) it used to normalize values by dividing them by the total count
# 
# b)to add margins
# 
# c) there is no parameter called as normalize in crosstab
# 
# d)both a & c

# ###In pd.crosstab method in pandas, setting normalize=True normalizes the values by dividing them by the total count, displaying proportions or percentages instead of counts. This is helpful when examining the relative frequencies of the cross-tabulated variables.

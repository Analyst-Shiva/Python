#!/usr/bin/env python
# coding: utf-8

# 1. What is the total bill value
# total = np.sum(n[:,1]) 
# total
# 4827.77
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 2. what is the total tip value ?
# total = np.sum(n[:,2]) 
# total
# 731.5799999999999
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 3. count how many sun,sat,thur,fri are there ?
# column= n[:, 5]
# unique_values, counts = np.unique(column, return_counts=True)
# zip(unique_values, counts)
# print('Sunday   : ',counts[0])
# print('Saturday : ',counts[1])
# print('Friday   : ',counts[2])
# print('Thursday : ',counts[3])
# Sunday   :  87
# Saturday :  76
# Friday   :  62
# Thursday :  19
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 4. how many smokers are there
# smokers = np.sum(n[:,4])
# smokers
# 93.0
# 
# ------------------------------------------------------------------------------------------------------------------------------
# 5. what is the average tip given by female and male
# male = np.count_nonzero(n[:,3] == 0)
# female = np.count_nonzero(n[:,3] == 1)
# print("number of male :",male)
# print("number of female :",female)
# number of male : 87
# number of female : 157
# tip = n[:,2]
# sex = n[:,3] 
# tip_male = np.mean(tip[sex == 0])
# print("male average tip : ",tip_male)
# tip_female = np.mean(tip[sex == 1])
# print("female average tip : ",tip_female)
# male average tip :  2.8334482758620685
# female average tip :  3.0896178343949043
# 
# ------------------------------------------------------------------------------------------------------------------------------
# 6. how much amount have been spent by female and male
# total=n[:,1]
# gender=n[:,3]
# male=np.sum(total[gender==0])
# female=np.sum(total[gender==1])
# print("male spent amount :",male)
# print("female spent amount: ",female)
# male spent amount : 1570.9499999999996
# female spent amount:  3256.8199999999997
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 7.what is the min, and max tip given
# mini_max=n[:,2]
# mi=np.min(mini_max)
# mx=np.max(mini_max)
# print("minimum tip :",mi)
# print("maximum tip :",mx)
# minimum tip : 1.0
# maximum tip : 10.0
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 8. how many male and female are going for lunch and dinner
# sex=n[:,3]
# time=n[:,6]
# male_lunch = np.sum((time == 0) & (sex==0))
# female_lunch = np.sum((time==0) & (sex==1))
# print("male lunch :",male_lunch)
# print("female lunch :",female_lunch)
# male lunch : 52
# female lunch : 124
# sex=n[:,3]
# time=n[:,6]
# 
# male_dinner = np.sum((time == 1) & (sex==0))
# female_dinner = np.sum((time==1) & (sex==1))
# 
# print("male lunch :",male_dinner)
# print("female lunch :",female_dinner)
# male lunch : 35
# female lunch : 33
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 9.find out the average size
# size = n[:,7]
# 
# avg=np.mean(size)
# 
# print("average is :",avg)
# average is : 2.569672131147541
# 
# -------------------------------------------------------------------------------------------------------------------------------
# 10. how many female smokers and male smokers are there
# sex = n[:,3]
# smoker = n[:,4]
# 
# male=np.sum(smoker[sex==0])
# female=np.sum(smoker[sex==1])
# print("male smokers :",male)
# print("female smokers: ",female)
# male smokers : 33.0
# female smokers:  60.0

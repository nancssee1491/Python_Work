# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:33:38 2023

@author: Joo Zhin Mei (Nancssee)
"""

# MODULE-4 Conditional Statements

# 1. Take a variable ‘age’ which is of positive value and check the following:
# a. If age is less than 10, print “Children”.
# b. If age is more than 60 , print ‘senior citizens’
# c. If it is in between 10 and 60, print ‘normal citizen’

age = int(input("Enter age here: "))
if 0 <= age < 10:
    print("Children")
elif 10 <= age <= 60:
    print('normal citizen')
elif age > 60:
    print('senior citizens')
else: print("Please enter positive value for age!")
    

# 2. Find the final train ticket price with the following conditions. 
# a. If male and sr.citizen, 70% of fare is applicable
# b. If female and sr.citizen, 50% of fare is applicable.
# c. If female and normal citizen, 70% of fare is applicable
# d. If male and normal citizen, 100% of fare is applicable
"""[Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60]"""

gender = str(input("male or female?: "))
age = int(input("Enter age here: "))

if gender == "male" and age >= 60:
    print("70% of fare is applicable.")
elif gender == "male" and age < 60:
    print("100% of fare is applicable.")
elif gender == "female" and age >= 60:
    print("50% of fare is applicable.")
else: print("70% of fare is applicable.")
    
    
# 3. Check whether the given number is positive and divisible by 5 or not.  

a = int(input("Enter a number to check: "))
if a > 0 and a%5 == 0:
    print("Given number is positive AND divisible by 5.")
else: print("Given number is not positive AND divisible by 5 at the same time.")
    
#OR

a = int(input("Enter a number to check: "))
if a > 0:
    print()
    if a%5 == 0:
        print("Given number is positive and divisible by 5.")
    else: print("Given number is positive but is not divisible by 5.")
else: print("Given number is not positive.")



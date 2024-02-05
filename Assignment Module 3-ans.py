# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 18:26:15 2023

@author: Joo Zhin Mei (Nancssee)
"""

# MODULE 3 Variables

# 1. What will be the output of the following (can/cannot):
    
# a. Age1=5

Age1=5
if Age1 == 5:
    print('Can')
else: print('Cannot')


# b. 5age=55

try:
    5age = 55  
    print(5age)
except:
    print("Cannot")    
"Cannot. SyntaxError shows that code was unable to be executed from the beginning."     


# 2. What will be the output of following (can/cannot):
    
# a. Age_1=100

Age_1=100
if Age_1 == 100:
    print('Can')
else: print('Cannot')
   

# b. age@1=100

age@1=100
print(age@1)
"Cannot. TypeError shows existence of unsupported symbol @." 


# 3. How can you delete variables in Python?

# Example 1:
    
a = [3, 4, 5, 6]
del a[-1]
print(a)


# Example 2:
    
try:
    b = 10
    del b
    print(b)
except: print("Deleted" )    


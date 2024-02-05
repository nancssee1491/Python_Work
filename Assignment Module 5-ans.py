# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:36:08 2023

@author: Joo Zhin Mei (Nancssee)
"""

# MODULE 5 LOOPS and Functions

# 1. 
# A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.

list1 = [1, 5.5, (10+20j), 'data science']
def list1_function(parameter1, parameter2, parameter3, parameter4):
    print(f"Parameter 1: {parameter1}")
    print(f"Parameter 2: {parameter2}")
    print(f"Parameter 3: {parameter3}")
    print(f"Parameter 4: {parameter4}")
list1_function(*list1)

    
# B) How do we create a sequence of numbers in Python.

for odd_numbers in range(1, 101, 2):
    print(odd_numbers)


# C) Read the input from keyboard and print a sequence of numbers up to that number

Input = int(input("Enter a positive whole number here: "))
while Input <= 0:
    Input = int(input("Enter a positive whole number here: "))
else:
    for Input in range(1, Input+1):
        print(Input)    


# 2. Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
# list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
# Create a dictionary such that list2 are keys and list 1 are values..

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def dictionary(list2, list1):
    return {keys: values for keys, values in zip(list2, list1)}
dictionary(list2, list1)

#OR

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

dictionary = dict(zip(list2, list1))
print(dictionary)


# 3. Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that 
# add 10 to the even number and multiply with 5 if it is odd number in the list1..

list1 = [3, 4, 5, 6, 7, 8]

def element_check(e):
    if e%2 == 0:
        return (e + 10)
    else: return e*5

list2 = list(map(element_check, list1))
print(list2)  


# 4. Write a simple user defined function that greets a person in such a way that:
# i) It should accept both name of person and message you want to deliver.
# ii) If no message is provided, it should greet a default message ‘How are you’
# Ex: Hello ---xxxx---, How are you-- --> default message.
# Ex: Hello ---xxxx---, --xx your message xx---

def greet():
    name = input("Enter your name here: ")
    if name:
        print(f"Hello {name}, are you good today? Hope you are doing well!")
    else: print("Hello there, How are you?")   
greet()    


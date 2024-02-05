# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:30:36 2023

@author: Joo Zhin Mei (Nancssee)
"""

# ASSIGNMENT-1 Data Types

# 1. Construct 2 lists containing all the available data types (integer, float, string, complex and Boolean) and do the following..

list1 = [1, 1.5, "Number", 2+3j, True]
list2 = [3, 3.5, "Text", 4j-3, False]


# a. Create another list by concatenating above 2 lists

list3 = list1 + list2
print(list3)


# b. Find the frequency of each element in the concatenated list.

list3 = [1, 1.5, 'Number', (2+3j), True, 3, 3.5, 'Text', (-3+4j), False]
print(list3.count(1))
print(list3.count(1.5))
print(list3.count('Number'))
print(list3.count(2+3j))
print(list3.count(True))
print(list3.count(3))
print(list3.count(3.5))
print(list3.count('Text'))
print(list3.count(-3+4j))
print(list3.count(False))


# c. Print the list in reverse order.

list3.reverse()
print(list3)


# 2. Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}


# a. Find the common elements in above 2 Sets.

common_elements = set1 & set2
print(common_elements)


# b. Find the elements that are not common.

set1.symmetric_difference(set2)


# c. Remove element 7 from both the Sets.

set1.remove(7)
print(set1)

set2.remove(7)
print(set2)


# 3. Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.

data ={'Selangor': 100, 'Sabah': 150, 'Sarawak': 50, 'Kelantan': 300, 'Terengganu': 200}


# a. Print only state names from the dictionary.

print(data.keys())


# b. Update another country and it’s covid-19 cases in the dictionary.

data.update({'Thailand': 1000})
print(data)







# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:37:28 2023

@author: Joo Zhin Mei (Nancssee)
"""

# MODULE 6 PACKAGES

# 1. For the dataset “Indian_cities”, 

import pandas as pd

Indian_cities = pd.read_csv(r"C:/Users/hanna/OneDrive/Desktop/Nancssee/Course Materials/Diploma In Practical Data Analytics/Python/python32hrsassignment/Module6_Indian_cities.csv")
print(Indian_cities)


# a) Find out top 10 states in female-male sex ratio

Sex_ratio_top_10_states = Indian_cities.groupby('state_name')['sex_ratio'].mean().sort_values(ascending=False).head(10)
print(Sex_ratio_top_10_states)


# b) Find out top 10 cities in total number of graduates

Total_graduates_top_10_cities = Indian_cities.groupby('name_of_city')['total_graduates'].sum().sort_values(ascending=False).head(10)
print(Total_graduates_top_10_cities)


# c) Find out top 10 cities and their locations in respect of total effective_literacy_rate.

Top_10_effective_literacy_rate_cities_locations = Indian_cities.groupby(['name_of_city', 'location'])['effective_literacy_rate_total'].mean().sort_values(ascending=False).head(10)
print(Top_10_effective_literacy_rate_cities_locations)


# 2. For the data set “Indian_cities”

import matplotlib.pyplot as plt

# a) Construct histogram on literates_total and comment about the inferences
plt.hist(Indian_cities['literates_total'])
plt.xlabel('Total Literates')
plt.ylabel('Frequency')
plt.title('Literacy Distribution')
plt.show()
"Inferences:"
'1) Histogram is heavily positive skewed, suggesting an extremely'
'low total of literacy across cities and states.'


# b) Construct scatter plot between male graduates and female graduates

plt.scatter(Indian_cities['male_graduates'], Indian_cities['female_graduates'])
plt.xlabel('Male Graduates')
plt.ylabel('Female Graduates')
plt.title('Male Graduates vs Female Graduates')
plt.show()


# 3. For the data set “Indian_cities”inferences
# a) Construct Boxplot on total effective literacy rate and draw inferences

plt.boxplot(Indian_cities['effective_literacy_rate_total'])
plt.ylabel('Total Effective Literacy Rate')
plt.xlabel('Data Set No.')
plt.title('Total Effective Literacy')
plt.show()
"Inteferences:"
'1) The total effective literacy rate are > 70% for most of the cities, with a median around 85%.'
'2) A number of cities are having a lower total effective literacy rate, beteween 50%-70%.'


# b) Find out the number of null values in each column of the dataset and delete them.

Null_values_count = Indian_cities.isna().sum()
print(Null_values_count)
Null_values_deleted = Indian_cities.dropna()
print(Null_values_deleted)



























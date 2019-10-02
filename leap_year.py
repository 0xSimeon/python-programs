# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 01:43:31 2019

@author: SIMI
"""
# A program to determine if a year is a leap year
year = int(input('Enter the year you want to check: '))
leap_year = year % 4 == 0 or year % 400 == 0 and year % 100 != 0
print(leap_year)

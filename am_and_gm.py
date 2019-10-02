
"""
Created on Sat Sep 28 13:48:54 2019

@author: SIMI (Simeon Udoh)
"""
# A program to compute the Arithmetic and Geometric Mean of 5 values
num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
num3 = int(input('Enter the 3rd number: '))
num4 = int(input('Enter the 4th number: '))
num5 = int(input('Enter the 5th number: '))
arithmetic_mean = (num1 + num2 + num3 + num4 + num5) / 5
geometric_mean = (num1 * num2 * num3 * num4 * num5) **(1/5)
print('The Arithmetic mean is = ', arithmetic_mean)
print('The Geometric mean is = ', geometric_mean)


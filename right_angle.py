"""
Created on Sat Sep 28 13:48:54 2019

@author: SIMI (Simeon Udoh)
"""

height = int(input("Enter the height : "))
base = int(input("Enter the base: "))
hypotenuse = int(input("Enter the hypotenuse side: "))
x = height + base
if x == hypotenuse:
    area = (1/2) * base * height
    perimeter = height + base + hypotenuse
    print("The area of the triangle is = ",area)
    print("The perimeter of the triangle is = ", perimeter)
    
else: 
    print("It's not a right angle triangle")
    

    

    
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:47:04 2019

@author: Simi
"""
#A fucntion to check is a string is a palindrome

def ispalindrome():
    word = input('Enter the word you want to check: ') #Get input from the user
    reverse = word[::-1] #Assigned the reversed word inputed by the user
    if word == reverse:
        print(True)
    else:
        print(False)
        
ispalindrome() #Calling the function
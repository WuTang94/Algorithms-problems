# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 00:37:49 2017

@author: Justin Tang
"""

def max2(A, B):
    print("This is homework 4 question 1.")
    """
    I searched around and found this simple, yet smart algorithm. Basically it
    focuses on the distance between the two numbers, and it adds the absolute
    value of half the distance to the average to get the bigger number (or subtracts
    to get the smaller number)
    
    link to it: http://www.programmerinterview.com/index.php/general-miscellaneous/find-max-without-comparison/
    """
    print("Max of these two numbers without comparison:", A, B)
    dist = A - B
    max = (A + B + abs(dist))/2
    return max
    
    #print(A)
    #print(B)
    #return
    



"""
Just for fun, here's how I figured you'd normally get max with comparison

def compMax(A,B):
    print("This is how we do it with comparison!")
    if (A>B):
        return A
    elif (B>A):
        return B
"""    
print(max2(2,7))

#print(compMax(2,7))
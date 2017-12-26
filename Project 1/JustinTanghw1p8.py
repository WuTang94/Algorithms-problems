# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:31:39 2017

@author: Justin Tang
"""

def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a + b)
    
def fibIt(num):
    print("Result =",fibItHelper(num, 0, 1))

noo = 5
#test print
print ("Problem 8")
print ("Input =", noo)
    
fibIt(noo)

'''
I tried printing the same values that started to run slowly on question 6, but
with this function, they run much faster. Almost as if they run almost 
instantly

Note: I tested the speed of the program by estimating the time between the
first thing I printed and printing the results of the function.
'''
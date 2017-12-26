# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:56:08 2017

@author: Justin Tang
"""
def fib(n):
    #if statement for anything <= 1. 0 and 1 both fit in this category
    if n <= 1:
        return n
    #for everything else...
    else:
        return (fib(n-1) + fib(n-2))
    print("Done")
    #print(result.str())
#our input will be called "noo". Just because
noo = 20
#just to make sure this works
print ("HW 1, problem 6 by Justin Tang")
print ("User input =", noo)
print("Fibonnaci result =", fib(noo))

"""
I started noticing a slight lag between when the input and result was printing
once the input reached around 21, and it didn’t become significantly noticeable 
until it reached 26

Note: I tested the speed of the program by estimating the time between the
first thing I printed and printing the results of the function.
"""
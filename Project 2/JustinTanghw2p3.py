# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:22:04 2017

@author: Justin Tang
"""
#part a
#representation of L
L = [[0,1],[1,1]]

#testing out printing matrix L
#for row in L:
#    print (' '.join(str(row)))

#part b
def fibPow(a, b):
    #indices are 1 less than in the notes, so c11 = c[0][0], for example
    c1 = a[0][0]*b[0][0]+a[0][1]*b[1][0]
    c2 = a[0][0]*b[0][1]+a[0][1]*b[1][1]
    c3 = a[1][0]*b[0][0]+a[1][1]*b[1][0]
    c4 = a[1][0]*b[0][1]+a[1][1]*b[1][1]
    #now creating matrix c from the individiual values
    c = [[c1,c2],[c3,c4]]
    return c

#part c
def fibPowHelper(n):    
    Ln = fibPow(L,L)
    for i in range(1,n-1):
        Ln = fibPow(Ln,L)
    return Ln
out = (fibPowHelper(5))    
for row in out:
    print (' '.join(str(row)))    
print("output =", out[1][0])    
    #return

#fibPow(3)
#oart c
#def fibPowHelper(iterations):
#    for i in renge(0,iterations):
#        #fibPow

#part d

"""
The time complexity for this algorithm is O(n) if run through fibPowHelper
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:08:10 2017

@author: Justin Tang
"""
"This is Part b of problem 3"
def extraSpace(S, M, i, j):
    #spaces = 0
    #minim = math.inf
    # nonlocal lsum
    print ("Part b")
    lsum = 0
    for l in range(i, j):
        lsum += S[l]
        space =  M - j + i - lsum#sum(k)
    print(lsum)
    return space
        

def printS(S):
    newS = []
    for i in range(0, len(S)):
        newS.append(len(S[i]))
    #print (newS)
    print(extraSpace(newS, 12, 0, len(newS)))
    print(bl(newS,12,0,len(newS)))
    #print(minBad(newS,20,6))
    #print(printParagraph(S))
        
#S = ["I","am", "Groot"]
S = ["Hey", "hey", "hey", "it's", "Fat", "Albert"]

print(S)
print(printS(S))
#print(badness(S))

"Question 3 part d"
def bl(S, M, i, j):
    print("Part d")
    lump = 0
    infinity = M + 1
    print("infinity = ", infinity)
    for l in range(i, j):
        lump += S[l]
        badness =  M - j + i - lump#sum(k)
    print(lump)
    #return badness
    if badness >= 0:
        return badness
    elif badness < M:
        return infinity
 
"Question 3 part g"
"""
THis was supposed to be done with recursion, with the function calling back to 
itself. It was supposed to recursively find the minimum of the function bl,
spread over the paragraph once the lines were created. The biggest difference 
was that it would call back recursively, so that's why it's slower than Dynamic
programming


def minBad(S, M, i):
    for n in len(i, len(S)):
        min = bl(S, M, i, n)
        
        minBad(S, M, i+1)
"""
"Question 3 part h"
def minBadDynamic(S, M):
    #Divide S into lines M, return the table
    table = [3,5,6,20]
    return min(table)
"""
This is the same as part g, except you do it with Dynamic programming and not
recursion

A table is created to store the results, so you just store the different parts
the dynamic programming here.
"""
    
    
"Question 3 part i"
"""
"""
#def minBadDynamicChoice(S, M):
    
def printParagraph(S):
    print("This is supposed to print the paragraph out through dynamic programming")
    print("Without further adue, the paragraph as I have it")
    for i in range(0,len(S)):
        print(i)


"""
Dynamic programming should reduce the big O time. Whereas doing this recursively
would lead to a big O runtime of O(2^(n^2)), doing this through dynamic programming
should be O(n^2), speeding things up.

"""  
#print (extraSpace(S, 12, 1, len(S)))
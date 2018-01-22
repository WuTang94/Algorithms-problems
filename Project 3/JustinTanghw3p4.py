# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:51:04 2017

@author: Justin Tang
"""
"""
Algorithms Homework 3, Question 4

part A
"""
array= [1, 2, 4, 5, 6, 10, 100]



def sortedHasSum(S, x):
    #hasSum = False
    lo = 0
    hi = len(S)-1
    #print (S[lo])
    #print (S[hi])
    #print(S[lo] + S[hi])
    print("The original array:", S)
    print("Chosen sum:", x)
    while lo < hi:
        if S[lo] + S[hi] == x:
            return True
        elif S[lo]+S[hi] > x:
            hi -=1
        elif S[lo]+S[hi] < x:
            lo +=1
    return False
    #sum = 0
    """
    for i in range(0,len(S)):
        #print(S[i])
        diff = x-S[i]
        
        if diff in S:
            hasSum = True
     """
    


#def addSum

#def searchSum()

print(sortedHasSum(array, 101))

"""
part B
"""
#the unsorted array
unArray= [2,4,6,10,5,100,1]

def hasSum(S, x):
    lo = 0
    hi = len(S)-1
    #print (S[lo])
    #print (S[hi])
    #print(S[lo] + S[hi])
    print("The original array:", S)
    print("Chosen sum:", x)
    mergesort(S, 0, len(S) - 1)
    print(S)
    while lo < hi:
        if S[lo] + S[hi] == x:
            return True
        elif S[lo]+S[hi] > x:
            hi -=1
        elif S[lo]+S[hi] < x:
            lo +=1
    return False

def mergesort(array, i, j):
    mid = 0
    if i < j:
        mid = int((i + j)/2)
        #print(mid)
        mergesort(array, i, mid)
        mergesort(array, mid + 1, j)
        merge(array, i, mid, j)
        
def merge(array, i, mid, j):
    #print("Left:", str(array[i:mid+1]))
    #print("Right:", str(array[mid + 1: j + 1]))
    N = len(array)
    temp = [0]*N
    l = i
    r = j
    m = mid + 1
    k = l
    while l <= mid and m <= r:
        if array[l] <= array[m]:
            temp[k] = array[l]
            l += 1
        else:
            temp[k] = array[m]
            m += 1
        k += 1
        
    while l <= mid:
        temp[k] = array[l]
        k += 1
        l += 1
    while m <= r:
        temp[k] = array[m]
        k += 1
        m += 1
        
    for i1 in range(i, j + 1):
        array[i1] = temp[i1]
    #print("After Merge: ", str(array[i:j+1]))
    
arr = [9, 5, 34, 2, 3]
print ("Initial Array: ", str(arr))
print(mergesort(arr, 0, len(arr) - 1))

print(hasSum(unArray, 101))
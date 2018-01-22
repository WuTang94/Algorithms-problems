# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:14:31 2017

@author: Justin Tang
"""

"""
this is the part we need to modify. Instead of calling quicksort twice at the
same time, we need to make it into calling it just once
"""
def quicksort(array, i, j):
    if i < j:
        pos = partition(array, i, j)
        quicksort(array, i, pos - 1)
        quicksort(array, pos + 1, j)


#this is what happens when you partition the array
def partition(arr, i, j):
    pivot = arr[j]
    small = i - 1
    for k in range(i, j):
        if arr[k] <= pivot:
            small += 1
            swap(arr, k, small)

    swap(arr, j, small + 1)
    print ("Pivot = ", str(arr[small + 1]))
    printArray(arr)
    return small + 1

#this function swaps i and j, and thus is the way quicksort organizes the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
def printArray(arr):
    print (' '.join(str(i) for i in arr))

arr = [99, 42, 8, 3, 1, 2, 52, 100, 23]
print ("Initial Array :",)
printArray(arr)
#choosing a pivot that belongs in the array 
quicksort(arr, 0, len(arr) - 1)
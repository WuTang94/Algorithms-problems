# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:30:24 2017

@author: Justin Tang
"""
#from bisect import bisect_left

def search(a, v):
    #defining lo and hi here so no need for searchHelp
    lo = 0
    hi = len(a)  
    print("Array: ", str(a))
    #print(len(a))
    #return
    while lo <= hi:
        mid = (lo + hi)//2
        if a[mid] < v:
            lo = mid+1
            return True
        elif v < a[mid]:
            hi = mid - 1
            return False
        else:
            return mid
    return None
'''
        print(lo)
        print(hi)
        x = lo + (hi - lo) // 2
        val = a[x]
        if v == val:
            return x
        elif v == val:
            if lo == x:
                break
            lo == x
        elif v < val:
            hi = x
'''
array = [2,4,5,6,3,21,9]
print(search(array,21))
#def searchHelp():
 #   return
 
 
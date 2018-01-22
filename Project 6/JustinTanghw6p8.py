# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:35:18 2017

@author: Justin Tang
"""


#this method initializes a table of zeros
#dynamicProgramming
def zeros(rows, cols):
    row = []
    data = []
    for i in range(cols):
        row.append(0)
    for i in range(rows):
        data.append(row[:])
    return data
#a = zeros(10,10) 

#the main Knapsack method, will call on another method to mark down items
def knapsack(val, weight, W):
    n = len(val)
    #c is the matrix for costs. Creating a matrix via the "zeros" method
    c = zeros(n,W+1)
    
    for i in range(0,n):
        for j in range(0,W+1):
            if weight[i] > j:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = max(c[i-1][j], val[i] + c[i-1][j-weight[i]])
    
    #let the following line print to see the computations
    #print(c)
    #return [c[n-1][W],getItemsUsed(weight,c)]
    print("Total value of things taken:",c[n-1][W])
    print("1's mark which item was taken, 0's mark an item left behind:")
    return markItems(weight,c)
    
#this method marks down which items are taken    
def markItems(w,c):
    i = len(c)-1
    currentW = len(c[0])-1
    
    marked = []
    for i in range(i+1):
        marked.append(0)
        
    while (i >= 0 and currentW >=0):
        if (i==0 and c[i][currentW] >0 )or c[i][currentW] != c[i-1][currentW]:
            marked[i] =1
            currentW = currentW-w[i]
        i = i-1
    return marked

#feel free to edit this list    
val = [500,2000,10050,1250,100000,155000]
weight = [12, 90, 100, 35, 23, 50]
#also feel free to edit W, the maximum weight we can take
print(knapsack(val, weight, 170))
    
   
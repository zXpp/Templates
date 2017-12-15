# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:40:02 2017

@author: zzpp220
"""
def arraw(arr,n):
    index_zero=arr.index(0)
    arr[0],arr[index_zero]=arr[index_zero],arr[0]
    for k in range(n-1,0,-1):
        for i in range(1,k): 
#            if arr[i]>arr[k]:
#                arr[0],arr[i]=arr[i],arr[0]
#                arr[i],arr[k]=arr[k],arr[i]
#                arr[0],arr[k]=arr[k],arr[0]
            if arr[i]>arr[i+1]:
                arr[0],arr[i]=arr[i],arr[0]
                arr[i],arr[i+1]=arr[i+1],arr[i]
                arr[0],arr[i+1]=arr[i+1],arr[0]
    return arr
    
def modiBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum >= 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True
        passnum -= 1
    return alist

def bubbleSort(alist):
    for passnum in range(len(alist)-1, -1, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

alist = [4,26,93,0,17,77,31,44,55,123]
print(bubbleSort(alist))
a=[1,3,2,6,4,0,9,5,8,7]
print arraw(alist,len(alist))
print(modiBubbleSort(alist))
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:39:12 2020

@author: Subhasis
"""

#Binary Search
import time
start = time.time()
def binarySearch(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    
    while low<=high:
        mid = low + high // 2
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return -1

a = [10,20,40,11,15,12]
a.sort()
print(a)
x = int(input())
result = binarySearch(a,x)
if result != -1:
    print(x,"found at index ",result)
else:
    print("element",x," not found.")
end = time.time()
print(f"Runtime of the program is {end - start}")
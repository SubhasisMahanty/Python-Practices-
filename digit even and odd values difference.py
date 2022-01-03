# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:36:49 2020

@author: Subhasis
"""
num = str(input("Enter the number:"))
c1,c2 = 0,0
for i in range(0,len(num)):
    if i%2 == 0:
        c1 = c1 + int(num[i])
    if i%2!=0:
        c2 = c2 + int(num[i])
print(abs(c2-c1))
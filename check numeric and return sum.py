# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:08:59 2020

@author: Subhasis
"""
print("Enter 2 no: \n")
n1,n2 = input().split(' ')
if n1.isnumeric()==1 and n2.isnumeric():
    sum = int(n1)+int(n2)
    print(sum)
else:
    print("Wrong Entry.")
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:09:33 2021

@author: Subhasis
"""

def check_division(a,b):
    t = False
    d = a+1
    while t == False:
        if d % b == 0:
            t = True
            return d
        else:
            d +=1
print(check_division(25,5))
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:52:34 2021

@author: Subhasis
"""

import random
import math
def factorial():
    n = random.randint(1,10)
    #print(n)
    if n==1:
        return (n, n)
    else:
        return (n, math.factorial(n))
    
print(factorial())
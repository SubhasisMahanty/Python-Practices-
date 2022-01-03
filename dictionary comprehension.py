# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:00:56 2020

@author: Subhasis
"""

f = ["anne","marrie","Rej"]
age = [10,7,3]
d = {
     f[i]:age[i]
     for i in range(len(f))
         if age[i] < 4
     }
print(d)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:11:11 2020

@author: Subhasis
"""

marks = [50,60,55,75,45,69,81,80]
def more_60(mark):
    return mark >60
x = list(filter(more_60,marks))
print(x)
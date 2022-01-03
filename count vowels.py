# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:58:30 2021

@author: Subhasis
"""

def count_vowels(input_string):
    vowels = ['a','e','i','o','u']
    t = list(input_string.strip())
    c = 0
    for i in t:
        if i in vowels:
            c += 1
    return c
print(count_vowels('aeiou'))
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:08:35 2020

@author: subhasish
"""
vowel = ['a','e','i','o','u']
word  = input("Enter a word for vowel count:\n")

found = {}

for letter in word:
    if letter in vowel:
        found.setdefault(letter, 0)
        found[letter] += 1       
for i,j in sorted(found.items()):
       print(i,'was found',j,'times')

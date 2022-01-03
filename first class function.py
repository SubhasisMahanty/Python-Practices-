# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:15:31 2020

@author: Subhasis
"""

def hello():
    name = input("enter your name:")
    print(f"Hello {name}.How are you:?")
    mood = input()
    if(mood.lower()=="good" or mood.lower() == "very good" or mood.lower()=="ok" or mood.lower()=="fine"):
        print("Have a nice day.")
    else:
        print("Every day is not a Good Day.")
        
    
a = hello
a()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:55:02 2021

@author: Subhasis
"""
T=int(input())
N,K=int(input()),int(input())

l=[]
a=[]
x=len(l)
for i in range(T):
    for i in range(N):
        l.append(int(input()))
    for i in range(K):
        l.reverse()
        a.append(l[i])
        l.remove(l[i])
        l.reverse()
    a.reverse()
    z=a.extend(l)
print(z)
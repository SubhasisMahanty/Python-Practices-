# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:18:55 2020

@author: Subhasis

Consider the following series:
    1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, 64, 729, 128, 2187 …

This series is a mixture of 2 series – 
all the odd terms in this series form a geometric series and 
all the even terms form yet another geometric series. 
Write a program to find the Nth term in the series.

The value N in a positive integer that should be read from STDIN.
The Nth term that is calculated by the program should be written to STDOUT. 
Other than value of n th term,no other character / string or message should be 
written to STDOUT.
For example , if N=16, the 16th term in the series is 2187,
so only value 2187 should be printed to STDOUT.

You can assume that N will not exceed 30.
"""
a,b=1,1
print("In:\n")
n = int(input())
for i in range(1,n+1):
    if i%2!=0:
        a = a * 2
    else:
        b=  b * 3
if n%2!=0:
    print("{}th term is {}".format(n,int(a)))
else:
    print("{}th term is {}".format(n,int(b)))
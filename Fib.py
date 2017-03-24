# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:44:33 2017

@author: gaaolitong
"""

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(120):
    print('fib('+ str(i) +') =', fib(i))

def fastFib(n, memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
for i in range(120):
    print('fib('+ str(i) +') =', fastFib(i))
    

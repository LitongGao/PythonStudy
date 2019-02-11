#!/usr/bin/env python
# -*- coding:utf-8 -*-

def f(x):
    return x*x

def add(x ,y):
    return x+y

def fn(x ,y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(fn, map(char2num, s))

def normalize(s):
    return s.capitalize()

def normalize_2(s):
    return s[:1].upper() + s[1:].lower()

def not_empty(s):
    return s and s.strip()

l0 = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
demo = ['adam', 'LISA', 'barT', ' ']
demo_update = map(normalize, demo)
demo_update_2 = map(normalize_2, demo_update)
l2list = list(demo_update)
L = [1,2,3,4,5,6,7,8,9]
L2 = map(f, L)
L_str = map(str, L)
sum = reduce(add, L)
sum_1 = reduce(fn, L)
char2num_1 = char2num('2')
char2num_2 = map(char2num, "13456")
sum_2 = reduce(fn, char2num_2)
sum_3 = reduce(fn, map(char2num, "13456"))
sum_4 = str2int("12345678")


if __name__ == "__main__":
    print L2
    print L_str
    print sum
    print sum_1
    print char2num_1
    print char2num_2
    print sum_2
    print sum_3
    print sum_4
    print demo_update
    print demo_update_2
    print l0
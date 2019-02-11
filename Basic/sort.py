#!/usr/bin/env python
# -*- coding:utf-8 -*-

def sort():
    a = "I am a boy"
    print (a[-1:])
    b = a.split(" ")
    print (b)
    c = []
    for i in range(len(b)-1,-1,-1):
        c.append(b[i])
    print (c)
    b.reverse()
    print(b)

if __name__ == "__main__":
    sort()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868198760391f49337a8bd847978adea85f0a535591000
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1= count()

def count_upgrade():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f2,f3,f4 = count_upgrade()

f = lambda x:x*x
if __name__ == "__main__":
    print f1[0]()
    print f2()
    print f(5)
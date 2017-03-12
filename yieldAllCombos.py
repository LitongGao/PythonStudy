# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:45:49 2017

@author: gaaolitong
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
    #print (combo)
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)    
    for i in range(3**N):
        T = ([],[])
        for j in range(N):
            if (i // (3**j)) % 3 == 1:
                T[0].append(items[j])
            elif (i // (3**j)) % 3 == 2:
                T[1].append(items[j])
        yield T
    #print (T)
def yieldA2(items):
        N = len(items)
        for i in range(3**N):
            bag1 = []
            bag2 = []
            for j in range(N):
                if (i // (3 ** j)) % 3 == 1:
                    bag1.append(items[j])
                elif (i // (3 ** j)) % 3 == 2:
                    bag2.append(items[j])
            yield (bag1, bag2)
items=['a','b','c']
powerSet(items)
#yieldAllCombos(items)
for i in yieldAllCombos(items):
    print (i, " ")
print("===============================")
for i in yieldA2(items):
    print (i, " ")
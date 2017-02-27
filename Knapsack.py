# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                +', ' + str(self.calories) + '>'
def buildMenu(names, values, calories):
    """names, values, calores lists of same length.
        name a list of string
        value and calories lists of numbers
        return list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = [] 
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <=maxCost:
                result.append(itemsCopy[i])
                totalCost += itemsCopy[i].getCost()
                totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken=', val)
    for item in taken:
        print(' ', item)
def testGreedys(maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, Food.density)
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)    

def maxValue(foods, maxUnits):
    if foods == [] or maxUnits == 0:
        result = (0, ())
    elif foods[0].getCost() > maxUnits:
        result = maxValue(foods[1:], maxUnits)
    else:
        nextItem = foods[0]
        #select left side
        withValue, withToTake = maxValue(foods[1:], 
                                         maxUnits - nextItem.getCost())
        withValue += nextItem.getValue()
        #select right side
        withOutValue, withOutTake = maxValue(foods[1:], maxUnits)
        #compare which way is best
        if withValue > withOutValue:
            result = (withValue,withToTake + (nextItem,))
        else:
            result = (withOutValue, withOutTake)
    return result
def testMaxValue(foods, maxUnits):
    print('\ntest the maxValue method')
    print(maxValue(foods, maxUnits))
    val , taken = maxValue(foods, maxUnits)
    for item in taken:
        print(' ', item)
    
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
#testGreedys(foods, 95)
testMaxValue(foods, 95)
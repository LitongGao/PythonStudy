s2 = 'Hello, \'Adam\''
print(s2)
s3 = r'Hello, "Bart"'
print s3
s4 = r'''Hello,
Lisa!'''
print s4
print(ord('A'))
print(chr(254))
print ('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%4d-%03d' % (3, 1))

classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print classmates[-1]
classmates.append("aaa")
print classmates
classmates.pop(0)
print classmates
classmates.insert(0,'litong')
print classmates
classmates[1] = 'heping'
print classmates
t = ('Michael', 'Bob', 'Tracy')
print t[1]
t2 = ('a', 'b', ['A', 'B'])
print t2[2][1]
t2[2][1] = 'C'
print t2

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print L[0][0]
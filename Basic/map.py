dica = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': "hello"}
dicb = {'b': 3, 'd': 5, 'e': 7, 'm': 9, 'f': "_11",'k': 'world'}
#正确答案
dic = {}
for key in dica:
    if dicb.get(key):
        dic[key] = dica[key] + dicb[key]
    else:
        dic[key] = dica[key]
for key in dicb:
    if dica.get(key):
        pass
    else:
        dic[key] = dicb[key]
print(dic)

#他的错误答案
d = {}
for i,j in dica.items():
    for m, n in dicb.items():
        if i == m:
            d[i] = dica[i] + dica[m]
        elif m not in d.keys():
            d[m] = n
print d
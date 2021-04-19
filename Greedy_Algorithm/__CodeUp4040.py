data = dict()
data['a'] = 'apple'
data['b'] = 'banana'

print(data.keys())
print(list(data.keys()))

from itertools import product
data = ['a','b','c']
print(list(product(data,repeat=2)))
print(list(product(data,repeat=3)))

from collections import Counter
counter = Counter(['1','2','3','4','1','2','1','2','3','1','1'])
print(counter['1'], dict(counter))
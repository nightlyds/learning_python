from collections import ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict
from collections.abc import *

# ChainMap
print("ChainMap examples")

toys = {'Blocks': 30, 'Monopoly': 20}
computers = {'iMac': 1000, 'Chromebook': 800, 'PC': 400}
clothing = {'Jeans': 40, 'T-Shirt': 10}

# Default case
inventory = toys.copy()
inventory.update(computers)
inventory.update(clothing)

print(inventory) # Output: {'Blocks': 30, 'Monopoly': 20, 'iMac': 1000, 'Chromebook': 800, 'PC': 400, 'Jeans': 40, 'T-Shirt': 10}
print(inventory['Blocks']) # Output: 30

# With collections module
inventory = ChainMap(toys, computers, clothing)

print(inventory) # Output: ChainMap({'Blocks': 30, 'Monopoly': 20}, {'iMac': 1000, 'Chromebook': 800, 'PC': 400}, {'Jeans': 40, 'T-Shirt': 10})
print(inventory['Blocks']) # Output: 30

# It fails with the standart update method
toys['Nintendo'] = 200
print(inventory['Nintendo']) # Output: 200

# Counter
print("\nCounter examples")

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt) # Output: Counter({'blue': 3, 'red': 2, 'green': 1})

c = Counter('gallahad')
print(c) # Output: Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
print(c.most_common(3)) # [('a', 3), ('l', 2), ('g', 1)]

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

c.subtract(d)

print(c) # Output: Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

# deque
print("\ndeque examples")

d = deque('ghikl')
print(d) # Output: deque(['g', 'h', 'i', 'k', 'l'])

d.appendleft('q')
print(d) # Output: deque(['q', 'g', 'h', 'i', 'k', 'l'])

d.popleft()
print(d) # Output: deque(['g', 'h', 'i', 'k', 'l'])

e = deque('eqwe')

d.extendleft(e)
print(d) # Output: deque(['e', 'w', 'q', 'e', 'g', 'h', 'i', 'k', 'l'])

# defaultdict
print('\ndefaultdict examples')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(d) # Output: defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d) # Output: defaultdict(<class 'int'>, {'The': 1, 'red': 1, 'for': 2, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'food': 1})

# namedtuple
print('\nnamedtuple examples')

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, 22)

print(p) # Output: Point(x=11, y=22)
print(p[0] + p[1]) # Output: 33
print(p.x, p.y) # Output: 11 22

# unpack like a regular tuple
x, y = p
print(x, y) # Output: 11 22

p = p._replace(y=23) # Need to assign a new tuple to the old
print(p.x, p.y) # Output: 11 23

# OrderDict
print("\nOrderDict examples")

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)

# Before:
#
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)
#
# After:
#
# ('a', 1)
# ('b', 2)
# ('c', 5)
# ('d', 4)

# collections.abc
print('\ncollections.abc examples')

print(f'[0, 1, 2, 3] is Iterable {isinstance([0, 1, 2, 3], Iterable)}') # Output: True
print(f'1 is Iterable {isinstance(1, Iterable)}') # Output: False

object = {"one": 1, "two": 2, "three": 3}
print(f'{object} is Collection {isinstance(object, Collection)}') # Output: True

tuple_implementation = (1, 2, 3)

print(f'{tuple_implementation} is Sequence {isinstance(tuple_implementation, Sequence)}') # Output: True

set_implementation = set()

print(f'{set_implementation} is Set {isinstance(set_implementation, Set)}') # Output: True
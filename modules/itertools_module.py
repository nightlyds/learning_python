from itertools import accumulate, chain, combinations, \
                      combinations_with_replacement, \
                      compress, count, cycle, dropwhile, \
                      filterfalse, groupby, islice, \
                      permutations, product, repeat, starmap, \
                      takewhile, tee, zip_longest

# accumulate
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

# by default adds previous value to current
# and write their sum
print(list(accumulate(data))) # [3, 7, 13, 15, 16, 25, 25, 32, 37, 45]

def multiply(a, b):
    return a * b

# it has oppurtunity to set
# the second argument that is a function
print(list(accumulate(data, multiply))) # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]

# chain
# makes generator from iterable values
chain_impl = chain([1, 2], [3, 4], [5, 6, 7])

try:
    while chain_impl:
        # on the end will throw StopIteration
        print(next(chain_impl), end=" ") # 1 2 3 4 5 6 7 StopIteration

except:
    print("StopIteration")

# chain.from_iterable
# the same like chain
# but takes only one argument
chain_from_iterable_impl = chain.from_iterable(["ABC", "DEF"])

try:
    while chain_from_iterable_impl:
        print(next(chain_from_iterable_impl), end=" ") # A B C D E F StopIteration

except:
    print('StopIteration')

# combinations
# Return r length subsequences of elements from the input iterable.

# [('A',), ('B',), ('C',), ('D',)]
print(list(combinations("ABCD", 1)))

# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
print(list(combinations("ABCD", 2)))

# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
print(list(combinations("ABCD", 3)))

# [('A', 'B', 'C', 'D')]
print(list(combinations("ABCD", 4)))

# combinations_with_replacement
# Return r length subsequences of elements from the input
# iterable allowing individual elements to be repeated more than once.

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(combinations_with_replacement("ABC", 2)))

# compress
# Make an iterator that filters elements from data returning only those
# that have a corresponding element in selectors that evaluates to True.

Codes =['C', 'C++', 'Java', 'Python']
selectors = [False, False, False, True]

print(list(compress(Codes, selectors))) # ['Python']

# count
count_impl = count(0, 5) # start, step

for i in range(1, 10):
    print(next(count_impl), end=" ") # 0 5 10 15 20 25 30 35 40

# cycle
cycle_impl = cycle("123")

for i in range(1, 10):
    print(next(cycle_impl), end=" ") # 1 2 3 1 2 3 1 2 3

# dropwhile
print(list(dropwhile(lambda i: i < 5, [1, 4, 6, 4, 1]))) # [6, 4, 1]

# filterfalse
print(list(filterfalse(lambda i: i % 2, range(10)))) # [0, 2, 4, 6, 8]

# groupby
print([k for k, g in groupby('AAAABBBCCDAABBB')]) # ['A', 'B', 'C', 'D', 'A', 'B']

# [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
print([list(g) for k, g in groupby('AAAABBBCCD')])

# islice
print(list(islice('ABCDEFG', 2))) # ['A', 'B']
print(list(islice('ABCDEFG', 2, 4))) # ['C', 'D']
print(list(islice('ABCDEFG', 2, None))) # ['C', 'D', 'E', 'F', 'G']
print(list(islice('ABCDEFG', 0, None, 2))) # ['A', 'C', 'E', 'G']

# permutations

# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'),
# ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'),
# ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
print(list(permutations("ABCD", 2)))

# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
print(list(permutations(range(3))))

# product

# [('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b'), ('C', 'a'), ('C', 'b')]
print(list(product("ABC", 'ab')))

# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
print(list(product(range(2), repeat=3)))

# repeat
print(list(repeat(10, 3))) # [10, 10, 10]

# starmap
print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)]))) # [32, 9, 1000]

# takewhile
# Make an iterator that returns elements from the iterable
# as long as the predicate is true.
print(list(takewhile(lambda i: i<5, [1, 4, 6, 4, 1]))) # [1, 4]

# tee
tee_impl = tee([2, 4, 6, 8, 10, 20], 3)

for i in range(0, 3):
    # [2, 4, 6, 8, 10, 20]
    # [2, 4, 6, 8, 10, 20]
    # [2, 4, 6, 8, 10, 20]
    print(list(tee_impl[i]))

# zip_longest
# [('A', 'a'), ('B', 'b'), ('C', '-'), ('D', '-')]
print(list(zip_longest("ABCD", "ab", fillvalue="-")))
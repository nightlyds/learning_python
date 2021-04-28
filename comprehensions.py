# List comprehensions
squares = []

for x in range(10):
    squares.append(x**2)

print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent to, by using map with lambda function or list comprehensions:
squares_map_lambda = list(map(lambda x: x**2, range(10)))
print(squares_map_lambda) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# or
squares_comprehensions = [x**2 for x in range(10)]
print(squares_comprehensions) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# We using dual brackets for making sets of x, y numbers
# also we have the condition, if x != y, but if x == y
# then the for-loop throw away that sequence
implementation_list_of_sets = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1] if x != y]
print(implementation_list_of_sets) # Output: [(1, 3), (1, 2), (2, 3), (2, 1), (3, 2), (3, 1)]

def function_implementation(x):
    return x * 2 + 1

list_implementation_for_function = [function_implementation(x) for x in [1, 2 ,3]] # Call function_implementation for every 'x'
print(list_implementation_for_function) # Output: [3, 5, 7]

matrix = [[1, 2, 3], [4, 5, 6]]

list_implementation_for_matrix = [num for elem in matrix for num in elem] # For every array in 'matrix', take every number inside
print(list_implementation_for_matrix) # Output: [1, 2, 3, 4, 5, 6]

# Dictionaries comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # Output: {'r', 'd'}

implementation_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
b = {k:v*2 for (k,v) in implementation_dictionary.items()}
print(b) # Output:{'e': 10, 'a': 2, 'c': 6, 'b': 4, 'd': 8}

# Enumarate list
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 0 tic
# 1 tac
# 2 toe

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null) # Output: Trondheim
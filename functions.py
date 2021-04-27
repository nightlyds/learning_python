from functools import reduce

# Map
print("MAP:")
array = [0, 1, 2, 3]


def function(x):
    return x + 1


result = list(map(function, array))

print(result)


def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]

for i in range(10):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Filter
print("FILTER:")
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Reduce
print("REDUCE:")
product = 1
array = [1, 2, 3, 4]

for num in array:
    product = product * num

print(f'Product: {product}')

# An alternative way with reduce
# It needs to import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

print(f'Product: {product}')

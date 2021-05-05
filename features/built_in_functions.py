print(abs(-1)) # Output: 1 | return number`s module.

print(all([1, 2, 3])) # Output: True | because all elements inside are True.

print(any([False, None, [], 1])) # Output: True | Return True if any element of the iterable is true.

print(bin(10)) # Output: 0b1010 | convert int to binary string.
print(format(10, '#b'), format(10, 'b')) # Output: ('0b1110', '1110')
print(bin(3)) # Output: 0b11
print(format(3, '11')) # 3

print(bool(1)) # Output: true | return bool value

# breakpoint() # pdb debugger

# callable
def implementation_def():
    pass

print(callable(implementation_def)) # Output: True

# compile
code = "a=5\nb=5\nsum_implementation=a+b\nprint(f'Executed by compile function {sum_implementation}')"
codeObject = compile(code, 'code', 'exec')
exec(codeObject)

# dict
print(dict(a=5, b=4)) # Output: {'a': 5, 'b': 4}

# dir
print(dir()) # Without arguments, return the list of names in the current local scope.

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

s = Shape()
print(dir(s))

# divmod
print(divmod(10, 3)) # Output: (3, 1) | return pair of numbers consisting of their quotient and remainder

# enumerate
for i, l in enumerate(['a', 'b', 'c', 'd']):
    print(i, l)

# eval
number = 5
print(eval('number + 3')) # Output: 8

# int
print(int('1')) # Output: 1 | transform into int

print(bin(11)) # Output: 0b1011
print(int('0b1011', 2)) # Output: 11

# max
print(max([1, 4, 1241, 2, 12, 5])) # Output: 1241 | return maximum value

# min
print(min([1, 4, 1241, 2, 12, 5])) # Output: 1 | return minimum value

# flaot
print(float('+1.23')) # Output: 1.23

print(float('   -12345\n')) # Output: -12345.0

print(float('1e-003')) # Output: 0.001

print(float('+1E6')) # Output: 1000000.0

print(float('-Infinity')) # Output: -inf

# round
print(round(5.76543, 2)) # Output: 5.77

# str
print(str(1)) # Output: 1

# set
implementation_set = set('abdasdsdasdas') # take unique characters
print(implementation_set) # Output: {'b', 'd', 's', 'a'}

# frozenset
implementation_frozenset = frozenset('abdasdsdasdas') # the same like set(), but immutable
print(implementation_frozenset) # Output: frozenset({'s', 'a', 'd', 'b'}

# len
print(len([1])) # Output: 1 | return lenght of the object

# range
# range(a, b, c) -> start, end, step
print(list(range(10))) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

implementation_list = [1, 2, 3]

# range only once initialize the value
# for example, the next example is not infinity loop
# because, after first iteration
# the look will be: for i in [1, 2, 3]
for i in range(len(implementation_list)):
    print(i)
    implementation_list.append(i)

# reversed
print(list(reversed([1, 2, 3]))) # Output: [3, 2, 1]

# slice
list_implementation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
slice_implementation = slice(9)

print(list_implementation[slice_implementation]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_implementation[:9]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sorted
print(sorted([1, 3, 2, 5, 4])) # Output: [1, 2, 3, 4, 5]
print(sorted([1, 3, 2, 5, 4], key=None, reverse=True)) # Output: [5, 4, 3, 2, 1]

# sum
# fsum from math module is more correctly
print(sum([2.5, 3, 4, -5])) # Output: 4,5

# tuple
print(tuple([1, 2, 3])) # Output: (1, 2, 3)

# list
print(list(('1', '2', '3'))) # Output: ['1', '2', '3']

# iter
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter)) # Output: a
print(next(vowels_iter)) # Output: e
print(next(vowels_iter)) # Output: i
print(next(vowels_iter)) # Output: o
print(next(vowels_iter)) # Output: u

# getattr
class Person:
    def name(self):
        pass

person = Person()
print(person.name)
# Equivalent to:
print(getattr(person, 'name'))

# hasattr
print(hasattr(person, 'name')) # Output: True

# setattr
def lastname(self):
    pass

setattr(person, 'lastname', lastname)
print(hasattr(person, 'lastname')) # Output: True

# globals
print(globals()) # Return a dictionary representing the current global symbol table.

# locals
print(locals()) # Update and return a dictionary representing the current local symbol table.

# hash
print(hash(1)) # Output: 1
print(hash('1')) # Output: hash_code
print(hash('1')) # Output: the same hash_code like previus

# help
help(hash) # return info about function

# id
print(id({})) # return id of the object
a = [1, 2, 3]
b = 1

# id for objects
print(a, id(a))
print(b, id(b))

a.append(4)
b = 2

print(a, id(a)) # the same id
# changed id, because immutable types
# use reassign and that`s the cause
# of rewriting the id
print(b, id(b))

# input
input_text = input("type text: ")
print(input_text) # return the inputed text

# isistance
print(isinstance(1, int)) # Output: True
print(isinstance([], list)) # Output: True
print(isinstance(set(), set)) # Output: True

# Also isistance function can be used with
# collections.abc module

# issubclass
class A:
    pass

class B(A):
    pass

print(issubclass(B, A)) # Output: True | because B inherit A

# pow
print(pow(38, -1, mod=97)) # Output: 23
print(23 * 38 % 97 == 1) # Output: True

print(pow(2, 3)) # Output: 8

# repr
print(repr(Person)) # Output: <class '__main__.Person'>

# type
# also type can be used for creating metaclasses
print(type(1)) # Output: <class 'int'>

# vars
print(vars()) # Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

# zip
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y) # zip
print(list(zipped)) # Output: [(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y)) # unzip by using *
print(x2, y2) # Output: (1, 2, 3) (4, 5, 6)
from functools import lru_cache, partial, update_wrapper, singledispatch, total_ordering

# lru_cache
print('lru_cache examples')

@lru_cache(maxsize=24)
def recursion(n):
    return n * recursion(n-1) if n else 1

print(recursion(10)) # 10 new recursion calls
print(recursion(5)) # without new calls
print(recursion(12)) # 2 new recursion calls

# partial
print('partial examples')

def multiply(a, b):
    return a * b

reordering_multiply = partial(multiply, 2) # set 2 for a argument, also we can use b=2 for setting 2 for b argument

print(reordering_multiply(4)) # Output: 8 | because 4 is set for b argument

# update_wrapper
print('update_wrapper examples')

print(multiply.__name__, multiply.__doc__)

# print(reordering_multiply.__name__, reordering_multiply.__doc__)
# Output:
# AttributeError: 'functools.partial' object has no attribute '__name__'
# partial(func, *args, **keywords) - new function with partial application
# of the given arguments and keywords.

update_wrapper(reordering_multiply, multiply)
print(reordering_multiply.__name__, reordering_multiply.__doc__) # works fine after updating wrapper

# singledispatch
print('singledispatch examples')

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
        print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

@fun.register(float)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)

def nothing(arg, verbose=False):
    print("Nothing.")

fun.register(type(None), nothing)

fun(1, verbose=True)
fun(['a', 'b'], verbose=True)
fun(1.2, verbose=True)
fun(None)

# total_ordering
print('total_ordering examples')

@total_ordering
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

jake = Student('Jake', 'LastName')
mike = Student('Mike', 'LastName')

print(jake._is_valid_operand(mike)) # True | has firstname and lastname, means is valid
print(mike.__eq__(jake)) # False | firstname is not the same
print(jake.__lt__(mike)) # True | comparison firstname and lastname, as such: 'J' < 'M' -> True

print(mike == jake) # False
print(jake < mike) # True

# The correspondence between operator symbols and method names is as follows:
# x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y),
# x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).
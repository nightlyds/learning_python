from multimethod import multimethod


@multimethod
def sum(x: int, y: int):
    return x + y


@multimethod
def sum(x: str, y: str):
    return x + " " + y

# The above example is similar to

def sum_two(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y

    elif isinstance(x, str) and isinstance(y, str):
        return x + ' ' + y


class GFG(object):

    @multimethod
    def double(self, x: int):
        print(2 * x)

    @multimethod
    def double(self, x: complex):
        print("sorry, I don't like complex numbers")


# Driver Code
obj = GFG()
obj.double(3)
obj.double(6j)
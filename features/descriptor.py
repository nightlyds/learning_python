class RevealAccess:
    """ The data descriptor, which set and return a value
    and print a message about accessing to the attribute.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Get', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Upgrade', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, "var 'x'")
    y = 5


m = MyClass()
print(m.x)  # Get var 'x'\n10
m.x = 20
# Upgrade var 'x'
print(m.x)
# Get var 'x'\n20
print(m.y)  # 5


class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')

        instance.__dict__[self.name] = value

    # Calls in time of creating the class.
    # In this case descriptor assigns to the name of the attribute.
    # for example:     # if call: price = NonNegative()
    # 'price' is the attribute and uses for
    # assigning as field for the descriptor.
    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
apple_order.total()  # 10

apple_order.price = -10
# ValueError: Cannot be negative
apple_order.quantity = -10
# ValueError: Cannot be negative

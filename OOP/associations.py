class A:
    pass

# Composition
class B:

    def __init__(self):
        self.a = A()

    def return_class(self):
        return self.a

# Aggregation
class C:

    def __init__(self, a):
        self.a = a

    def return_class(self):
        return self.a

a = A()
c = C(a)
print(c.return_class())

b = B()
print(b.return_class())


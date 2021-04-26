def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    It returns object-class, which names of the attributes
    is transformed to UpperCase
    """

    # take any attribute, which doesn`t start with '__'
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # transform it into UpperCase
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # create class by 'type'
    return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Foo(metaclass=UpperAttrMetaclass): # metaclass=upper_attr - for using function as metaclass

    bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False

print(hasattr(Foo, 'BAR'))
# Out: True

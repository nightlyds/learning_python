# Function decorator
def mydecorator(function):

    def wrapper():

        print('Something')

        value = function()

        print(f'Something two and {value}')

    return wrapper

@mydecorator
def something_def():
    return 'Something between'

something_def()

# Class decorator
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # We can add some code
        # before function call

        self.function()

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")

function()
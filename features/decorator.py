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
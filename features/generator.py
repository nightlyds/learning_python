def mygenerator():
    yield print('This is generator')

next(mygenerator())
next(mygenerator())
next(mygenerator())
next(mygenerator())

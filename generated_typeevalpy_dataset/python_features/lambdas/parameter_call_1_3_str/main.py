# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a('huiut')


y = lambda x: x + 'huiut'

b = func(y)

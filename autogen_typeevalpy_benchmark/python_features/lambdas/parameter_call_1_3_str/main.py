# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a('pijle')


y = lambda x: x + 'pijle'

b = func(y)

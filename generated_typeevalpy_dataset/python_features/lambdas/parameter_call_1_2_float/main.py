# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(9.3)


y = lambda x: x + 9.3

b = func(y)

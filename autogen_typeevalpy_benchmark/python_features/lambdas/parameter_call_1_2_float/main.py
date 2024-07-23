# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(2.4)


y = lambda x: x + 2.4

b = func(y)

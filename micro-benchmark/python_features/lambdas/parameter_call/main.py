# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(1)


y = lambda x: x + 1

b = func(y)

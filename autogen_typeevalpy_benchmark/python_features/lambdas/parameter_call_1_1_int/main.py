# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(81)


y = lambda x: x + 81

b = func(y)

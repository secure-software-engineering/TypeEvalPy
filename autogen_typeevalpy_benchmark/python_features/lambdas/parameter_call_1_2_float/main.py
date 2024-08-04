# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(55.03)


y = lambda x: x + 55.03

b = func(y)

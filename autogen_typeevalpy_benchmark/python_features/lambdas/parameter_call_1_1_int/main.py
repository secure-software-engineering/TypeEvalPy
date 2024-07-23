# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a(45)


y = lambda x: x + 45

b = func(y)

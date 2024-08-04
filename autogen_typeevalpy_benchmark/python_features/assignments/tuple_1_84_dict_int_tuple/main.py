# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'endyw': 93, 'pwciw': 11, 'jmknn': 44}


def func2():
    return 44


def func3():
    return (76, 6, 32)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

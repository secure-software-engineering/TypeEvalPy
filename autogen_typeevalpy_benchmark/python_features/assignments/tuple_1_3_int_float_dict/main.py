# Two variables are assigned a value via a tuple assignment.
def func1():
    return 57


def func2():
    return 9.07


def func3():
    return {'lrbaa': 47, 'iypfe': 3, 'vyosu': 63}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

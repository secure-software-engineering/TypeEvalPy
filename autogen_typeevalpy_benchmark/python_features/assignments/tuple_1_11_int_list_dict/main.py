# Two variables are assigned a value via a tuple assignment.
def func1():
    return 24


def func2():
    return [42, 46, 75]


def func3():
    return {'wnmsd': 14, 'ldchr': 3, 'porsz': 75}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

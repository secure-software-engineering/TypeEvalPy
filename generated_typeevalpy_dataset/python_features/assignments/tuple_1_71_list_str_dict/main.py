# Two variables are assigned a value via a tuple assignment.
def func1():
    return [12, 88, 21]


def func2():
    return 'rmpzp'


def func3():
    return {'nnkbe': 32, 'lgchw': 34, 'sroai': 46}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

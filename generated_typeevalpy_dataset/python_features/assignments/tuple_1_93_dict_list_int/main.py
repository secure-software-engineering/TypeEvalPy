# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'nnuum': 12, 'wxyzj': 62, 'jrttx': 3}


def func2():
    return [19, 33, 1]


def func3():
    return 84


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

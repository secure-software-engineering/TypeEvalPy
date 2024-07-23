# Two variables are assigned a value via a tuple assignment.
def func1():
    return 65.85


def func2():
    return {'xtvfu': 51, 'oobif': 13, 'dxrnu': 44}


def func3():
    return [100, 58, 66]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

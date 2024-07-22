# Two variables are assigned a value via a tuple assignment.
def func1():
    return (11, 44, 30)


def func2():
    return {'jikgr': 67, 'lmnle': 87, 'gsypm': 86}


def func3():
    return 8.07


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

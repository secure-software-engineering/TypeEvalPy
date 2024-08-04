# Two variables are assigned a value via a tuple assignment.
def func1():
    return 19.77


def func2():
    return {'jtddr': 11, 'avsyg': 36, 'yfqdu': 37}


def func3():
    return [46, 19, 76]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

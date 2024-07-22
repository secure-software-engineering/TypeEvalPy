# Two variables are assigned a value via a tuple assignment.
def func1():
    return 96.64


def func2():
    return 'cutdb'


def func3():
    return {'jonhg': 15, 'fojmh': 70, 'onhoh': 29}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

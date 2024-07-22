# Two variables are assigned a value via a tuple assignment.
def func1():
    return [68, 12, 52]


def func2():
    return {'fvmkg': 69, 'cnqxn': 30, 'lsrap': 10}


def func3():
    return 'ndqvr'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

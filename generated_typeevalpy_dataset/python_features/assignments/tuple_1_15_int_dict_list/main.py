# Two variables are assigned a value via a tuple assignment.
def func1():
    return 12


def func2():
    return {'zyirt': 78, 'bqusm': 31, 'attjo': 61}


def func3():
    return [14, 18, 96]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'bmyqt': 65, 'zgsbc': 61, 'kvbyp': 24}


def func2():
    return (53, 16, 69)


def func3():
    return [74, 20, 72]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

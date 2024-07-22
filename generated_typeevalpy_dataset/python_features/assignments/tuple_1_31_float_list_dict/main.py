# Two variables are assigned a value via a tuple assignment.
def func1():
    return 22.68


def func2():
    return [91, 84, 67]


def func3():
    return {'kjyfi': 32, 'ldsyw': 79, 'omwop': 16}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

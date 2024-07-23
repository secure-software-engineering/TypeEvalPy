# Two variables are assigned a value via a tuple assignment.
def func1():
    return [71, 62, 74]


def func2():
    return {'fdioy': 25, 'spbau': 19, 'sytnt': 63}


def func3():
    return 68.52


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

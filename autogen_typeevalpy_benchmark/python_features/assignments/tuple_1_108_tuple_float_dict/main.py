# Two variables are assigned a value via a tuple assignment.
def func1():
    return (33, 66, 97)


def func2():
    return 6.38


def func3():
    return {'dwpof': 81, 'uzxel': 29, 'okmdi': 95}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

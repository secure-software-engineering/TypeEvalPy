# Two variables are assigned a value via a tuple assignment.
def func1():
    return 7.04


def func2():
    return [33, 99, 67]


def func3():
    return {'yyhfr': 96, 'qtojx': 76, 'updda': 64}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return [88, 58, 42]


def func2():
    return {'hxycm': 85, 'nodtz': 48, 'jthuf': 1}


def func3():
    return 54.7


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

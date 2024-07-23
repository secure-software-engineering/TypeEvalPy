# Two variables are assigned a value via a tuple assignment.
def func1():
    return (85, 96, 68)


def func2():
    return [79, 65, 32]


def func3():
    return {'zliia': 59, 'sndzj': 11, 'pibcn': 81}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

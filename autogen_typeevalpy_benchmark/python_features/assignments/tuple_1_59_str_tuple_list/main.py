# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'zsdhe'


def func2():
    return (27, 41, 55)


def func3():
    return [67, 35, 6]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

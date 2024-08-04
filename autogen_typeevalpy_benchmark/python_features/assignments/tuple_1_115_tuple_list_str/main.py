# Two variables are assigned a value via a tuple assignment.
def func1():
    return (6, 55, 75)


def func2():
    return [1, 41, 60]


def func3():
    return 'yuzcn'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

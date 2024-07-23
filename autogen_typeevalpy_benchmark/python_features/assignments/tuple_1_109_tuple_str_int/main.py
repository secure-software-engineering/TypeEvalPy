# Two variables are assigned a value via a tuple assignment.
def func1():
    return (82, 54, 43)


def func2():
    return 'lmpff'


def func3():
    return 22


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return [48, 35, 91]


def func2():
    return 'ynfiy'


def func3():
    return (45, 86, 97)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

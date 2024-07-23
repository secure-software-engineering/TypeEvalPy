# Two variables are assigned a value via a tuple assignment.
def func1():
    return (63, 21, 86)


def func2():
    return 'ufvqc'


def func3():
    return [58, 12, 47]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return 80


def func2():
    return (77, 49, 55)


def func3():
    return 'iuggr'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

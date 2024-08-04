# Two variables are assigned a value via a tuple assignment.
def func1():
    return 67


def func2():
    return (41, 75, 2)


def func3():
    return 'durdu'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

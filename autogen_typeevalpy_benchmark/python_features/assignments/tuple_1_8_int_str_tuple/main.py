# Two variables are assigned a value via a tuple assignment.
def func1():
    return 55


def func2():
    return 'iredl'


def func3():
    return (83, 9, 70)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

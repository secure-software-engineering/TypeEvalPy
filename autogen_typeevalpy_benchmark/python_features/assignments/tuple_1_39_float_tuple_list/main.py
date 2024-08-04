# Two variables are assigned a value via a tuple assignment.
def func1():
    return 36.24


def func2():
    return (71, 92, 53)


def func3():
    return [81, 9, 94]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

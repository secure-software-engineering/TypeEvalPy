# Two variables are assigned a value via a tuple assignment.
def func1():
    return (36, 28, 13)


def func2():
    return 16


def func3():
    return [54, 19, 11]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

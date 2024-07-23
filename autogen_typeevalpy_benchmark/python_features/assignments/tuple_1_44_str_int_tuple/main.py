# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'drlab'


def func2():
    return 46


def func3():
    return (8, 50, 22)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

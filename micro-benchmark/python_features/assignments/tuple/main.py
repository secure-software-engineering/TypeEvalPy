# Two variables are assigned a value via a tuple assignment.
def func1():
    return "Hello from func1"


def func2():
    return 42


def func3():
    return 42.5


a, b = func1, func2
a()
b()

c, d, e = func1, func2, func3

c()
d()
e()

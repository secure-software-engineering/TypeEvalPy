# Two variables are assigned a value via a tuple assignment.
def func1():
    return [80, 1, 3]


def func2():
    return 'caazw'


def func3():
    return 98


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

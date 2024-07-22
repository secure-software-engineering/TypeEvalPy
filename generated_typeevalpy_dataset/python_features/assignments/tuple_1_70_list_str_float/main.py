# Two variables are assigned a value via a tuple assignment.
def func1():
    return [83, 30, 94]


def func2():
    return 'dtprm'


def func3():
    return 56.43


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

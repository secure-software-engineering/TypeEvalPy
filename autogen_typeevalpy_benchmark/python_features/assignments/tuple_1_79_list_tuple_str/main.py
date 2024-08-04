# Two variables are assigned a value via a tuple assignment.
def func1():
    return [41, 96, 76]


def func2():
    return (28, 4, 26)


def func3():
    return 'zzaqj'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'sfutd'


def func2():
    return [88, 45, 66]


def func3():
    return (2, 45, 4)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

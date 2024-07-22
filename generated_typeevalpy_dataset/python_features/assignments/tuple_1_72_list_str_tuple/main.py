# Two variables are assigned a value via a tuple assignment.
def func1():
    return [18, 45, 6]


def func2():
    return 'sfbod'


def func3():
    return (65, 14, 40)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return (100, 36, 35)


def func2():
    return [16, 45, 20]


def func3():
    return 'ozghw'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

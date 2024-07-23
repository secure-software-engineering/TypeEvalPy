# Two variables are assigned a value via a tuple assignment.
def func1():
    return [26, 96, 1]


def func2():
    return (9, 35, 23)


def func3():
    return 'blqkc'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

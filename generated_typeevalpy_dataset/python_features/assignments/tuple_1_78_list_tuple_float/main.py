# Two variables are assigned a value via a tuple assignment.
def func1():
    return [89, 18, 5]


def func2():
    return (33, 18, 50)


def func3():
    return 80.23


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

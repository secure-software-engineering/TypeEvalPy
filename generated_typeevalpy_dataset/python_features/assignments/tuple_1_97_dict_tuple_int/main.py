# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'cgttg': 36, 'zlhvd': 74, 'bwzjl': 51}


def func2():
    return (16, 32, 1)


def func3():
    return 61


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

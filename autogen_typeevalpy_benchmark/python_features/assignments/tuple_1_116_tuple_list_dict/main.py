# Two variables are assigned a value via a tuple assignment.
def func1():
    return (50, 59, 89)


def func2():
    return [77, 26, 24]


def func3():
    return {'zjuof': 61, 'sgqjn': 8, 'tszwk': 57}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

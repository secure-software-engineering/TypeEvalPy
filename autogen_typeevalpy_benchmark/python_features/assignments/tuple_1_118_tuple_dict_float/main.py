# Two variables are assigned a value via a tuple assignment.
def func1():
    return (42, 91, 40)


def func2():
    return {'oaibf': 25, 'husfk': 60, 'tamus': 90}


def func3():
    return 87.18


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

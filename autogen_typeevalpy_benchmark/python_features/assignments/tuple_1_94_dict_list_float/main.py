# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'leryo': 35, 'pnhyn': 18, 'tklkt': 95}


def func2():
    return [2, 70, 30]


def func3():
    return 30.6


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

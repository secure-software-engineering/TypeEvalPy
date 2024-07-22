# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'jdzdy': 45, 'uwyey': 51, 'ghnfy': 10}


def func2():
    return 70.55


def func3():
    return (59, 80, 80)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'zjdbs': 70, 'tbvth': 77, 'dbxqa': 95}


def func2():
    return (47, 63, 26)


def func3():
    return 70.08


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

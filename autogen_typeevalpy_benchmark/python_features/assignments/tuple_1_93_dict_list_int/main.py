# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'xpcit': 23, 'jamns': 36, 'qzktu': 61}


def func2():
    return [21, 9, 6]


def func3():
    return 53


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

# Two variables are assigned a value via a tuple assignment.
def func1():
    return (10, 68, 84)


def func2():
    return {'rjnzs': 96, 'uxmkd': 92, 'nvdkb': 10}


def func3():
    return [43, 44, 33]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

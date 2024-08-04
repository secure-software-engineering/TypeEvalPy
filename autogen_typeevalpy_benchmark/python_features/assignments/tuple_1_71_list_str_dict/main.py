# Two variables are assigned a value via a tuple assignment.
def func1():
    return [9, 7, 12]


def func2():
    return 'aqlmn'


def func3():
    return {'rpchn': 42, 'plomn': 58, 'zwacg': 84}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()

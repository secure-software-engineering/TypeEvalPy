# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 13, 21)


def func2():
    return 'spynq'


def func3():
    return 85


def func4():
    return 86.84


def func5():
    return {'cqoig': 91, 'abrls': 39, 'xexvz': 64}


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()

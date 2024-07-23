# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 9, 14)


def func2():
    return {'hlezf': 12, 'torgq': 81, 'ryrtr': 86}


def func3():
    return [9, 12, 7]


def func4():
    return 'gmjpr'


def func5():
    return 55.15


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

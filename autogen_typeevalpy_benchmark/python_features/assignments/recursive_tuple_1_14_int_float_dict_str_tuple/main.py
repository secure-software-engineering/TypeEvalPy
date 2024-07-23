# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return 78.64


def func3():
    return {'wedjs': 90, 'xvoxk': 100, 'imzft': 63}


def func4():
    return 'xucyd'


def func5():
    return (67, 48, 82)


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

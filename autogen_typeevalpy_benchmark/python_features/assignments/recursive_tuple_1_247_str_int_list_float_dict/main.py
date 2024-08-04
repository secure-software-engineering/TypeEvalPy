# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vaysi'


def func2():
    return 13


def func3():
    return [52, 74, 90]


def func4():
    return 94.95


def func5():
    return {'kksdi': 44, 'cjswm': 58, 'ekfzq': 97}


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

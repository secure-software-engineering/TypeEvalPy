# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'garxx'


def func2():
    return 28.99


def func3():
    return {'ljikz': 27, 'opaea': 62, 'aiexg': 91}


def func4():
    return [8, 1, 90]


def func5():
    return 27


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

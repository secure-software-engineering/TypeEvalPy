# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'afcab'


def func2():
    return 10.51


def func3():
    return [74, 94, 78]


def func4():
    return 50


def func5():
    return {'erenw': 22, 'gtpjr': 71, 'dibfq': 30}


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

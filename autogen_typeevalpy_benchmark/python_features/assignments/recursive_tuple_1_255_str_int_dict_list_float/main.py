# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kavjv'


def func2():
    return 25


def func3():
    return {'vmpqk': 95, 'slrfq': 33, 'cxmei': 88}


def func4():
    return [92, 89, 51]


def func5():
    return 29.2


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

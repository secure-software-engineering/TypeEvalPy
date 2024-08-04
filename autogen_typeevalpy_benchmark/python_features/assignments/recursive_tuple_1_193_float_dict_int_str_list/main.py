# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 24.38


def func2():
    return {'fcgrv': 98, 'jmimr': 13, 'sxrvs': 50}


def func3():
    return 17


def func4():
    return 'iykih'


def func5():
    return [87, 94, 55]


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

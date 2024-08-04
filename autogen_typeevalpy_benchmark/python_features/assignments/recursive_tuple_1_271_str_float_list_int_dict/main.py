# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'aefdo'


def func2():
    return 97.3


def func3():
    return [90, 16, 90]


def func4():
    return 98


def func5():
    return {'beize': 88, 'qppnh': 33, 'lvtnr': 37}


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

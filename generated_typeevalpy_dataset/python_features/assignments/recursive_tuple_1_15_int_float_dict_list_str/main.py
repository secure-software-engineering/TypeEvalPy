# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return 83.58


def func3():
    return {'bjzyi': 45, 'rkums': 19, 'nbixt': 74}


def func4():
    return [57, 26, 88]


def func5():
    return 'bqxap'


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

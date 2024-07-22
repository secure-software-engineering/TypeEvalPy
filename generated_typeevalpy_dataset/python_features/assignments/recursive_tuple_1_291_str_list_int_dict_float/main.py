# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lcppa'


def func2():
    return [51, 50, 92]


def func3():
    return 25


def func4():
    return {'nuxwi': 32, 'yymuo': 70, 'rsvrz': 77}


def func5():
    return 42.09


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

# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'uwuki'


def func2():
    return 94.35


def func3():
    return 93


def func4():
    return {'gfhcl': 9, 'ruxwx': 20, 'adtge': 74}


def func5():
    return (31, 100, 12)


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

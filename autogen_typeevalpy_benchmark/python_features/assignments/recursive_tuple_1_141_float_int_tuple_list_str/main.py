# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82.15


def func2():
    return 14


def func3():
    return (33, 97, 63)


def func4():
    return [50, 15, 65]


def func5():
    return 'totxl'


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

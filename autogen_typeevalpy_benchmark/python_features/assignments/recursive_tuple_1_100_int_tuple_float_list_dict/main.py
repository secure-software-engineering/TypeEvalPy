# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56


def func2():
    return (87, 51, 16)


def func3():
    return 48.16


def func4():
    return [7, 7, 69]


def func5():
    return {'cxeth': 8, 'dmkkw': 45, 'xlvaw': 22}


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

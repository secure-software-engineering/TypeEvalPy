# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 100


def func2():
    return {'stsga': 38, 'zaoyx': 59, 'bjwwv': 19}


def func3():
    return (71, 54, 32)


def func4():
    return [27, 29, 8]


def func5():
    return 74.95


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

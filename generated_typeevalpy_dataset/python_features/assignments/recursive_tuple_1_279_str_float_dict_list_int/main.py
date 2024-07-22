# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'fiogz'


def func2():
    return 78.01


def func3():
    return {'bfxid': 55, 'lylhj': 8, 'svwvi': 10}


def func4():
    return [90, 40, 56]


def func5():
    return 26


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

# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 79


def func2():
    return 'blboh'


def func3():
    return {'aotdl': 51, 'bsusq': 2, 'zhhnx': 59}


def func4():
    return [4, 54, 76]


def func5():
    return 17.81


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

# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30.23


def func2():
    return {'htrwh': 1, 'rrglw': 68, 'kbilo': 15}


def func3():
    return 'lctal'


def func4():
    return 92


def func5():
    return [15, 35, 39]


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

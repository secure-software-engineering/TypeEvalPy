# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pgeij'


def func2():
    return [86, 32, 59]


def func3():
    return {'csfpy': 78, 'juhso': 97, 'bzsrr': 66}


def func4():
    return 45


def func5():
    return 67.89


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

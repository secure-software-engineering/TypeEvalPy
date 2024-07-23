# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72


def func2():
    return 'jwcex'


def func3():
    return (90, 52, 96)


def func4():
    return {'lqlzl': 23, 'iugnh': 99, 'eecmt': 73}


def func5():
    return [83, 59, 78]


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

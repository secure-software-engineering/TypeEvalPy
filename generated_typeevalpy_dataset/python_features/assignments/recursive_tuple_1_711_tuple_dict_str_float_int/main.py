# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (76, 52, 63)


def func2():
    return {'ikofw': 20, 'jwvga': 28, 'oudhm': 41}


def func3():
    return 'hlfpi'


def func4():
    return 96.71


def func5():
    return 36


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

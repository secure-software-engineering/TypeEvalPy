# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tcsqp': 98, 'amvbg': 79, 'zfsab': 6}


def func2():
    return 6


def func3():
    return [48, 3, 85]


def func4():
    return 'rzwxm'


def func5():
    return 45.23


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

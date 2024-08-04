# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wbjpl'


def func2():
    return [61, 70, 21]


def func3():
    return 48


def func4():
    return 66.2


def func5():
    return {'jodtj': 56, 'ekmjh': 12, 'vtmoj': 78}


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

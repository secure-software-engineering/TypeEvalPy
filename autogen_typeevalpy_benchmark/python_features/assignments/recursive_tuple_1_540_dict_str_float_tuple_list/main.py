# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kaczm': 5, 'yqfnv': 25, 'xkgzz': 86}


def func2():
    return 'oamfg'


def func3():
    return 49.17


def func4():
    return (27, 55, 18)


def func5():
    return [66, 14, 34]


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

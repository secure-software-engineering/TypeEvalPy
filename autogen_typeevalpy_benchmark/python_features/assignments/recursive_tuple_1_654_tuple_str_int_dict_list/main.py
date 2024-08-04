# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (36, 43, 64)


def func2():
    return 'rnkit'


def func3():
    return 64


def func4():
    return {'jzemh': 49, 'aklnv': 46, 'vwhbb': 33}


def func5():
    return [42, 14, 20]


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

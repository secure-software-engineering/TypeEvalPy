# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [27, 4, 33]


def func2():
    return (65, 60, 61)


def func3():
    return 'rihvg'


def func4():
    return 65.24


def func5():
    return {'vzmuv': 30, 'tixbk': 11, 'hgcww': 17}


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

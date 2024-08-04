# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (45, 8, 29)


def func2():
    return 54


def func3():
    return {'corzd': 24, 'iqvpb': 38, 'fmfbh': 40}


def func4():
    return [36, 58, 37]


def func5():
    return 'oahll'


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

# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [71, 72, 56]


def func2():
    return {'tbkrz': 43, 'dltbk': 36, 'icpcn': 17}


def func3():
    return 'ylfkv'


def func4():
    return 73


def func5():
    return 69.32


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

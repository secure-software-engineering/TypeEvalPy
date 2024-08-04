# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vubnw': 51, 'jrehj': 76, 'cmtyp': 9}


def func2():
    return 'zfvdp'


def func3():
    return 33


def func4():
    return [49, 81, 56]


def func5():
    return 26.94


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

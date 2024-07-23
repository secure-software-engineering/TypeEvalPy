# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [19, 20, 85]


def func2():
    return 'nfnxq'


def func3():
    return 4.99


def func4():
    return 94


def func5():
    return {'bhqcq': 76, 'mzmxl': 28, 'rmnml': 13}


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

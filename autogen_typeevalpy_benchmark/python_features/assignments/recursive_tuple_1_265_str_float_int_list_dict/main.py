# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'arvyp'


def func2():
    return 19.0


def func3():
    return 3


def func4():
    return [63, 86, 73]


def func5():
    return {'iicje': 11, 'qrxcy': 46, 'yfqhu': 78}


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

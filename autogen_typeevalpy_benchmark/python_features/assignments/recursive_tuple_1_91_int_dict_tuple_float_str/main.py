# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 32


def func2():
    return {'ugypu': 40, 'auovw': 43, 'cdtxv': 62}


def func3():
    return (20, 32, 8)


def func4():
    return 54.81


def func5():
    return 'goabo'


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

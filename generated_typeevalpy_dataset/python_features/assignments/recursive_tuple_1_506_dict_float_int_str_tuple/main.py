# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tsqrg': 46, 'asfsq': 96, 'kcctw': 94}


def func2():
    return 58.37


def func3():
    return 38


def func4():
    return 'pzkxe'


def func5():
    return (1, 55, 89)


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

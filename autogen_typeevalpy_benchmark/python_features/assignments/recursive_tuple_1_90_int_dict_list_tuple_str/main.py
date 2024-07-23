# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 55


def func2():
    return {'bngav': 68, 'zxfgj': 28, 'zcpdc': 29}


def func3():
    return [59, 25, 65]


def func4():
    return (13, 79, 4)


def func5():
    return 'wsfcw'


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

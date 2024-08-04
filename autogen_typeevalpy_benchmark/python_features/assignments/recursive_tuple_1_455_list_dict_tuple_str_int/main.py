# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 60, 100]


def func2():
    return {'nkprd': 41, 'uslkr': 35, 'eqkqx': 90}


def func3():
    return (11, 88, 23)


def func4():
    return 'zxrex'


def func5():
    return 73


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

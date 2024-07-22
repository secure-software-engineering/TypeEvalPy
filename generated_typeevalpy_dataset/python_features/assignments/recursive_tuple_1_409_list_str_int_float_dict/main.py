# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 94, 21]


def func2():
    return 'xlxdm'


def func3():
    return 8


def func4():
    return 36.89


def func5():
    return {'tgemm': 97, 'knmro': 28, 'zecce': 83}


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

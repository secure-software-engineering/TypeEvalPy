# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mkrdd': 49, 'pglzb': 78, 'sphlp': 87}


def func2():
    return 59


def func3():
    return 'dmgej'


def func4():
    return [59, 57, 51]


def func5():
    return (100, 69, 13)


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

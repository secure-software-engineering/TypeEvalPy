# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 57.94


def func2():
    return {'ilgxt': 50, 'ibrpj': 61, 'xdmwb': 32}


def func3():
    return 92


def func4():
    return 'rgvod'


def func5():
    return [18, 14, 49]


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

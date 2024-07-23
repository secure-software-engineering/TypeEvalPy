# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [57, 56, 26]


def func2():
    return 'asqzs'


def func3():
    return {'jetbe': 97, 'mgyqk': 87, 'iexmj': 86}


def func4():
    return 33


def func5():
    return (80, 99, 30)


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

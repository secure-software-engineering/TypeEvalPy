# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [71, 71, 19]


def func2():
    return 24.41


def func3():
    return {'eqsgp': 51, 'xfoik': 38, 'mqtwf': 32}


def func4():
    return 'yoggv'


def func5():
    return 100


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

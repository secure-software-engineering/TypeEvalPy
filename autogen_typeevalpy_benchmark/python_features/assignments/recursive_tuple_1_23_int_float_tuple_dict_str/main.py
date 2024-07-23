# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63


def func2():
    return 24.21


def func3():
    return (20, 99, 90)


def func4():
    return {'avzkx': 4, 'juxfr': 97, 'gkbec': 90}


def func5():
    return 'nrcli'


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

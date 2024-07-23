# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (90, 44, 1)


def func2():
    return {'kngzj': 68, 'djojt': 80, 'njajz': 49}


def func3():
    return 'womde'


def func4():
    return 51.66


def func5():
    return [23, 5, 82]


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

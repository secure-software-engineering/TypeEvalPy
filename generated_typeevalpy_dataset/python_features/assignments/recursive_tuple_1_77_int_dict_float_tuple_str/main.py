# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 80


def func2():
    return {'lnemi': 13, 'lhfcz': 2, 'aartk': 64}


def func3():
    return 14.23


def func4():
    return (56, 30, 10)


def func5():
    return 'mqgdb'


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

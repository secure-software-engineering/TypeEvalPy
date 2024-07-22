# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 48.2


def func2():
    return 3


def func3():
    return 'fglme'


def func4():
    return (41, 2, 74)


def func5():
    return {'iwoeg': 41, 'qctvf': 6, 'mfdma': 75}


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

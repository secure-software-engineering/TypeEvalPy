# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [66, 64, 64]


def func2():
    return {'xlqux': 43, 'qimkk': 30, 'ppoib': 8}


def func3():
    return 6


def func4():
    return 'zlgbr'


def func5():
    return (77, 47, 9)


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

# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [30, 57, 45]


def func2():
    return {'fvevr': 85, 'idgdx': 10, 'kicda': 31}


def func3():
    return 'ehwcs'


def func4():
    return (28, 33, 13)


def func5():
    return 52


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

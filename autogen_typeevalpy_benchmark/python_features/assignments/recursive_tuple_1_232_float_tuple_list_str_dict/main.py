# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75.79


def func2():
    return (11, 85, 91)


def func3():
    return [33, 81, 82]


def func4():
    return 'hufji'


def func5():
    return {'ahjqr': 74, 'ypyod': 74, 'jwhjm': 91}


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

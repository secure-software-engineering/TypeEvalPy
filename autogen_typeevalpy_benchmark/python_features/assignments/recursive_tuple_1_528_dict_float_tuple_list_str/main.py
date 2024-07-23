# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dkwcm': 48, 'xyhrn': 66, 'etumi': 52}


def func2():
    return 82.04


def func3():
    return (68, 28, 33)


def func4():
    return [14, 54, 16]


def func5():
    return 'diyme'


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

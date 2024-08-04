# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (72, 48, 91)


def func2():
    return 'rqzfe'


def func3():
    return {'cwtbj': 33, 'tnpua': 50, 'mfhjm': 23}


def func4():
    return [94, 16, 45]


def func5():
    return 74.56


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
